
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

def main():
    # Input file
    input_file = r'D:\University\input.txt'
    with open(input_file, 'r') as infile:
        input_text = infile.readlines()

    tokens = []
    errors = []
    id_counter = 1
    identifier_dict = {}

    # op DFAs
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

    # Line and word
    line_number = 1
    for line in input_text:
        word_position = 1
        input_tokens = line.split()
        
        # token in each line
        for token in input_tokens:
            matched = False

            # numbers
            if token.isdigit():
                tokens.append(f"<{token}>")
                matched = True
            elif '/' in token:
                numerator, *denominator = token.split('/')
                if numerator.isdigit() and len(denominator) == 1 and denominator[0].isdigit():
                    tokens.append(f"<{token}>")
                    matched = True

            # keywords
            if not matched:
                keywords = {
                    "GO": dfaGO,
                    "CON": dfaCON,
                    "GOCON": dfaGOCON,
                    "SUB": dfaSUB,
                    "SAYSUBTO": dfaSAYSUBTO,
                    "NOTOK": dfaNOTOK,
                }
                if token in keywords:
                    keyword_func = keywords[token]
                    keyword_tokens, keyword_errors = keyword_func(token)
                    if keyword_tokens:
                        tokens.extend(keyword_tokens)
                        matched = True
                    for error in keyword_errors:
                        errors.append(f"Line {line_number}, Word {word_position}: {error}")

            # operators
            if not matched:
                for dfa_func, expected_token in OPdfas:
                    dfa_tokens, dfa_errors = dfa_func(token)
                    if dfa_tokens:
                        tokens.extend(dfa_tokens)
                        matched = True
                        break

            #identifiers
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

            # unrecognized tokens
            if not matched:
                if "<" in token or ">" in token:
                    errors.append(f"Line {line_number}, Word {word_position}: '{token}' - Cannot be an arithmetic operator")
                else:
                    errors.append(f"Line {line_number}, Word {word_position}: '{token}' - Unrecognized token")
            
            word_position += 1

        line_number += 1

    # output file
    output_file = r'D:\University\output.txt'
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write tokens
        for token in tokens:
            outfile.write(f"{token}\n")
        
        # errors
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
