import re
import copy
import json

# This script takes hummod.py and outputs a causal network in the form of nodes and edges

#TODO ========
# ignore useless parts:
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
    "CPR_Heart",
    "PeripheralResistance" #PeripheralResistance is a useful clinical metric but it is not defined in the correct causal direction in HumMod
    "AirSupply_GasTanks",
]

#DialyzerActivity and the exercise things have some bits that are useful, can add this in later

#what to do about "whitenoise" (only implemented in phaeochromocytoma) - replace with probability distributions?

#get rid of "switch", "clamp switch" etc.

#=========


filename = "src/hummod.py"

id = 0

data = {
    "nodes": {},
    "edges": []
}

"""
data is of the form:

{
    "nodes":{
        "FebrileConvulsions": {"formula":[
                    ["init": <initial expression>]
                    [[list of conditions], <expression>]
                ]
            }
        },
        ...
    ],
    "edges":[
        {
            "from":"42cd723b-ec9d-440a-841b-1875525cfdf7",
            "to":"FebrileConvulsions",
            "id":"b08e1424-f505-4741-8ff9-d32c60bf46f0"
        },
        ...
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
        spline_matches = re.findall(r'def (\w.*curve).*\n.*cubic_hermite_spline\(x, (.*)\)', class_contents)
        for match in spline_matches:
            spline_name = class_name + "." + match[0]
            spline_params = match[1]
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
    implicit_block = implicit_blocks.pop(0)

    matches = re.search(r'((.|\n)*)\n *self.(\w*) = impliciteq', implicit_block)
    implicit_eq = matches.group(1)
    dependent_var = class_name + "." + matches.group(3)

    #some implicit blocks contain conditional blocks
    implicit_block, conditional_blocks = extract_conditional_blocks(implicit_block)

    #find the input, replace with the dependent variable name
    input_name = re.search(r'implicitfunc\((.*)\)', implicit_eq).group(1)
    implicit_eq = re.sub(r' {} '.format(input_name), dependent_var ,implicit_eq)

    #replace all "self."" with the class name
    implicit_block = re.sub(r'\bself.', class_name+".", implicit_block)

    implicit_block_lines = implicit_block.split('\n')

    expressions = []

    for line in implicit_block_lines[1:-4]+implicit_block_lines[-1:]: #ignore first line
        if re.match(r'#conditional block', line):
            raw_expressions = process_conditional_block(class_name, conditional_blocks.pop(0), data, implicit_blocks, conditions)
        elif re.match(r'^ *.*\(\)', line):
            raw_expressions = process_function_call_line(class_name, line, file_contents, data, conditions)
        elif re.match(r'^ *.*=.*$', line):
            raw_expressions = [process_expression(class_name, line, data, conditions)]
        else:
            raise Exception("conditional case contains unprocessable line:", line)

        #need to replace formulae with the full implicit eq
        processed_expressions = []
        for i, expression in enumerate(raw_expressions):
            processed_expressions.append([expression[0], []])
            for case in expression[1]:
                case_conditions = case[0] #ignore these
                case_right_side = "start_implicit_block" + implicit_block + "end_implicit_block"
                processed_expressions[i][1].append([conditions, case_right_side])
        
        expressions += processed_expressions


    return expressions

def process_conditional_block(class_name, conditional_block, data, implicit_blocks, conditions=[]):
    """
    takes a conditional_block, returns all expressions within it and their conditions

    returns
        list of the form:
        [
            ['DigoxinPool.Change', [
                    ['init', None],
                    [[], ' DigoxinPool.Gain - DigoxinPool.Loss']
                ]   
            ]
            ['TGF_Vascular.Steady_State', [
                    ['init', None],
                    [['TGF_Vascular.Clamp == True'], ' TGF_Vascular.Level'],
                    [['TGF_Vascular.Clamp == False', ''],' TGF_Vascular.BasicSignal * TGF_Vascular.NaEffect * TGF_Vascular.A2Effect * TGF_Vascular.ANPEffect * TGF_Vascular.FurosemideEffect']
                ]
            ]
        ]
    """
    expressions = []
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
                expressions += process_conditional_block(class_name, conditional_subblocks.pop(0), data, implicit_blocks, local_conditions+[condition])
            elif re.match(r'#implicit block', case_line):
                expressions += process_implicit_block(class_name, data, implicit_blocks, local_conditions+[condition])
            elif re.match(r'^ *.*\(\)', case_line):
                expressions += process_function_call_line(class_name, case_line, file_contents, data, local_conditions+[condition])
            elif re.match(r'^ *.*=.*$', case_line):
                expressions.append(process_expression(class_name, case_line, data, local_conditions+[condition]))
            else:
                raise Exception("conditional case contains unprocessable line:", case_line)
        if condition not in ["True", "False"]:
            local_conditions += [inverse_condition(condition)]
    return expressions

def process_expression(class_name, line, data, conditions):
    left_var_match = re.search(r'^ *(\w*\.(\w|.)*?) *=', line)
    left_var = left_var_match.group(1)
    left_var = left_var.replace("self.", class_name+".")
    left_var_match.end()
    right_side = line[left_var_match.end():]
    right_side = re.sub(r'(^| )self\.', r'\g<1>{}.'.format(class_name), right_side)
    expression = [left_var, [[conditions, right_side]]]
    return expression

def create_nodes_from_expression(expression, data):
    #create entries in the data dictionary for the variables mentioned in an expression

    #create nodes for the appropriate variables in the conditions
    for case in expression[1]:
        condition = str(case[0])
        condition_vars = re.findall(r'(\w*[A-Za-z]+\w*\.\w*[A-Za-z]+\w*)(?: |$|\n)', condition)
        for condition_var in condition_vars:
            if condition_var not in data["nodes"].keys():
                set_node(condition_var, [["init", None]])

        #create nodes for the variables on the right side (accounting for implicit blocks)
        right_side = case[1]
        implicit_block_match = re.match(r'start_implicit_block<((\n|.)*?)>end_implicit_block', right_side)
        if not implicit_block_match:
            #create nodes for the appropriate variables on the right side
            right_vars = re.findall(r'(\w*[A-Za-z]+\w*\.\w*[A-Za-z]+\w*)(?: |$|\n)', right_side)
            for right_var in right_vars:
                if right_var not in data["nodes"].keys():
                    set_node(right_var, [["init", None]])

    #create a node for the variable on the left side
    left_var = expression[0]
    if left_var not in data["nodes"].keys():
        set_node(left_var, [["init", None], [condition, right_side]])
    else:
        left_var_pre = data["nodes"][left_var]["formula"]
        set_node(left_var, left_var_pre + [[condition, right_side]])

blah=['LungO2.Uptake', [], [['Breathing.AlveolarVentilation_STPD > 0.0'], 'start_implicit_block        def Uptakeimplicitfunc(Uptake):\n            LungO2.conc_Alveolar = Bronchi.conc_O2 - ( Uptake / Breathing.AlveolarVentilation_STPD )\n            LungO2.PAlveolar = LungO2.conc_Alveolar * Barometer.Pressure\n            LungO2.MembraneGradient = Uptake / PulmonaryMembrane.Permeability\n            LungO2.PCapy = LungO2.PAlveolar - LungO2.MembraneGradient\n            HgbLung.pO2 = LungO2.PCapy\n            HgbLung.PO2ToO2_func()\n            LungO2.conc_Capy = HgbLung.conc_O2\n            EndUptake = LungBloodFlow.AlveolarVentilated * ( LungO2.conc_Capy - LungArtyO2.conc_O2 )\n\n            return EndUptake\n        LungO2.Uptake = impliciteq( Uptakeimplicitfunc, LungO2.Uptake, 2.5)end_implicit_block']]


def edges_from_nodes(data):
    #processes a formula for a node, extracts out all variable names and adds edges from these to the node
    for node in list(data["nodes"]):
        node_formula = data["nodes"][node]["formula"]
        formula_string = str(node_formula)
        vars = re.findall(r'\b\w*[a-zA-Z]+\w*\.\w*[a-zA-Z]+\w*(?= |\'|"|$)', formula_string)
        print("formula:", node_formula)
        print("vars:", vars)

        vars = list(set(vars)) #remove duplicates
        for var in vars:
            print("    var:", var)
            add_edge(data, var, node)

def process_function_call_line(class_name, line, file_contents, data, conditions):
    func_call_match = re.match(r'^ *(.*)\.(.*)\(\)', line)
    func_class = func_call_match.group(1)
    if func_class == "self":
        func_class = class_name
    func_name = func_call_match.group(2)
    expressions = process_function(func_class, func_name, file_contents, data, conditions=conditions)
    return expressions

def process_function(class_name, function_name, file_contents, data, conditions=[]):

    function_contents = get_function(class_name, function_name, file_contents)

    function_contents, implicit_blocks = extract_implicit_blocks(function_contents)

    function_contents, conditional_blocks = extract_conditional_blocks(function_contents)

    lines = function_contents.split("\n")

    expressions = []
    
    for line in lines[1:]:

        #empty line
        if line.strip() == "":
            pass

        #simple expression
        elif re.match(r'^ *.*=.*$', line):
            expressions.append(process_expression(class_name, line, data, conditions=conditions))

        #function call
        elif re.match(r'^ *.*\(\)', line):
            function_call_line_output = process_function_call_line(class_name, line, file_contents, data, conditions=conditions)
            expressions += function_call_line_output

        #conditional block
        elif re.match(r'#conditional block', line):
            expressions += process_conditional_block(class_name, conditional_blocks.pop(0), data, implicit_blocks, conditions=conditions)

        #implicit block
        elif re.match(r'#implicit block', line):
            expressions += process_implicit_block(class_name, data, implicit_blocks, conditions)

        else:
            print("###orphan line:", line)
        
    return(expressions)

with open(filename, "r") as file:
    file_contents = file.read()
    all_splines = find_splines(file_contents)
    init_nodes(file_contents, data)
    expressions = []
    expressions += process_function("Structure", "Context_func", file_contents, data)
    expressions += process_function("Structure", "Parms_func", file_contents, data)
    expressions += process_function("Structure", "Dervs_func", file_contents, data)
    expressions += process_function("Structure", "Wrapup_func", file_contents, data)
    for expression in expressions:
        create_nodes_from_expression(expression, data)
    edges_from_nodes(data)

    #print(all_splines)

    #all_classes = get_all_classes(file_contents)

with open("data_dump.txt", "w") as file:
    nodes = [{"id": key, "label":key} for key in data["nodes"].keys()]
    file.write(json.dumps(nodes) + "\n\n\n\n\n" + json.dumps(data["edges"]))