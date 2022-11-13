from os import linesep
import re
import copy

#TODO: support splines
# support for "whitenoise"

filename = "/Users/henryhoward/PyHumModInitialWork/src/hummod.py"

id = 0

data = {
    "nodes": {},
    "edges": []
}

"""
{
    "nodes":{
        "FebrileConvulsions": {"formula":[
                    ["init": <initial expression>]
                    [[list of conditions], <expression>]
                ]
            }
        },
    ],
    "edges":[
        {
            "from":"42cd723b-ec9d-440a-841b-1875525cfdf7",
            "to":"FebrileConvulsions",
            "id":"b08e1424-f505-4741-8ff9-d32c60bf46f0"
        }
    ]
}
"""        

def set_node(id, formula):
    data["nodes"][id] = {
            "formula":formula
        }

def add_edge(data, from_id, to_id):
    global id
    data["edges"].append(
        {
            "from":from_id,
            "to":to_id,
            "id": id,
        }
    )
    id += 1


def get_all_classes(contents):
    matches = re.findall(r'class(?:\n|.)*?\n(?=\w)', contents)
    #all_class_contents = [match.group() for match in matches]
    #return all_class_contents
    return matches

def get_class_variable_expressions(class_contents):
    class_name_match = re.search(r'class (\w*?):', class_contents)
    class_name = class_name_match.group(1)
    init_block_match = re.search(r'def __init__\(self\):\n((\n|.)*?)def', class_contents)
    if init_block_match:
        init_block_string = init_block_match.group().split('\n')
        expressions = []
        for line in init_block_string:
            if "=" in line:
                left, right = line.split('=')
                left = left.replace("self.", class_name+".")
                right = right.replace("self.", class_name+".")
                expressions.append((left.strip(), right.strip()))
        return expressions
        
    else:
        return []

def get_var_definition(var, class_contents):
    return []
    """
        special cases:
        impliciteq
            need to find implicit equation definition, copy it into the formula
        diffeq, delay
        if statements

    """

def init_nodes(file_contents, data):
    for class_n in get_all_classes(file_contents):
        expressions = get_class_variable_expressions(class_n)
        for expression in expressions:
            set_node(expression[0], [["init", expression[1]]])

def get_class(class_name, file_contents):
    match = re.search(r'(class {}:(.|\n)*?)\n(\w)'.format(class_name), file_contents)
    if match:
        return match.group(1)
    else:
        raise Exception("class: {} does not exist".format(class_name))

def get_function(class_name, function_name, file_contents):
    class_contents = get_class(class_name, file_contents)
    func_match = re.search(r'( *)def {}\(self\): *\n'.format(function_name), class_contents)
    indent = func_match.group(1)
    if func_match:
        function_regex = r'( *def {}\(self\): *\n(.|\n)*?)(?:\n{}\w|\Z)'.format(function_name, indent)
        full_func_match = re.search(function_regex, class_contents)
        return full_func_match.group(1)
    else:
        raise Exception("function: {} does not exist".format(function_name))

def extract_conditional_blocks(function_contents):
    """
    finds conditional blocks (if ... elif... else... )in a function, removes them and returns them

    input:
    function contents (str): the contents of a function

    returns:
    function_contents (str): contents of the function, with "#conditional block" in place of conditional blocks
    conditional_blocks (list of strings): a list of the conditional block strings, in order
    """

    conditional_blocks = []

    if_line_match = re.search(r'(?:\n|^)(( *)if .*?)(?:$|\n)', function_contents)
    while if_line_match:
        match_start_onwards = function_contents[if_line_match.start():]
        indent = if_line_match.group(2)
        conditional_block_regex = r'(?:\n|^)( *if .*?\n(?:.|\n)*?)(?:(?=\Z|\n{}(?!(else|elif| ))))'.format(indent)
        conditional_block_match = re.match(conditional_block_regex, match_start_onwards)
        conditional_block_str = conditional_block_match.group(1)
        conditional_blocks.append(conditional_block_str)
        function_contents = function_contents.replace(conditional_block_str, "#conditional block")
        if_line_match = re.search(r'(\n|^){}if .*?($|\n)'.format(indent), function_contents)
    return function_contents, conditional_blocks

def extract_implicit_blocks(function_contents):
    """
    finds implicit equation definitions and implementations in a function, removes them and returns them

    input:
    function contents (str): the contents of a function

    returns:
    function_contents (str): contents of the function, with "#implicit block" in place of implicit blocks
    implicit_blocks (list of strings): a list of the implicit block strings, in order
    """

    implicit_blocks = []

    implicit_match = re.search(r'(?:\n|^)( *)def .*?implicitfunc.*?\n', function_contents)
    
    while implicit_match:
        match_start_onwards = function_contents[implicit_match.start():]
        indent = implicit_match.group(1)
        implicit_block_regex = r'(?:\n|^)(( *)def .*?implicitfunc.*?\n(\n|.)*?{}.*?impliciteq.*)\n'.format(indent)
        implicit_block_match = re.match(implicit_block_regex, match_start_onwards)
        implicit_block_str = implicit_block_match.group(1)
        print("&&&extracted string:>>{}<<".format(implicit_block_str))
        implicit_blocks.append(implicit_block_str)
        function_contents = function_contents.replace(implicit_block_str, "#implicit block")
        implicit_match = re.search(r'(?:\n|^)( *)def .*?implicitfunc.*?\n', function_contents)

    return function_contents, implicit_blocks

def find_splines(file_contents):
    all_splines = []
    all_class_matches = get_all_classes(file_contents)
    for class_match in all_class_matches:
        class_contents = class_match
        class_name_match = re.search(r'(\w*):', class_contents)
        class_name = class_name_match.group(1)
        print("====")
        print(class_contents)
        print(class_name)
        spline_matches = re.findall(r'def (\w.*curve).*\n.*cubic_hermite_spline\(x, (.*)\)', class_contents)
        print("spline matches:", spline_matches)
        for match in spline_matches:
            spline_name = class_name + "." + match[0]
            spline_params = match[1]
            print("~~~spline:", spline_name, spline_params)
            all_splines.append([spline_name, spline_params])
    return all_splines

def inverse_condition(condition_string):
    operator_inv_dict = {
        "==":"!=",
        "!=":"==",
        "<=":">",
        ">=":"<",
        "<":">=",
        ">":"<=",
        "and": "or",
        "or": "and",
        "not": ""
    }

    #replace all "if not X" with "if X == False"
    if_true_regex = r'(not( |\(|\))*(\w+\.+\w*))(?=(( |\(|\))*)($|or |and |not ))'
    condition_string = re.sub(if_true_regex, r'\g<3> != True', condition_string)

    #replace all "if X" with "if X == True"
    if_true_regex = r'((if|elif| or| and|^)( |\(|\))*(\w+\.+\w*))(?=(( |\(|\))*)($|or |and |not ))'
    condition_string = re.sub(if_true_regex, r'\g<1> == True', condition_string)

    operator_matches = re.finditer(r'(==|!=|<=|>=|<|>|(?<= )and(?= )|(?<= )or(?= )|not(?= ))', condition_string)
    
    operator_matches = list(operator_matches)
    operator_matches.reverse()
    for operator_match in operator_matches:
        operator = operator_match.group(1)
        new_operator = operator_inv_dict[operator]
        operator_start = operator_match.start()
        operator_end = operator_match.end()
        condition_string = condition_string[:operator_start] + new_operator + condition_string[operator_end:]
    condition_string = re.sub(r'!= True( |$)', r'== False\g<1>', condition_string)
    return condition_string

def process_implicit_block(class_name, data, implicit_blocks, conditions):
    print("processing implicit blocks {} with conditions:".format(implicit_blocks), conditions)
    implicit_block = implicit_blocks.pop(0)
    print("!!! implicit block>>>{}<<<".format(implicit_block))
    vars = re.findall(r'[a-zA-Z_]+\.[a-zA-Z_]+\s', implicit_block)
    #for var in vars:
    matches = re.search(r'((.|\n)*)\n *self.(\w*) = impliciteq', implicit_block)
    implicit_eq = matches.group(1)
    dependent_var = class_name + "." + matches.group(3)
    print(matches)
    print("dependent var:", dependent_var)
    print("implicit_eq:", implicit_eq)

    #for every 

    #set_node()

def process_conditional_block(class_name, conditional_block, data, implicit_blocks, conditions=[]):
    local_conditions = copy.copy(conditions) #need to create a local copy of the initial conditions
    indent_match = re.match(r'\W*', conditional_block)
    indent = indent_match.group()
    cases_regex = r'(?:^|\n){0}(if|elif|else) *(.*?): *\n((?:\n|.)*?)(?=\n{0}(?:if|elif|else)|$)'.format(indent) #extracts the condition and the contents of that condition
    cases = re.findall(cases_regex, conditional_block) 
    #cases has the form: [<"if" or "elif" or "else">, <condition>, <code to execute>]
    for case in cases:
        if_elif_else = case[0]
        condition = case[1]
        condition = condition.replace(" self.", " {}.".format(class_name))
        condition = re.sub(r'(^| )self\.', r'\g<1>{}.'.format(class_name), condition)
        if re.match(r'^\w*\.\w*$', condition):
            condition += " == True"
        condition_content = case[2]
        condition_content, conditional_subblocks = extract_conditional_blocks(condition_content)
        case_lines = condition_content.split('\n')
        for case_line in case_lines:
            #empty line
            if case_line.strip() == "":
                pass
            elif case_line.strip() == "pass":
                pass
            elif re.match(r'#conditional block', case_line):
                process_conditional_block(class_name, conditional_subblocks.pop(0), data, implicit_blocks, local_conditions+[condition])
            elif re.match(r'#implicit block', case_line):
                process_implicit_block(class_name, data, implicit_blocks, local_conditions+[condition])
            elif re.match(r'^ *.*\(\)', case_line):
                process_function_call_line(class_name, case_line, file_contents, data, local_conditions+[condition])
            elif re.match(r'^ *.*=.*$', case_line):
                process_expression(class_name, case_line, data, local_conditions+[condition])
            else:
                raise Exception("conditional case contains unprocessable line:", case_line)
        if condition not in ["True", "False"]:
            local_conditions += [inverse_condition(condition)]

def process_expression(class_name, line, data, conditions):
    left_var_match = re.search(r'^ *(\w*\.(\w|.)*?) *=', line)
    left_var = left_var_match.group(1)
    left_var = left_var.replace("self.", class_name+".")
    left_var_match.end()
    right_side = line[left_var_match.end():]
    right_side = re.sub(r'(^| )self\.', r'\g<1>{}.'.format(class_name), right_side)
    if left_var not in data["nodes"]:
        set_node(left_var, [["init", None]])
    set_node(left_var, data["nodes"][left_var]["formula"] + [[conditions, right_side]])
    right_vars = re.findall(r'(\w*[A-Za-z]+\w*\.\w*[A-Za-z]+\w*)(?: |$|\n)', right_side)
    for right_var in right_vars:
        if right_var not in data["nodes"].keys():
            set_node(right_var, [["init", None]])

    #process_expression(line, class_name)
    #if the left hand side is a node: we will be creating new edges now
    #if the left hand side is not a node, it may be used to create an edge later
    #for all variables on the the right:
    #   if variable represents a node:

def edges_from_nodes(data):
    #processes a formula for a node, extracts out all variable names and adds edges from these to the node
    for node in list(data["nodes"]):
        node_formula = data["nodes"][node]["formula"]
        vars = re.findall(r'[a-zA-Z_]+\.[a-zA-Z_]+\s', str(node_formula))
        vars = list(set(vars)) #remove duplicates
        for var in vars:
            add_edge(data, var, node)

def process_function_call_line(class_name, line, file_contents, data, conditions):
    print("processing function call line with conditions:>->{}<-<".format(conditions))
    func_call_match = re.match(r'^ *(.*)\.(.*)\(\)', line)
    func_class = func_call_match.group(1)
    if func_class == "self":
        func_class = class_name
    func_name = func_call_match.group(2)
    process_function(func_class, func_name, file_contents, data, conditions=conditions)

def process_function(class_name, function_name, file_contents, data, conditions=[]):

    print('processing func: {}.{}'.format(class_name, function_name))

    function_contents = get_function(class_name, function_name, file_contents)

    function_contents, implicit_blocks = extract_implicit_blocks(function_contents)

    function_contents, conditional_blocks = extract_conditional_blocks(function_contents)

    lines = function_contents.split("\n")
    
    for line in lines[1:]:

        #empty line
        if line.strip() == "":
            pass

        #simple expression
        elif re.match(r'^ *.*=.*$', line):
            process_expression(class_name, line, data, conditions=conditions)

        #function call
        elif re.match(r'^ *.*\(\)', line):
            process_function_call_line(class_name, line, file_contents, data, conditions=conditions)

        #conditional block
        elif re.match(r'#conditional block', line):
            process_conditional_block(class_name, conditional_blocks.pop(0), data, implicit_blocks, conditions=conditions)

        #implicit block
        elif re.match(r'#implicit block', line):
            process_implicit_block(class_name, data, implicit_blocks, conditions)

        else:
            print("###orphan line:", line)

with open(filename, "r") as file:
    file_contents = file.read()
    all_splines = find_splines(file_contents)
    init_nodes(file_contents, data)
    process_function("Structure", "Context_func", file_contents, data)
    process_function("Structure", "Parms_func", file_contents, data)
    process_function("Structure", "Dervs_func", file_contents, data)
    process_function("Structure", "Wrapup_func", file_contents, data)
    edges_from_nodes(data)
    print(data["edges"][-100:])
    for n in [[key, data["nodes"][key]] for key in list(data["nodes"].keys())[-100:]]:
        print(n)
    print(all_splines)
    #all_classes = get_all_classes(file_contents)

To_ignore = [
    "Symptoms",
    "DailyPlannerControl",
    "ThiazideDailyDose",
    "MidodrineDailyDose",
    "DigoxinDailyDose",
    "DialyzerActivity.Wrapup_func",
    "Exercise_Bike",
    "Exercise_Treadmill",
    "Exercise_Motivation",
    "Exercise_Metabolism",
    "Exercise_Control",
    "Pheochromocytoma.Wrapup_func",
    "Heart_VFib",
    "PeripheralResistance",
    "CPR_Heart"
]

#DialyzerActivity and the exercise things have some bits that are useful, can add this in later

#PeripheralResistance is a useful metric but it is not defined in the correct causal direction in HumMod

#NOTE: get rid of "switch","clamp switch"

#TODO: