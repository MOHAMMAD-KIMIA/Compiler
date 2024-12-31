
ALPHABET = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
# GO (while statement)
def dfaGO(input_text):
    
    state = 'X'
    gotokens = []
    goerrors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'G':
                    state = 'Y'
                elif ch in ALPHABET - {'G'}:
                    goerrors.append()
                    state = 'Z'  
            
            case 'Y':
                if ch == 'O':
                    state = 'W'
                elif ch in ALPHABET - {'O'}:
                    goerrors.append()
                    state = 'Z'

            case 'W':
                if ch in ALPHABET:
                    goerrors.append()
                    state = 'Z'

            case _: 
                goerrors.append()
                break

    if state == 'W':
        gotokens.append("<GO_TK>")
    else:
        goerrors.append()

    return gotokens, goerrors
# GOCON (for statement)
def dfaGOCON(input_text):

    state = 'X'
    gocontokens = []
    goconerrors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'G':
                    state = 'Y'
                elif ch in ALPHABET - {'G'}:
                    goconerrors.append()
                    state = 'Z' 
            
            case 'Y':
                if ch == 'O':
                    state = 'W'
                elif ch in ALPHABET - {'O'}:
                    goconerrors.append()
                    state = 'Z'

            case 'W':
                if ch == 'C':
                    state = 'V'
                elif ch in ALPHABET - {'C'}:
                    goconerrors.append()
                    state = 'Z'
            
            case 'V':
                if ch == 'O':
                    state = 'Q'
                elif ch in ALPHABET - {'O'}:
                    goconerrors.append()
                    state = 'Z'

            case 'Q':
                if ch == 'N':
                    state = 'B'
                elif ch in ALPHABET - {'N'}:
                    goconerrors.append()
                    state = 'Z'

            case 'B':
                if ch in ALPHABET:
                    goconerrors.append()
                    state = 'Z'

            case _:  
                goconerrors.append()
                break

    if state == 'B':
        gocontokens.append("<GOCON_TK>")
    else:
        goconerrors.append()

    return gocontokens, goconerrors
# CON (if statement)
def dfaCON(input_text):

    state = 'X'
    contokens = []
    conerrors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'C':
                    state = 'Y'
                elif ch in ALPHABET - {'C'}:
                    conerrors.append()
                    state = 'Z'  
            
            case 'Y':
                if ch == 'O':
                    state = 'W'
                elif ch in ALPHABET - {'O'}:
                    conerrors.append()
                    state = 'Z'
                    
            case 'W':
                if ch == 'N':
                    state = 'V'
                elif ch in ALPHABET - {'N'}:
                    conerrors.append()
                    state = 'Z'
            
            case 'V':
                if ch in ALPHABET:
                    conerrors.append()
                    state = 'Z'
            
            case _:  
                conerrors.append()
                break


    if state == 'V':
        contokens.append("<CON_TK>")
    else:
        conerrors.append()

    return contokens, conerrors
# NOTOK (else statement)
def dfaNOTOK(input_text):

    state = 'X'
    notokens = []
    noterrors = []
    position = 0
    
    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'N':
                    state = 'Y'
                elif ch in ALPHABET - {'N'}:
                    noterrors.append()
                    state = 'Z'
            
            case 'Y':
                if ch == 'O':
                    state = 'W'
                elif ch in ALPHABET - {'O'}:
                    noterrors.append()
                    state = 'Z'
            
            case 'W':
                if ch == 'T':
                    state = 'V'
                elif ch in ALPHABET - {'T'}:
                    noterrors.append()
                    state = 'Z'
            
            case 'V':
                if ch == 'O':
                    state = 'Q'
                elif ch in ALPHABET - {'O'}:
                    noterrors.append()
                    state = 'Z'
            
            case 'Q':
                if ch == 'K':
                    state = 'B'
                elif ch in ALPHABET - {'K'}:
                    noterrors.append()
                    state = 'Z'
            
            case 'B':
                if ch in ALPHABET:
                    noterrors.append()
                    state = 'Z'

            case _: 
                noterrors.append()
                break
    
    if state == 'B':
        notokens.append("<NOTOK_TK>")
    else:
        noterrors.append()
    
    return notokens, noterrors
# SUB (Create function)
def dfaSUB(input_text):
    
    state = 'X'
    subtokens = []
    suberrors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'S':
                    state = 'Y'
                elif ch in ALPHABET - {'S'}:
                    suberrors.append()
                    state = 'Z'  
            
            case 'Y':
                if ch == 'U':
                    state = 'W'
                elif ch in ALPHABET - {'U'}:
                    suberrors.append()
                    state = 'Z'
                    
            case 'W':
                if ch == 'B':
                    state = 'V'
                elif ch in ALPHABET - {'B'}:
                    suberrors.append()
                    state = 'Z'
            
            case 'V':
                if ch in ALPHABET:
                    suberrors.append()
                    state = 'Z'
            
            case _: 
                suberrors.append()
                break


    if state == 'V':
        subtokens.append("<SUB_TK>")
    else:
        suberrors.append()

    return subtokens, suberrors
#SAYSUBTO (Use function)
def dfaSAYSUBTO(input_text):

    state = 'X'
    saysubtotokens = []
    saysubtoerrors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'S':
                    state = 'F'
                elif ch in ALPHABET - {'S'}:
                    saysubtoerrors.append()
                    state = 'Z'  
            
            case 'F':
                if ch == 'A':
                    state = 'W'
                elif ch in ALPHABET - {'A'}:
                    saysubtoerrors.append()
                    state = 'Z'
            
            case 'W':
                if ch == 'Y':
                    state = 'V'
                elif ch in ALPHABET - {'Y'}:
                    saysubtoerrors.append()
                    state = 'Z'
            
            case 'V':
                if ch == 'S':
                    state = 'Q'
                elif ch in ALPHABET - {'T'}:
                    saysubtoerrors.append()
                    state = 'Z'

            case 'Q':
                if ch == 'U':
                    state = 'E'
                elif ch in ALPHABET - {'A'}:
                    saysubtoerrors.append()
                    state = 'Z'
            
            case 'E':
                if ch == 'B':
                    state = 'D'
                elif ch in ALPHABET - {'B'}:
                    saysubtoerrors.append()
                    state = 'Z'

            case 'D':
                if ch == 'T':
                    state = 'H'
                elif ch in ALPHABET - {'T'}:
                    saysubtoerrors.append()
                    state = 'Z'

            case 'H':
                if ch == 'O':
                    state = 'K'
                elif ch in ALPHABET - {'O'}:
                    saysubtoerrors.append()
                    state = 'Z'
            
            case 'K':
                if ch in ALPHABET:
                    saysubtoerrors.append()
                    state = 'Z'

            case _:  
                saysubtoerrors.append()
                break

    if state == 'K':
        saysubtotokens.append("<SAYSUBTO_TK>")
    else:
        saysubtoerrors.append()

    return saysubtotokens, saysubtoerrors
# Identiffier
def dfaIdentifier(input_text, identifier_index, identifier_dict):

    state = 'A'
    idtokens = []
    iderrors = []

    if input_text in identifier_dict:
        idtokens.append(identifier_dict[input_text])
        return idtokens, iderrors, identifier_index
    
    state = 'A'  
    is_identifier = True 

    for i, ch in enumerate(input_text):
        if state == 'A':
            if ch == '-':
                state = 'B'
            else:
                iderrors.append()
                is_identifier = False
                break

        elif state == 'B':
            if ch in ALPHABET:
                state = 'D'
            else:
                iderrors.append()
                is_identifier = False
                break

        elif state == 'D':
            if ch in ALPHABET:
                state = 'D'  
            elif ch == '-':
                state = 'E'
            else:
                iderrors.append()
                is_identifier = False
                break


    if state == 'E' and is_identifier:
        idtokens.append(f"<id,{identifier_index}>")
        identifier_dict[input_text] = idtokens
        identifier_index += 1  
    elif is_identifier:
        iderrors.append()

    return idtokens, iderrors, identifier_index

# Arithmetic Operators (from line 390 to line 695)
# = 
def dfaEquals(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '=':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<=>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# *
def dfaAnd(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '∧':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<×>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# +
def dfaOr(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '∨':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<+>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# -
def dfaMinus(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '-':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<->")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# /
def dfaDivide(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '∺':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<÷>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# !=
def dfaNotEqual(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '≠':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<≠>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# == 
def dfaAssignment(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '∈':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'B':
        tokens.append("<Assi>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# <
def dfaLessthan(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '<':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<<>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors
# >
def dfaGreater(input_text):
    state = 'A'
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch == '<':
                    state = 'B'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'B':
                if ch == '>':
                    state = 'C'
                else:
                    errors.append(f"")
                    state = 'Z'
            case 'C':
                if ch == '>':
                    state = 'D'
                else:
                    errors.append(f"")
                    state = 'Z'

    if state == 'D':
        tokens.append("<>>")
    else:
        errors.append("Error: Input did not end in the accepting state")

    return tokens, errors

# Arithmetic Operators (from line 310 to line 695)

# Numbers (from line 697 to line 773)
def dfaInteger(input_text):
    state = 'A'  
    tokens = []
    errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'A':
                if ch.isdigit():
                    state = 'B'
                else:
                    errors.append()
                    state = 'Z'
            case 'B':
                if ch.isdigit():
                    state = 'B'  
                else:
                    errors.append()
                    state = 'Z'
            case _:  
                errors.append()
                break

    if state == 'B':
        tokens.append(f"<{input_text}>")
    else:
        errors.append()

    return tokens, errors

def dfaFloat(input_text):
    state = 'A' 
    tokens = []
    errors = []

    for i, ch in enumerate(input_text):
        match state:
            case 'A':
                if ch.isdigit():
                    state = 'B'
                else:
                    errors.append()
                    state = 'Z'
            case 'B':
                if ch.isdigit():
                    state = 'B'
                elif ch == '/':
                    state = 'C'
                else:
                    errors.append()
                    state = 'Z'
            case 'C':
                if ch.isdigit():
                    state = 'D'
                else:
                    errors.append()
                    state = 'Z'
            case 'D':
                if ch.isdigit():
                    state = 'D' 
                else:
                    errors.append()
                    state = 'Z'
            case _:  
                errors.append()
                break

    if state == 'D':
        tokens.append(f"<{input_text}>")
    else:
        errors.append()

    return tokens, errors
# Numbers (from line 697 to line 773)

# DFA for THEN
def dfaTHEN(input_text):
    state = 'X'
    next_tokens = []
    next_errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'T':
                    state = 'Y'
                elif ch in ALPHABET - {'T'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'Y':
                if ch == 'H':
                    state = 'Z'
                elif ch in ALPHABET - {'H'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'Z':
                if ch == 'E':
                    state = 'A'
                elif ch in ALPHABET - {'E'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'A':
                if ch == 'N':
                    next_tokens.append("<THEN_TK>")
                    state = 'Z'

            case _:
                next_errors.append(position)
                break

    if state == 'A':
        next_tokens.append("<THEN_TK>")
    return next_tokens, next_errors


# DFA for colon (:)
def dfaColon(input_text):
    state = 'X'
    colon_tokens = []
    colon_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == ':':
            colon_tokens.append("<:>")
        else:
            colon_errors.append(position)
            break

    return colon_tokens, colon_errors

# DFA for semi colon (,)
def dfaSemiColon(input_text):
    state = 'X'
    semicolon_tokens = []
    semicolon_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == ',':
            semicolon_tokens.append("<,>")
        else:
            semicolon_errors.append(position)
            break

    return semicolon_tokens, semicolon_errors


# DFA for semicolon (;)
def dfaSemicolon(input_text):
    state = 'X'
    semicolon_tokens = []
    semicolon_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == ';':
            semicolon_tokens.append("<;>")
        else:
            semicolon_errors.append(position)
            break

    return semicolon_tokens, semicolon_errors


# DFA for left curly brace ({)
def dfaLeftBrace(input_text):
    state = 'X'
    left_brace_tokens = []
    left_brace_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == '{':
            left_brace_tokens.append("<{>")
        else:
            left_brace_errors.append(position)
            break

    return left_brace_tokens, left_brace_errors


# DFA for pipe symbol (|)
def dfaPipe(input_text):
    state = 'X'
    pipe_tokens = []
    pipe_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == '|':
            pipe_tokens.append("<|>")
        else:
            pipe_errors.append(position)
            break

    return pipe_tokens, pipe_errors


# DFA for right curly brace (})
def dfaRightBrace(input_text):
    state = 'X'
    right_brace_tokens = []
    right_brace_errors = []
    position = 0

    for ch in input_text:
        position += 1
        if ch == '}':
            right_brace_tokens.append("<}>")
        else:
            right_brace_errors.append(position)
            break

    return right_brace_tokens, right_brace_errors


# DFA for WITH
def dfaWITH(input_text):
    state = 'X'
    with_tokens = []
    with_errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'W':
                    state = 'Y'
                elif ch in ALPHABET - {'W'}:
                    with_errors.append(position)
                    state = 'Z'

            case 'Y':
                if ch == 'I':
                    state = 'Z'
                elif ch in ALPHABET - {'I'}:
                    with_errors.append(position)
                    state = 'Z'

            case 'Z':
                if ch == 'T':
                    state = 'A'
                elif ch in ALPHABET - {'T'}:
                    with_errors.append(position)
                    state = 'Z'

            case 'A':
                if ch == 'H':
                    with_tokens.append("<WITH_TK>")
                    state = 'Z'
                elif ch in ALPHABET - {'H'}:
                    with_errors.append(position)
                    state = 'Z'

            case _:
                with_errors.append(position)
                break

    if state == 'A':
        with_tokens.append("<WITH_TK>")
    return with_tokens, with_errors


# DFA for UNTIL
def dfaUNTIL(input_text):
    state = 'X'
    until_tokens = []
    until_errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'U':
                    state = 'Y'
                elif ch in ALPHABET - {'U'}:
                    until_errors.append(position)
                    state = 'Z'

            case 'Y':
                if ch == 'N':
                    state = 'Z'
                elif ch in ALPHABET - {'N'}:
                    until_errors.append(position)
                    state = 'Z'

            case 'Z':
                if ch == 'T':
                    state = 'A'
                elif ch in ALPHABET - {'T'}:
                    until_errors.append(position)
                    state = 'Z'

            case 'A':
                if ch == 'I':
                    state = 'B'
                elif ch in ALPHABET - {'I'}:
                    until_errors.append(position)
                    state = 'Z'

            case 'B':
                if ch == 'L':
                    state = 'C'
                elif ch in ALPHABET - {'L'}:
                    until_errors.append(position)
                    state = 'Z'

            case 'C':
                if ch == 'T':
                    until_tokens.append("<UNTIL_TK>")
                    state = 'Z'

            case _:
                until_errors.append(position)
                break

    if state == 'C':
        until_tokens.append("<UNTIL_TK>")
    return until_tokens, until_errors


# DFA for NEXT
def dfaNEXT(input_text):
    state = 'X'
    next_tokens = []
    next_errors = []
    position = 0

    for ch in input_text:
        position += 1
        match state:
            case 'X':
                if ch == 'N':
                    state = 'Y'
                elif ch in ALPHABET - {'N'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'Y':
                if ch == 'E':
                    state = 'Z'
                elif ch in ALPHABET - {'E'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'Z':
                if ch == 'X':
                    state = 'A'
                elif ch in ALPHABET - {'X'}:
                    next_errors.append(position)
                    state = 'Z'

            case 'A':
                if ch == 'T':
                    next_tokens.append("<NEXT_TK>")
                    state = 'Z'

            case _:
                next_errors.append(position)
                break

    if state == 'A':
        next_tokens.append("<NEXT_TK>")
    return next_tokens, next_errors

def main():
    # Input file
    input_file = r'D:\University\input.txt'
    with open(input_file, 'r', encoding='utf-8') as infile:
        input_text = infile.readlines()

    tokens = []
    errors = []
    id_counter = 1
    identifier_dict = {}

    # Operator DFAs 
    OPdfas = [
        (dfaEquals, "<=>"),
        (dfaAnd, "<×>"),
        (dfaOr, "<+>"),
        (dfaMinus, "<->"),
        (dfaDivide, "<÷>"),
        (dfaNotEqual, "<≠>"),
        (dfaLessthan, "<<>"),
        (dfaGreater, "<>>"),
        (dfaAssignment, "<Assi>")
    ]
    
    # Others DFAs
    othersList = {
        "THEN": dfaTHEN,
        ":": dfaColon,
        ";": dfaSemicolon,
        "{": dfaLeftBrace,
        "|": dfaPipe,
        "}": dfaRightBrace,
        "WITH": dfaWITH,
        "UNTIL": dfaUNTIL,
        ",": dfaSemiColon,
        "NEXT": dfaNEXT
    }

    # Keywords DFAs 
    keywords = {
        "GO": dfaGO,
        "CON": dfaCON,
        "GOCON": dfaGOCON,
        "SUB": dfaSUB,
        "SAYSUBTO": dfaSAYSUBTO,
        "NOTOK": dfaNOTOK
    }

    # Line and word counters
    line_number = 1
    for line in input_text:
        word_position = 1
        input_tokens = line.split()
        
        # Process each token in the line
        for token in input_tokens:
            matched = False

            # Handle numbers
            if token.isdigit():
                tokens.append(f"<{token}>")
                matched = True
            elif '/' in token:
                numerator, *denominator = token.split('/')
                if numerator.isdigit() and len(denominator) == 1 and denominator[0].isdigit():
                    tokens.append(f"<{token}>")
                    matched = True

            # Handle keywords
            if not matched:
                if token in keywords:
                    keyword_func = keywords[token]
                    keyword_tokens, keyword_errors = keyword_func(token)
                    if keyword_tokens:
                        tokens.extend(keyword_tokens)
                        matched = True
                    for error in keyword_errors:
                        errors.append(f"Line {line_number}, Word {word_position}: {error}")

            # Handle others (THEN, :, ;, {, etc.)
            if not matched:
                if token in othersList:
                    others_func = othersList[token]
                    others_tokens, others_errors = others_func(token)
                    if others_tokens:
                        tokens.extend(others_tokens)
                        matched = True
                    for error in others_errors:
                        errors.append(f"Line {line_number}, Word {word_position}: {error}")

            # Handle operators
            if not matched:
                for dfa_func, _ in OPdfas:
                    dfa_tokens, dfa_errors = dfa_func(token)
                    if dfa_tokens:
                        tokens.extend(dfa_tokens)
                        matched = True
                        break

            # Handle identifiers
            if not matched:
                if token.startswith('-') and token.endswith('-') and len(token) > 2:
                    if token in identifier_dict:
                        # Reuse existing token
                        tokens.append(identifier_dict[token])
                    else:
                        # Create a new token and store it
                        identifier_token = f"<id,{id_counter}>"
                        identifier_dict[token] = identifier_token
                        tokens.append(identifier_token)
                        id_counter += 1
                    matched = True

            # Handle unrecognized tokens
            if not matched:
                if "<" in token or ">" in token:
                    errors.append(f"Line {line_number}, Word {word_position}: '{token}' - Cannot be an arithmetic operator")
                else:
                    errors.append(f"Line {line_number}, Word {word_position}: '{token}' - Unrecognized token")
            
            word_position += 1

        line_number += 1

    # Output to file
    output_file = r'D:\University\output.txt'
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write tokens
        for token in tokens:
            outfile.write(f"{token}\n")
        
        # Write errors
        if errors:
            outfile.write("\nErrors:\n")
            for error in errors:
                outfile.write(f"{error}\n")
    

    if tokens:
        print("Tokens:", tokens)
    if errors:
        print("Errors:")
        for error in errors:
            print(error)


if __name__ == "__main__":
    main()
