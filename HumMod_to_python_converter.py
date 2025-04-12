import os
import re

'''
This script converts the .DES HumMod library into a python file. Every .DES file becomes a class
'''

def create_module(path, filename, file_contents):
    # os.makedirs(path)
    pass

def remove_comments(string):
    return re.sub("<!--((.|\n)*?)-->", '', string) 

def find_sub_elements(parent_element_name, string, cursor):
    '''
    parent_element_name is the name of the element in which we are currently searching
    string is the full text of the xml file we are converting
    cursor is a string index. It's the position we're currently searching from in the string

    returns the list and a cursor

    TODO: ignore: <!--
    '''
    element_list = [parent_element_name, "", []]
    done = False
    while not done:
        next_element = re.search("<(.*?)>", string[cursor:])
        if next_element:
            parent_element_text = string[cursor:cursor +
                                         next_element.start()].replace("\r", "").replace("\n", "")
            element_list[1] += parent_element_text
            next_element_name = next_element.groups()[0]
            cursor += next_element.end()
            if next_element_name[0] == "/":  # look for the closing </element>
                if next_element_name != "/"+parent_element_name:
                    raise Exception("error: unclosed element:",
                                    parent_element_name)
                else:
                    # this is the closing </element>, so can end the loop
                    done = True
            elif next_element_name[0] == "?":
                import_match = re.search(r'\?include( .* )\?', next_element_name)
                if import_match:
                    import_target = import_match.group(1).replace(".DES", "")
                    import_target = re.sub(r'.*\\(.*?) ', r' \g<1> ',import_target)
                    element_list[2].append(["?include", import_target, []])
                # it's one of those wierd XML elements. Cannot have children
                pass
            elif next_element_name[-1] == "/":
                # it's <exitblock/>
                element_list[2].append(["exitblock/", "", []])
            else:
                # new element, need to subsearch
                subsearch = find_sub_elements(
                    next_element_name, string, cursor)
                element_list[2].append(subsearch[0])
                cursor = subsearch[1]
        else:
            # there is no next_element. We have reached the end of the document
            done = True
    if len(element_list) < 3:
        element_list.append([])
    return [element_list, cursor]

def find_child_els_by_name(element, name):
    ''' finds the immediate child elements of the given name and returns them
    if can't find, returns False
    '''
    ret = False
    children = element[2]
    ret = []
    for child in children:
        if child[0] == name:
            ret.append(child)
    return ret

def create_xml_tree(path, filename):
    '''create a list of nested lists in which each list is two elements: the name of the element, then a list of nested elements like:
        ['rootelement', 'text_content', [
            ['nest1elem1', 'text_content', [
                ['nest2elem1', 'text_content', []],
                ['nest2elem2'], 'text_content', []],
                ['nest2elem3', 'text_content', [
                    ['nest3elem1', 'text_content', []],
                ],
            ],
            ['nest1elem2', 'text_content', []],
            ['nest1elem3'], 'text_content', []],
        ]
    '''
    f = open(path+"/"+filename, 'r')
    raw_text = f.read()

    # shave the junk
    start_junk = re.search("<", raw_text)
    if not start_junk:
        return ['root', '', []]  # Some files in HumMod are empty
    else:
        start_point = start_junk.end()-1
        end_junk = re.search("\nEnd", raw_text)
        end_point = end_junk.start()
        text = raw_text[start_point:end_point]

        text = remove_comments(text)

        # first_element = re.search("<(.*?)>", text)
        # first_element_close = re.search("</"+first_element.groups()[0]+">", text)
        cursor = 0
        tree = find_sub_elements("root", text, cursor)[
            0]  # [0] only want the tree
        return tree

def parse_xml_subelements(element_list, memory):
    code = ''
    for element in element_list:
        subcode, memory = parse_xml_element(element, memory)
        code += subcode
    return code, memory

def char_repair(string):
    # "-" is used in variable names as a hyphen or charge but sometimes "-" indicates a negative value or an index eg. "-4.0e-5"
    # get rid of the hyphens in the middle of variables and the negative at the end of ions
    string = re.sub(r'((?:\d|\w|_)*(?:[a-df-zA-DF-Z]|_)(?:\d|\w|_)*)-', r'\g<1>_', string)
    # "+" is used in variable names to indicate combination or charge
    string = re.sub(r' (\S+)\+', r' \g<1>_', string)
    # "/" is used in variable names when specifying units eg. mg/mL
    string = re.sub(r' (\S+?)/', r' \g<1>per', string)
    # "%" is used in eg. "Sat(%)" or Area%
    string = re.sub(r' (\S+)\%', r' \g<1>percent', string)
    # parentheses without spaces around them are used in variable names
    string = re.sub(r'\((\S+)\)', r'_\g<1>', string)
    # square brackets without spaces inside them are used in variable names to indicate concentration
    string = re.sub(r'\[(\S+)\]', r'conc_\g<1>', string)
    # some variable names have a question mark on the end
    if re.search(r'(?<=\.|\s)(\w+?)\?', string):
        print("@@@", re.search('(?<=\.|\s)(\w+?)\?', string))
    string = re.sub(r'(?<=\.|\s)(\w+?)\?', r'query_\g<1>', string)
    # some variable names have an equals sign in them
    string = re.sub(r'(\S+)=(\S+)', r'\g<1>_equals_\g<2>', string)
    # some variable names have ampersand in them
    string = re.sub(r'(\S+)&(\S+)', r'\g<1>_and_\g<2>', string)

    return string

def format_names(string):
    '''
    removes special characters from all variable names in an expression

    takes a string, replaces "-", "+", "/", "[", "]", "(", ")" that are parts of variables with replacements

    eg.
    "Pressure + -4.0e-5 ^ ( ( ( Altitude.Feet MAX [O2] ) GT Rate(mL/min) ) * INVERT RespRate"
    =>
    "Pressure + -4.0e-5 ^ ( ( ( Altitude.Feet MAX conc_O2 ) GT Rate_mLperL ) * INVERT RespRate"
    '''

    new_string = char_repair(string)

    while new_string != string: #need to run recursively until fully formatted because regex matches sometimes overlap
        string = new_string
        new_string = char_repair(new_string)
    string = new_string

    #get rid of excessive spaces again (can't be bothered figuring out the real problem)
    string = re.sub(r' +', r' ', string)

    # remove space from start and end of string
    string = re.sub(r'^ ', '', string)
    string = re.sub(r' $', '', string)

    return string

def find_opposing_bracket(string, index, direction="forward"):
    '''
    takes a string, the index of a parenthesis in the string and returns the index of the opposing parenthesis
    '''

    depth = 0
    step = 1
    opener = "("
    closer = ")"
    if direction == 'backward':
        step = -1
        opener = ")"
        closer = "("
    elif direction != "forward":
        raise Exception("invalid direction, give 'forward' or 'backward'")
    found = False
    while not found:
        index += step
        char = string[index]
        if char == opener:
            depth += 1
        elif (char == closer) and (depth == 0):
            found = True
        elif char == closer:
            depth -= 1
    return index

def process_minmax(string):
    '''
    looks for every " MAX " or " MIN " in a string, changes the string around so that:
    "x MAX y" -> "max(x,y)"
    "x MIN y" -> "min(x,y)"
    '''
    done = False
    while not done:
        match = re.search(r'( MAX | MIN )', string)
        if match:
            start_point = match.start()  # this is the index of the first space in " MAX "
            end_point = match.end()  # this is the index of the character after " MAX "
            left_block = None
            slice_index_left = None
            if string[start_point-1] == ")":
                slice_index_left = find_opposing_bracket(
                    string, start_point-1, "backward")
                left_block = string[slice_index_left:start_point]
            else:
                left_block_match = re.search(
                    r'(\w|\d|_|¬|\.)*$', string[:start_point])
                slice_index_left = left_block_match.start()
                left_block = left_block_match.group()
            right_block = None
            slice_index_right = None
            if string[end_point] == "(":
                slice_index_right = find_opposing_bracket(
                    string, end_point+1, "forward")
                right_block = string[end_point: slice_index_right+1]
            else:
                right_block_match = re.search(
                    r'(\w|\d|_|¬|\.)*', string[end_point:])
                slice_index_right = end_point+right_block_match.end()
                right_block = right_block_match.group()
            minormax = match.group().strip().lower()
            string = "{}( {}( {}, {}) ){}".format(
                string[0:slice_index_left], minormax, left_block, right_block, string[slice_index_right:])
        else:
            done = True
    return string

def get_operator_precedence(string):
    '''
    takes a string representing an operator and returns a value from 0 to 3 representing its precendence. 0 is lowest
    '''
    precedence = None
    if string in [">=", "<=", "==", ">", "<", "and", "or", "not", "!=", "MAX", "MIN"]:
        precedence = 0
    elif string in ["+", "-"]:
        precedence = 1
    elif string in ["/", "*", "%"]:
        precedence = 2
    elif string in ["**"]:
        precedence = 3
    else:
        raise Exception("not a valid operator")
    return precedence

precedences = {">=": 0, "<=": 0, "==": 0, ">": 0, "<": 0, "and": 0, "or": 0, "not": 0, "!=": 0, "MAX": 0, "MIN": 0,
               "+": 1, "-": 1,
               "/": 2, "*": 2, "%": 2,
               "**": 3
               }

def implement_PEMDAS(string):
    '''
    takes a HUMMOD expression in which there are no parentheses and places parentheses appropriately so that it complies with the PEMDAS order of operations

    loops through each operator, checks if the one after it has higher precedence. Creates parentheses if so.
    '''

    iterator = re.finditer(
        r' (>=|<=|==|\*\*|\+|-|/|\*|%|>|<|and|or|not|\!=|MAX|MIN) ', string)

    # finditer returns an iterator. Convert this to a list of the matches
    operator_matches = [match_obj for match_obj in iterator]

    extra_indices = 0
    for i, match in enumerate(operator_matches[:-1]):
        op = match.group().strip()
        nextop = operator_matches[i+1].group().strip()
        precedence_tracker = precedences[op]
        if precedences[nextop] > precedence_tracker:
            # need to put parentheses around everything so far
            new_para_point = operator_matches[i+1].start()+extra_indices
            string = "(" + string[0:new_para_point] + \
                ")" + string[new_para_point:]
            extra_indices += 2  # account for the change in string length because of new parentheses

    return string

def process_part(part):
    '''
    this is passed a partly processed expression in which there are no parentheses

    Because HumMod's expressions evaluate left to right, defying BODMAS/PEMDAS, we need to go left to right drawing parentheses around everything so that the order of operations is correct in python

    returns string in which parentheses have been placed correctly and MIN and MAX have been reformatted
    '''
    # Replace unary operators with special tags
    part = re.sub(r'INVERT ([^ ]+)', r'__INVERT__\g<1>', part)
    part = re.sub(r'EXP ([^ ]+)', r'__EXP__\g<1>', part)
    part = re.sub(r'LOG10 ([^ ]+)', r'__LOG10__\g<1>', part)
    part = re.sub(r'LOG ([^ ]+)', r'__LOG__\g<1>', part)
    part = re.sub(r'SINDEG ([^ ]+)', r'__SINDEG__\g<1>', part)
    part = re.sub(r'SQRT ([^ ]+)', r'__SQRT__\g<1>', part)

    # convert to PEMDAS order: P, E, MD, AS by using parentheses
    part = implement_PEMDAS(part)

    # now sub MAX and MIN
    part = process_minmax(part)

    #convert unary operator tags into python
    part = re.sub(r'__INVERT__(\S+)', r'( 1 / \g<1> )', part)
    part = re.sub(r'__EXP__(\S+)', r'( math.e ** \g<1> )', part)
    part = re.sub(r'__LOG10__(\S+)', r'( math.log10( \g<1> ) )', part)
    part = re.sub(r'__LOG__(\S+)', r'( math.log( \g<1> ) )', part)
    part = re.sub(r'__SINDEG__(\S+)', r'( math.sin ( math.radians ( \g<1> ) ) )', part)
    part = re.sub(r'__SQRT__(\S+)', r'( math.sqrt( \g<1> ) )', part)

    return part

def process_parentheses_tree(parentheses_tree):
    '''
    takes a parentheses tree created with create_parenthesis_tree,
    runs process_part on all of the layers then combines them
    '''
    processed_outer = process_part(parentheses_tree[0])

    if len(parentheses_tree[1]) > 0:
        processed_inners = []
        for subtree in parentheses_tree[1]:
            processed_inners.append(process_parentheses_tree(subtree))
        for i, processed_inner in enumerate(processed_inners):
            processed_outer = processed_outer.replace(
                '__{}__'.format(i), "("+processed_inner+")")
    return processed_outer

def create_parentheses_tree(string):
    '''
    takes a string and separates out blocks contained within parentheses eg.
    "123 - (abc + def) * (ghi / jkl)"
    => ["123 - __1__ + __2__", [
            ["abc + def", []],
            ["ghi / jkl", []]
        ]
    '''
    parentheses_tree = ['', []]
    replacement_index = 0
    while True:
        open_para_match = re.search(r'\(', string)
        if open_para_match:
            close_bracket_index = find_opposing_bracket(
                string, open_para_match.start())
            inner_tree = create_parentheses_tree(
                string[open_para_match.start()+1:close_bracket_index])
            string = string[:open_para_match.start(
            )] + "__{}__".format(replacement_index) + string[close_bracket_index+1:]
            replacement_index += 1
            parentheses_tree[1].append(inner_tree)
        else:
            break
    parentheses_tree[0] = string
    return parentheses_tree

def process_expression(string):
    '''
    takes a HUMMOD expression string and converts it to a python expression eg.

    eg.
        "FA+GlucoseFraction * ( Ratio / ( Ratio + KR ) ) MIN [O2]"
            =>
        "min((FA_GlucoseFraction * (Ratio / (Ratio + KR))), conc_O2)"

    The HumMod XML has its own mathematical expression syntax. This needs to be converted to python expression syntax
    One notable difference between the systems is that HUMMOD operations are evaluated left to right, not according to PEMDAS
    '''

    #get rid of excessive spaces
    string = re.sub(r' +', r' ', string)

    string = format_names(string)

    #easier to process if strings start and end with a space
    if string[0] != " ":
        string = " " + string
    if string[-1] != " ":
        string = string + " "

    #replace newlines
    string = string.replace("\n", " ")

    string = string.replace(" GT ", " > ")
    string = string.replace(" GE ", " >= ")
    string = string.replace(" LT ", " < ")
    string = string.replace(" LE ", " <= ")
    string = string.replace(" ^ ", " ** ")
    string = string.replace(" AND ", " and ")
    string = string.replace(" OR ", " or ")
    string = string.replace(" EQ ", " == ")
    string = string.replace(" NE ", " != ")
    string = string.replace(" REM ", " % ")
    string = string.replace(" PI ", " 3.14159265359 ")
    string = string.replace(" NOT ", " not ")
    string = string.replace(" TRUE ", " True ")
    string = string.replace(" FALSE ", " False ")
    string = string.replace(" INFINITE ", "float(\"inf\")")
    string = string.replace(" UNDEFINED ", "0") #HumMod treats undefined as zero
    string = string.replace(" UNKNOWN ", "None")
    string = string.replace(" BLANK ", "None")

    # sometimes a "-" operator is used to signal that a variable is being made negative. In these cases it is preceded by the start of the string or by "("
    string = re.sub(r'^ *- +([^ ]+) ', r' __NEG__\g<1> ', string)
    string = re.sub(r'\( *- +([^ ]+) ', r'( __NEG__\g<1> ', string)

    parentheses_tree = create_parentheses_tree(string)

    string = process_parentheses_tree(parentheses_tree)

    #now sub any remaining curves
    string = re.sub(r'(^| +)((?:\w|\.)+) \[ ((?:\w|\.)*) \]', r'\g<1>\g<2>_curve( \g<3> )', string)

    string = re.sub(r'__NEG__', r'- ', string)

    #remove spaces from start and end of string
    if string[0] == " ":
        string = string[1:]
    if string[-1] == " ":
        string = string[:-1]

    return string

def add_self_where_necessary(code):
    '''
    takes a string of code, adds .self to any variable from this class

    this is a hack. ideally it would have been done during parsing but it was an afterthought
    '''

    #pick out anything that has at least one letter or underscore in it:
    matches = re.finditer(r'(?:^| )((?:\w|\.)*[a-df-zA-DF-Z](?:\w|\.)*)', code) 

    var_likes = [[match.group(1), match.end()] for match in matches]

    #replace all those with placeholder
    new_code = re.sub(r'(^| )((?:\w|_|\.)*[a-df-zA-DF-Z](?:\w|_|\.)*)', r'\g<1>__VARLIKE__', code)

    #for every var-like string, see if it really does need a ".self" in from of it
    for i, var_like in enumerate(var_likes):
        string = var_like[0]
        endpoint = var_like[1]
        if (
            not ((len(code) > endpoint+2) and (code[endpoint:endpoint+2] in ["(s", "(x"])) and #this is a function name, so don't add "self."
            not ("." in string) and #it's referring to another object
            not (string in [
                "def",
                "None",
                "True",
                "False",
                "pass",
                "if",
                "else",
                "elif",
                "or",
                "not",
                "and",
                "return",
                "max",
                "min",
                "x",
                "Timer",
                "print"]) and #special words
            not re.match("impliciteq", string) and
            not re.match("diffeq", string) and
            not re.match("delay", string) and
            not re.match("cubic_hermite", string) and
            not re.match("stabledelay", string) and
            not re.match("backwardeuler", string) and
            not re.search("implicitfunc", string) and
            not re.match("set_timervar", string)
        ):
            var_likes[i] = ["self." + string, endpoint] #don't know why the strip() is necessary

    while re.search(r'__VARLIKE__', new_code):
        new_code = re.sub( r'__VARLIKE__', var_likes.pop(0)[0], new_code, 1)

    #implicit functions are more complex. Some .self needed but not on all variables

    implicitfunc_matches = re.finditer(r'implicitfunc\((\w+)\)(.|\n)*\n *return self\.(.*) *\n', new_code)
    for implicitfunc_match in implicitfunc_matches:
        implicitfunc_str = implicitfunc_match.group(0)
        mainvar = implicitfunc_match.group(1)
        retvar = implicitfunc_match.group(3)
        new_implicitfunc_str = re.sub(r'self\.{}( |\n)'.format(mainvar), mainvar+r'\g<1>', implicitfunc_str)
        new_implicitfunc_str = re.sub(r'self\.{}( |\n)'.format(retvar), retvar+r'\g<1>', new_implicitfunc_str)
        new_code = new_code.replace(implicitfunc_str, new_implicitfunc_str)

    return new_code

def check_for_var_ref(string, var):
    '''
    searches string of python code for variable of the given name, returns true or false
    '''
    if re.search(r'(^| |\(|self\.){} '.format(var), string):
        return True
    else:
        return False

def parse_block_subelements(subelements, memory):
    '''
    takes the subelements of a <block> element and returns the python code for everything inside <block>

    this separate function is necessary to manage <if> and <andif> element logic:

    there are eight possible situations in an <if> element:
    1. the true element has exitblock and there is no false element
        - everything after the <if> needs to go under the "else:", which otherwise would be empty
    2. the true element has exitblock and the false element has exitblock
        - everything in <block> after the <if> element should be ignored
    3. the true element has exitblock and the false element has no exitblock
        - everything after the <if> needs to go under the "else:", after the processed contents of <false>
    4. the true element has no exitblock and there is no false element
        - process contents of <true> and put under "if", no "else" needed
    5. the true element has no exitblock and the false element has exitblock
        everything in <block> after <if> needs to go under "if:", after the processed contents of <true>
    6. the true element has no exitblock and the false element has no exitblock
        - process contents of <true> and <false> and but under standard "if" and "else"
    7. there is no true element and the false element has exitblock
        - everything in <block> after <if> needs to go under "if:" which would otherwise be empty
    8. there is no true element and the false element has no exitblock
        - standard "if"/"else" where "if" has just "pass"
    9. there is neither true nor false elements
        - <if> block is pointless but set both "if:" and "else:" to "pass" anyway
    '''

    code = ''
    done = False
    i = 0
    while not done and i < len(subelements):
        subelement = subelements[i]
        if subelement[0] not in ["if", "andif"]:
            subcode, memory = parse_xml_element(subelement, memory)
            code += subcode
        else:  # we are dealing with an <if> or <andif> element
            memory["depth"] += 1 #"if" and "else" need to be indented
            # need to know if there is a true element and if so, if it contains an exitblock
            test_contents = process_expression(
                find_child_els_by_name(subelement, "test")[0][1])

            true_elems = find_child_els_by_name(subelement, "true")
            if len(true_elems) > 0:
                true_elem = true_elems[0]
            else:
                true_elem = False

            if true_elem:
                exitblock_idx = "undefined"
                for j, true_elem_child in enumerate(true_elem[2]):
                    if true_elem_child[0] == "exitblock/":
                        exitblock_idx = j
                        break
                if exitblock_idx != "undefined":
                    true_exitblock = True
                    # cut anything after <exitblock/>
                    true_elem[2] = true_elem[2][0:j]
                else:
                    true_exitblock = False
            
            # need to know if there is a false element and if so, if it contains an exitblock
            false_elems = find_child_els_by_name(subelement, "false")
            if len(false_elems) > 0:
                false_elem = false_elems[0]
            else:
                false_elem = False
            if false_elem:
                exitblock_idx = "undefined"
                for j, false_elem_child in enumerate(false_elem[2]):
                    if false_elem_child[0] == "exitblock/":
                        exitblock_idx = j
                        break
                if exitblock_idx != "undefined":
                    false_exitblock = True
                    # cut anything after <exitblock/>
                    false_elem[2] = false_elem[2][0:j]
                else:
                    false_exitblock = False

            # 1 the true element has exitblock and there is no false element
            if true_elem and true_exitblock and not false_elem:
                true_contents, memory = parse_xml_element(true_elem, memory)
                false_contents, memory = parse_block_subelements(
                    subelements[i+1:], memory)
                done = True

            # 2 the true element has exitblock and the false element has exitblock
            #NOTE: this situation does not seem to appear in HUMMOD
            elif true_elem and true_exitblock and false_elem and false_exitblock:
                true_contents, memory = parse_xml_element(true_elem, memory)
                false_contents, memory = parse_xml_element(false_elem, memory)
                done = True

            # 3 the true element has exitblock and the false element has no exitblock
            #NOTE: this situation does not seem to appear in HUMMOD
            elif true_elem and true_exitblock and false_elem and not false_exitblock:
                true_contents, memory = parse_xml_element(true_elem, memory)
                false_contents, memory = parse_xml_element(false_elem, memory)
                additional_false_contents, memory = parse_block_subelements(
                    subelements[i+1:], memory)
                false_contents += additional_false_contents
                done = True

            # 4 the true element has no exitblock and there is no false element
            elif true_elem and not true_exitblock and not false_elem:
                true_contents, memory = parse_xml_element(true_elem, memory)
                false_contents = "{}    pass\n".format("    "*memory["depth"])

            # 5 the true element has no exitblock and the false element has exitblock
            #NOTE: this situation does not seem to appear in HUMMOD
            elif true_elem and not true_exitblock and false_elem and false_exitblock:
                # everything in <block> after <if> needs to go under "if:", after the processed contents of <true>
                true_contents = parse_xml_element(true_elem, memory)
                additional_true_contents, memory = parse_block_subelements(
                    subelements[i+1:], memory)
                true_contents += additional_true_contents
                false_contents, memory = parse_xml_element(false_elem, memory)
                done = True

            # 6 the true element has no exitblock and the false element has no exitblock
            elif true_elem and not true_exitblock and false_elem and not false_exitblock:
                true_contents, memory = parse_xml_element(true_elem, memory)
                false_contents, memory = parse_xml_element(false_elem, memory)

            # 7 there is no true element and the false element has exitblock
            elif not true_elem and false_elem and false_exitblock:
                true_contents, memory = parse_block_subelements(
                    subelements[i+1:], memory)
                false_contents, memory = parse_xml_element(false_elem, memory)
                done = True

            # 8 there is no true element and the false element has no exitblock
            #NOTE: this situation does not seem to appear in HUMMOD
            elif not true_elem and false_elem and not false_exitblock:
                true_contents = "{}    pass\n".format("    "*memory["depth"])
                false_contents, memory = parse_xml_element(false_elem, memory)

            # 9 there is neither true nor false elements
            #NOTE: this situation does not seem to appear in HUMMOD
            elif (not true_elem) and (not false_elem):
                true_contents = "{}    pass\n".format("    "*memory["depth"])
                false_contents = "{}    pass\n".format("    "*memory["depth"])

            # check that the true and false contents aren't empty (eg. if they just contained <exitblock/>)
            if true_contents.strip() == "":
                true_contents = "{}    pass\n".format("    "*memory["depth"])
            if false_contents.strip() == "":
                false_contents = "{}    pass\n".format("    "*memory["depth"])

            code += '{0}if {1}:\n{2}{0}else:\n{3}'.format(
                "    "*memory["depth"], test_contents, true_contents, false_contents)

            memory["depth"]-=1

        i += 1

    return code, memory

def parse_xml_element(element, memory={}):
    '''
    takes an item from the xml tree and a memroy dict and converts the xml and everything sub to it to python code

    element represents an XML element. It is of the form:
        ["name", "blah content blah", [
            <child element 1>,
            <child element 2>]
        ]

    memory is a dictionary of data that is passed up and down the XML tree as we process everything, allowing us to refer to information from earlier in the file
    it is of the form:
        {"equations": {
            "equation name": "equation data as string",
            },
        "imports": [
                "import blah.blah",
                "import foo.bar"
            ],
        }
        "curves": {
            "curve name": [[xarrays],[yarras],[slopes]]
        }


    return:
        code (string): the python equivalent of the input XML element
        memory: a memory dict, as above
    '''
    code = ''

    memory["depth"] += 1

    depth = memory["depth"]

    depth_correct = -1

    name = element[0]
    content = element[1]
    children = element[2]

    # root elements
    if name == "root":
        memory["depth"] -= 1

    elif name == "model":
        memory["depth"] -= 1

    elif name == "structure":
        memory["depth"] -= 1

    # second-level elements:
    elif name == "variables":
        # can ignore <var> because they just declare a variable without setting a value
        memory["depth"] -= 1
        depth_correct += 1

    elif name == "definitions":
        memory["depth"] -= 1
        depth_correct += 1

    elif name == "equations":
        pass
        # see "curve"

    elif name == "functions":
        pass
        # see "curve"

    elif name == "curve":
        name = find_child_els_by_name(element, "name")[-1][1]
        name = format_names(name)
        xs = []
        ys = []
        slopes = []
        for point in find_child_els_by_name(element, "point"):
            xs.append(float(find_child_els_by_name(point, "x")[-1][1]))
            ys.append(float(find_child_els_by_name(point, "y")[-1][1]))
            slopes.append(float(find_child_els_by_name(point, "slope")[-1][1]))

        code += "\n    def {0}_curve(self, x):\n        return cubic_hermite_spline(x, {1}, {2}, {3})\n".format(name ,xs, ys, slopes)
        
        #memory["special_func_imports"]["from special_functions import cubic_hermite_spline\n"] = True
        #memory["curves"][name] = points
        children = []  # erase children as they have been processed

    elif name == "parm":
        name = find_child_els_by_name(element, "name")[-1][1]
        if name.strip() != "":  # sometimes the name is not defined (eg. LH_.DES)
            name = format_names(name)
            memory["all_vars"].append(memory["filename"]+"."+name)
            memory["parms"].append(memory["filename"]+"."+name)
            val_els = find_child_els_by_name(element, "val")
            if len(val_els) > 0:
                val = val_els[-1][1]
                val = process_expression(val)
            else:
                val = "None"
            code += "    "*depth+"self.{} = {}\n".format(name, val)
            children = []

    elif name == "var":
        name = find_child_els_by_name(element, "name")[-1][1]
        if name.strip() != "":  # sometimes the name is not defined (eg. LH_.DES)
            name = format_names(name)
            memory["all_vars"].append(memory["filename"]+"."+name)
            val_els = find_child_els_by_name(element, "val")
            if len(val_els) > 0:
                val = val_els[-1][1]
                val = process_expression(val)
            else:
                val = "None"
            code += "    "*depth+"self.{} = {}\n".format(name, val)
            children = []

    elif name == "constant":
        name = find_child_els_by_name(element, "name")[-1][1]
        name = format_names(name)
        memory["all_vars"].append(memory["filename"]+"."+name)
        val_els = find_child_els_by_name(element, "val")
        if len(val_els) > 0:
            val = val_els[-1][1]
            val = process_expression(val)
        else:
            val = "None"
        code += "    "*depth+"self.{} = {}\n".format(name, val)
        children = []  # erase children as they are already processed

    elif name == "def":
        # in [EPO]Delay.DES, SteadyState is used as both the name of a variable and the name of a curve, though it is not meant to overwrite itself
        # in order to manage this, in any expression we check to see if it is referring to itself. if it is, check to see if there is a curve with that name
        name = find_child_els_by_name(element, "name")[-1][1]
        if name.strip() != "":  # sometimes name and val are empty (eg. LH_.DES)
            name = format_names(name)
            val = find_child_els_by_name(element, "val")[-1][1]
            val = process_expression(val)

            if val.strip() == memory["filename"].upper(): #for some reason sometimes val is just the filename capitalised, perhaps meant to be a string. These don't ever seem to be used for anything.
                val = "\"{}\"".format(val.strip())
            if "." in name: #occasionally the var name contains a dot, which is annoying
                code += "    "*depth+"{} = {}\n".format(name, val)
            else:
                code += "    "*depth+"self.{} = {}\n".format(name, val)
        children = []  # erase children as they are already processed

    # everything else
    elif name == "impliciteq":
        '''
        need to convert the block into a function that can then be fed into implicit eq

        The path from startval to endval (the function f) is defined in:
            <implicitmath>
        '''
        startname = format_names(
            find_child_els_by_name(element, "startname")[-1][1])
        yend = format_names(find_child_els_by_name(element, "endname")[-1][1])
        error_limit = format_names(
            find_child_els_by_name(element, "errorlim")[-1][1])

        initial_vals = find_child_els_by_name(element, "initialval")
        if len(initial_vals) > 0:
            initial_val = process_expression(initial_vals[-1][1])
            code += "    self.{} = {}".format(startname, initial_val)

        impliciteq_code = "self.{0} = impliciteq( {0}implicitfunc, {0}, {1})".format(
            startname, error_limit)
        memory["special_func_imports"]["from special_functions import impliciteq\n"] = True
        memory["equations"]["impliciteq"][startname] = {
            "code": impliciteq_code, "yend": yend}
        children = []

    elif name == "implicitmath":
        # recall the "implicit equation" from memory
        name = format_names(find_child_els_by_name(element, "name")[-1][1])
        implicitfunc, memory = parse_xml_subelements(element[2], memory)
        code += "\n{0}def {1}implicitfunc({1}):\n{2}\n{0}    return {3}\n".format(
            "    "*depth, name, implicitfunc, memory["equations"]["impliciteq"][name]["yend"])
        impliciteq_code = memory["equations"]["impliciteq"][name]["code"]
        code += "    "*depth + impliciteq_code + "\n"
        children = []

    elif name == "copy":
        from_var = format_names(find_child_els_by_name(element, "from")[-1][1])
        to_var = format_names(find_child_els_by_name(element, "to")[-1][1])
        if "." in to_var: #don't add ".self" if the name contains a dot
            code += "{}{} = {}\n".format("    "*depth, to_var, from_var)
        else:
            code += "{}self.{} = {}\n".format("    "*depth, to_var, from_var)   
        children = []

    elif name == "block":
        '''
        Processing a block complicated by the <if> logic. We use a dedicated function parse_block_subelements
        '''
        name = format_names(find_child_els_by_name(element, "name")[-1][1])

        code += "\n{}def {}_func(self):\n".format("    "*depth, name)

        subcode, memory = parse_block_subelements(children, memory)

        if subcode.strip() == "":
            # some files are blank, for some reason
            subcode = "    {}pass\n".format("    "*memory["depth"])

        code += subcode

        # now add in the differential and delay equation at the end of the block if relevant
        if len(memory["equations"]["diffeq"]) > 0:
            for key in memory["equations"]["diffeq"].keys():
                if check_for_var_ref(subcode, key):
                    code += "{}    {}\n".format("    "*memory["depth"], memory["equations"]["diffeq"][key]["code"])

        if len(memory["equations"]["delay"]) > 0:
            # check if there is a variable with name matching the input, if so, add delay code to the end of the block
            
            #######
            #NOTE: HACK workaround:
            #in SkeletalMuscle_MetabolicVasodilation the delay function is called before K is defined, this is the only place this happens. We just manually move the delay function to after K is defined
            if memory["filename"] == "SkeletalMuscle-MetabolicVasodilation":
                if name == "Dervs":
                    code += "{}    {}\n".format("    "*memory["depth"], memory["equations"]["delay"]["SteadyState"]["code"])
                    print("^^^^^")
            #######

            else:
                for key in memory["equations"]["delay"].keys():
                    if check_for_var_ref(subcode, key):
                        code += "{}    {}\n".format("    "*memory["depth"], memory["equations"]["delay"][key]["code"])

        if len(memory["equations"]["backwardeuler"]) > 0:
            # check if there is a variables F1 or F2, if so, add the backwardeuler code
            for key in memory["equations"]["backwardeuler"].keys():
                if check_for_var_ref(subcode, "F1") or check_for_var_ref(subcode, "F2"):
                    code += "{}    {}\n".format("    "*memory["depth"], memory["equations"]["backwardeuler"][key]["code"])

        if len(memory["equations"]["stabledelay"]) > 0:
            # check if there is a variable with name matching the input, if so, add stabledelay code to the end of the block
            for key in memory["equations"]["stabledelay"].keys():
                if check_for_var_ref(subcode, key):
                    code += "{}    {}\n".format("    "*memory["depth"], memory["equations"]["stabledelay"][key]["code"])

        children = []  # erase children as they have already been processed

    elif name in ["delay", "stabledelay"]:
        outputname = format_names(
            find_child_els_by_name(element, "outputname")[-1][1])
        initialval = format_names(
            find_child_els_by_name(element, "initialval")[-1][1])
        inputname = format_names(
            find_child_els_by_name(element, "inputname")[-1][1])
        k = format_names(find_child_els_by_name(
            element, "rateconstname")[-1][1])
        
        # check errorlim
        errorlimels = (find_child_els_by_name(element, "errorlim"))
        if len(errorlimels) > 0:
            errorlim = float(errorlimels[-1][1])
        else:
            errorlim = None

        # if there is an initialval defined, declare it at the top of the document
        code += "{}self.{} = {}\n".format("    "*(depth-1), outputname, initialval)
        delay_code = "self.{0} = delay( {1}, {2}, {0}, System.Dx, {3})\n".format(outputname, k, inputname, errorlim)
        memory["special_func_imports"]["from special_functions import delay\n"] = True
        
        if name == "delay":
            memory["equations"]["delay"][inputname] = {
                "code": delay_code,
                "output name": outputname,
                "k": k,
                "inputname":inputname,
                "errorlim": errorlim}
        else:
            memory["equations"]["stabledelay"][inputname] = {
                "code": delay_code,
                "output name": outputname,
                "k": k,
                "inputname":inputname,
                "errorlim": errorlim}
        children = []

    elif name == "backwardeuler":
        integralname = format_names(
            find_child_els_by_name(element, "integralname")[-1][1])
        
        outp_name = format_names(
            find_child_els_by_name(element, "name")[-1][1])

        # if there is an initialval, set integralname = initalval at the start of the document
        initialvalels = find_child_els_by_name(element, "initialval")
        if len(initialvalels) > 0:
            initialval = format_names(initialvalels[-1][1])
            code += "{}self.{} = {}\n".format("    " *
                                         (depth-1), integralname, initialval)

        f1name = format_names(find_child_els_by_name(element, "f1name")[-1][1])
        f2name = format_names(find_child_els_by_name(element, "f2name")[-1][1])

        # check errorlim
        errorlimels = (find_child_els_by_name(element, "errorlim"))
        if len(errorlimels) > 0:
            errorlim = float(errorlimels[-1][1])
        else:
            errorlim = None

        beuler_code = "self.{0} = backwardeuler( {1}, {2}, System.Dx, {0}, {3})\n".format(integralname, f1name, f2name, errorlim)
        memory["special_func_imports"]["from special_functions import backwardeuler\n"] = True
        memory["equations"]["backwardeuler"][integralname] = {
            "code": beuler_code,
            "output name": outp_name,
            "f1": f1name,
            "f2": f2name,
            "errorlim": errorlim}
        children = []
        # TODO the backward euler integral needs to update whenever its components update. Need to know where f1 and f2 are defined.
        # need to find where f1 and f2 are defined then place the code after this ??

    elif name in ["diffeq", "stablediffeq"]:
        integralname = format_names(
            find_child_els_by_name(element, "integralname")[-1][1])
        
        dervname = format_names(
            find_child_els_by_name(element, "dervname")[-1][1])

        outp_name = format_names(
            find_child_els_by_name(element, "name")[-1][1])

        # get errorlim
        errorlimels = (find_child_els_by_name(element, "errorlim"))
        if len(errorlimels) > 0:
            errorlim = float(errorlimels[-1][1])
        else:
            errorlim = None

        # if there is an initialval, set integralname = initalval at the start of the document
        initialvalels = find_child_els_by_name(element, "initialval")
        if len(initialvalels) > 0:
            initialval = format_names(initialvalels[-1][1])
            code += "{}self.{} = {}\n".format("    " *
                                         (depth-1), integralname, initialval)
        diffeq_code = "self.{0} = diffeq( {1}, System.Dx, {0}, {2})\n".format(integralname, dervname, errorlim)
        memory["special_func_imports"]["from special_functions import diffeq\n"] = True
        if name == "diffeq":
            memory["equations"]["diffeq"][dervname] = {
                "code": diffeq_code,
                "output name": outp_name,
                "dervname": dervname,
                "errorlim": errorlim}
        else:
            memory["equations"]["stablediffeq"][dervname] = {
                "code": diffeq_code,
                "output name": outp_name,
                "dervname": dervname,
                "errorlim": errorlim}
        children = []

    elif name == "call":
        # <call> calls a function
        func_name = format_names(content)
        code += "    "*depth + func_name + "_func()\n"

    elif name == "onjustchanged":
        # treat everything sub to this as a block
        # erase children as they have already been processed
        memory["depth"] -= 1
        depth_correct += 1
        subcode, memory = parse_block_subelements(children, memory)

        if subcode.strip() == "":
            subcode = "    {}pass\n".format("    "*memory["depth"])
        
        code += subcode

        children = [] #already processed

    elif name == "conditional":
        name = find_child_els_by_name(element, "name")[-1][1]
        name = format_names(name)
        test = process_expression(find_child_els_by_name(element, "test")[-1][1])
        true = process_expression(
            find_child_els_by_name(element, "true")[-1][1])
        # sometimes there is no "if false" clause
        false_children = find_child_els_by_name(element, "false")
        if len(false_children) > 0:
            false = process_expression(false_children[-1][1])
            false_string = "{0} = {1}\n".format(name, false)
        else:
            false_string ="pass"
        code += "{0}if {2}:\n{0}    {1} = {3}\n{0}else:\n{0}    {4}\n".format("    "*depth, name, test, true, false_string)
        children = []  # erase children as they have already been processed

    elif name == "andif":
        '''
        this is only ever invokes within <if> elements
        '''

        # treat everything sub to this as a block
        # erase children as they have already been processed
        memory["depth"] -= 1
        depth_correct += 1
        subcode, memory = parse_block_subelements([element], memory)

        if subcode.strip() == "":
            subcode = "    {}pass\n".format("    "*memory["depth"])
        
        code += subcode

        children = [] #already processed


    elif name[0] == "?":
        # <?path ...> is ignored
        # <?include ...> indicates a required module import
        if "?include" in name[0:]:
            import_target = format_names(content)
            memory["imports"]["import " + import_target + "\n"] = True

    elif name == "gofor":
        pass  # not sure what this is

    elif name == "testcase":
        # this is a series of if/elif tests
        cases = find_child_els_by_name(element, "case")
        for i, case in enumerate(cases):
            if i == 0:
                code += "    "*depth+"if "
            else:
                code += "    "*depth+"elif "
            test_expression = find_child_els_by_name(case, "test")[-1][1]
            test_expression = process_expression(test_expression)
            # assumes that <test> is the first element in <case>. Is this true?
            rest_of_case = case[2][1:]
            defcode, memory = parse_xml_subelements(rest_of_case, memory)
            if defcode.strip() == "":
                defcode = "{}    pass\n".format("    "*memory["depth"])
            code += test_expression + ":\n" + defcode
        children = []  # erase children as they have already been processed

    elif name ==  "timervar":
        name = format_names(find_child_els_by_name(element, "name")[-1][1])
        val_els = find_child_els_by_name(element, "val")
        val = 0
        if len(val_els) > 0:
            val = process_expression(val_els[-1][1])
        state_els = find_child_els_by_name(element, "state")
        state = None
        if len(state_els) > 0:
            state = state_els[-1][1]
        code += "{0}self.{1} = Timer({2}, \"{3}\", System.Dx)\n".format("    "*depth, name, val, state)
        code += "{}timervars.append(self.{})\n".format("    "*depth, name)
        children = []

    elif name == "timer":
        name = format_names(find_child_els_by_name(element, "name")[-1][1])
        val_els = find_child_els_by_name(element, "val")
        if len(val_els) > 0:
            val = process_expression(val_els[-1][1])
            code += "{0}self.{1}.val = {2}\n".format("    "*depth, name, val)
        state_els = find_child_els_by_name(element, "state")
        if len(state_els) > 0:
            state = state_els[-1][1]
            code += "{0}self.{1}.state = \"{2}\"\n".format("    "*depth, name, state)

        children = []  # already processed

    elif name == "ontimedout":
        # these are defined in blocks
        # when the block is called, it's saying to wait until the timer is a certain value, then do what's in the block
        # what we do is we attach that block function to the timevar in the timevar dictionary, so that it knows what to do when the timer hits 0
        name = format_names(find_child_els_by_name(element, "name")[-1][1])
        # all <ontimedout> els have a single <call> after <name>
        called_func = format_names(
            find_child_els_by_name(element, "call")[-1][1])
        code += "{0}if self.{1} == 0:\n{0}    {2}_func()\n".format(
            "    "*depth, name, called_func)
        children = []

    elif name in ["message", "page", "name"]:
        # all useless
        pass

    elif name in ["true", "false"]:
        #need to decrease depth
        memory["depth"] -=1
        depth_correct +=1
        pass

    else:
        print("unknown element:", name)

    if len(children) > 0:
        subcode, memory = parse_xml_subelements(children, memory)
        code += subcode

    memory["depth"] += depth_correct

    return code, memory

def convert_DES_to_py(path, filename):
    xml_tree = create_xml_tree(path, filename)
    parse_xml_element(xml_tree[0])

all_vars = []

parms = []

def convert_directory(root_dir, source_dirs, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    with open(destination_dir+"hummod_converted.py", 'w') as f:
        f.write("from .special_functions import *\n")
        f.write("import math\n")
        f.write("\ntimervars = []\n")
        f.write("""\nclass System:
    def __init__(self):
        self.InitialX = 0
        self.X = 0
        self.Dx = 0.0003

class Timer:
    def __init__(self, val, state, Dx):
        self.val = val
        self.state = state
        self.Dx = Dx
    
    def count(self):
        if self.state == "OFF":
            pass
        elif self.state == "UP":
            self.val += self.Dx
        elif self.state == "DOWN":
            self.val -= self.Dx
    
    def __lt__(self, other):
        return self.val<other
    
    def __gt__(self, other):
        return self.val>other\n\n""")
        class_instantiations = []
        all_ODE_outputs = []
        for source_dir in source_dirs:
            for subdir, _dirs, files in os.walk(root_dir+source_dir):
                for file in files:
                    if file[-4:] == ".DES":
                        xml_tree = create_xml_tree(subdir, file)
                        memory = {"equations": {"delay": {}, "impliciteq": {}, "diffeq": {
                        }, "backwardeuler": {}, "stabledelay": {}, "stablediffeq":{}}, "imports": {}, "special_func_imports": {}, "depth": 0, "curves": {}, "filename": file[:-4], "all_vars": [], "parms":[]}
                        new_file_contents, memory = parse_xml_element(xml_tree, memory)
                        # python_code = convert_DES_to_py(subdir, file)

                        class_name = format_names(" "+file[:-4]+" ")

                        #sometimes the .DES file has no useful contents, for some reason
                        if new_file_contents.strip() == "":
                            new_file_contents = "    pass\n"

                        #need to add .self to the start of any local variable definition or reference
                        new_file_contents = add_self_where_necessary(new_file_contents)

                        #indent everything up to the first def and put it inside a constructor
                        first_def = re.search('\n\s*?def ', new_file_contents)
                        if first_def:
                            constructor_contents = new_file_contents[:first_def.start()]
                            post_constructor_code = new_file_contents[first_def.start():]
                        else:
                            constructor_contents = new_file_contents
                            post_constructor_code = ""
                        constructor_code = re.sub("\n", "\n    ", constructor_contents)
                        if not constructor_code.strip() == "":
                            new_file_contents = "    def __init__(self):\n    "+ constructor_code + post_constructor_code

                        new_file_contents = "class {}:\n{}\n".format(class_name, new_file_contents)

                        if "{0} = {0}()\n".format(class_name) not in class_instantiations:
                            class_instantiations.append("{0} = {0}()\n".format(class_name))
                        
                        #create a list of all ODEs, for optimising timesteps
                        for diffeq_outp in memory['equations']['diffeq'].values():
                            all_ODE_outputs.append({"type": "diffeq",
                                "classname": class_name,
                                "outputname": diffeq_outp["output name"],
                                "dervname": diffeq_outp["dervname"],
                                "errorlim": diffeq_outp["errorlim"]})
                        for backwardeuler_outp in memory['equations']['backwardeuler'].values():
                            all_ODE_outputs.append({"type": "backwardeuler",
                                "classname": class_name,
                                "outputname": backwardeuler_outp["output name"],
                                "f1": backwardeuler_outp["f1"],
                                "f2": backwardeuler_outp["f2"],
                                "errorlim": backwardeuler_outp["errorlim"]})
                        for stablediffeq_outp in memory['equations']['stablediffeq'].values():
                            all_ODE_outputs.append({"type":"stablediffeq",
                                "classname": class_name,
                                "outputname": stablediffeq_outp["output name"],
                                "dervname": stablediffeq_outp["dervname"],
                                "errorlim": stablediffeq_outp["errorlim"]})
                        for delay_outp in memory['equations']['delay'].values():
                            all_ODE_outputs.append({"type":"delay",
                                "classname": class_name,
                                "outputname": delay_outp["output name"],
                                "k": delay_outp["k"],
                                "inputname": delay_outp["inputname"],
                                "errorlim": delay_outp["errorlim"]})
                        for stabledelay_outp in memory['equations']['stabledelay'].values():
                            all_ODE_outputs.append({"type": "stabledelay",
                                "classname": class_name,
                                "outputname": stabledelay_outp["output name"],
                                "k": stabledelay_outp["k"],
                                "inputname": stabledelay_outp["inputname"],
                                "errorlim": stabledelay_outp["errorlim"]})

                        #NOTE: afterthought hack - this should have been done earlier:
                        new_file_contents = new_file_contents.replace('" self.UP "', '"UP"')
                        new_file_contents = new_file_contents.replace('" self.DOWN "', '"DOWN"')
                        new_file_contents = new_file_contents.replace('" self.OFF "', '"OFF"')

                        print("class " + class_name + " is: =======\n" + new_file_contents + "=========\n")

                        f.write(new_file_contents)

                        for var in memory["all_vars"]:
                            all_vars.append(var)
                        for parm in memory["parms"]:
                            parms.append(parm)

        f.write("\n")

        f.write("System = System()\n")

        for line in class_instantiations:
            f.write(line)

        f.write("""
components = #fill in

all_ODEs = {}
""".format(all_ODE_outputs))

        f.write("""def step_with_timestep(timestep):
    System.Dx = timestep
    Structure.Dervs_func()
    Structure.Wrapup_func()
""")
    
#source_dir = '/path/to/hummod-respository/'
source_dir = '/Users/henryhoward/Downloads/hummod-standalone/'
destination_dir = './src/'

convert_directory(source_dir, ['Structure', 'Context'], destination_dir)

# #copy special_functions.py into the destination folder
# with open("special_functions.py", "r") as func_f1:
#     contents = func_f1.read()
#     with open(destination_dir+"special_functions.py", "w") as func_f2:
#         func_f2.write(contents)

"""
TODO:

Include MaxDx for stablediffeq and stabledelay
whitenoise in phaeochromocytoma
fix ROUND
"""