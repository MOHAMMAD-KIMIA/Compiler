tokens = []
current_token_index = 0

def advance():
    global current_token_index
    if current_token_index < len(tokens) - 1:
        current_token_index += 1

def lookahead():
    if current_token_index < len(tokens):
        return tokens[current_token_index]
    return None

def match(expected_token):
    global current_token_index
    token = lookahead()

    # Special handling for <id,number>
    if expected_token.startswith("<id,") and expected_token.endswith(">"):
        if token.startswith("<id,") and token.endswith(">"):
            # Extract the number part
            number_part = token[4:-1]
            if number_part.isdigit():
                print(f"Matched: {token}")
                advance()
                return
        raise SyntaxError(f"Syntax error: Expected {expected_token}, but got {token}")
    
    # Default exact match
    if token == expected_token:
        print(f"Matched: {token}")
        advance()
    else:
        raise SyntaxError(f"Syntax error: Expected {expected_token}, but got {token}")
    
def START():
    # START -> StmtList | id Expression | λ
    token = lookahead()
    if token.startswith("<id,") and token.endswith(">"):
        match(token)
        Expression()
    elif lookahead() in {"<CON_TK>", "<GO_TK>", "<GOCON_TK>", "<SUB_TK>", "<SAYSUBTO_TK>"}:
        StmtList()
    else:
        # Allow λ (empty production)
        print("START: λ (empty production)")

def StmtList():
    token = lookahead()
    if token == "<CON_TK>":
        IfStmt()
    elif token == "<GO_TK>":
        WhileStmt()
    elif token == "<GOCON_TK>":
        ForStmt()
    elif token == "<SUB_TK>":
        FuncStmt()
    elif token == "<SAYSUBTO_TK>":
        Callfunc()
    else:
        raise SyntaxError("StmtList: Invalid statement")

def IfStmt():
    # IfStmt -> CON Condition THEN: { START }; X
    match("<CON_TK>")
    match("<|>")
    Condition()
    match("<|>")
    match("<THEN_TK>")
    match("<:>")
    match("<{>")
    START()
    match("<}>")
    match("<;>")
    X()

def X():
    # X -> ElseStmt | START | λ
    token = lookahead()
    if token == "<NOTOK_TK>":
        ElseStmt()
    elif token in {"<CON_TK>", "<GO_TK>", "<GOCON_TK>", "<SUB_TK>", "<SAYSUBTO_TK>", "<id>"}:
        START()
    else:
        print("X: λ (empty production)")

def ElseStmt():
    # ElseStmt -> NOTOK { START }; Y
    match("<NOTOK_TK>")
    match("<{>")
    START()
    match("<}>")
    match("<;>")
    Y()

def Y():
    # Y -> START | λ
    token = lookahead()
    if token in {"<CON_TK>", "<GO_TK>", "<GOCON_TK>", "<SUB_TK>", "<SAYSUBTO_TK>", "<id>"}:
        START()
    else:
        print("Y: λ (empty production)")

def WhileStmt():
    # WhileStmt -> GO UNTIL Condition { START }; Y
    match("<GO_TK>")
    match("<|>")
    match("<UNTIL_TK>")
    Condition()
    match("<|>")
    match("<{>")
    START()
    match("<}>")
    match("<;>")
    Y()
def ForStmt():
    # ForStmt -> GOCON WITH Condition UNTIL Condition NEXT Condition { START }; Y
    match("<GOCON_TK>")
    match("<|>")
    match("<WITH_TK>")
    Condition()
    match("<UNTIL_TK>")
    Condition()
    match("<NEXT_TK>")
    Condition()
    match("<|>")
    match("<{>")
    START()
    match("<}>")
    match("<;>")
    Y()

def FuncStmt():
    # FuncStmt -> SUB(id ,PARAMETER) { START }; Y
    match("<SUB_TK>")
    match("<(>")
    match("<id,\\d+>")
    match("<,>")
    PARAMETER()
    match("<)>")
    match("<{>")
    START()
    match("<}>")
    match("<;>")
    Y()

def Callfunc():
    # Callfunc -> SAYSUBTO(id ,PARAMETER) Y
    match("<SAYSUBTO_TK>")
    match("<(>")
    match("<id,\\d+>")
    match("<,>")
    PARAMETER()
    match("<)>")
    Y()

def Condition():
    # Condition -> TERM ASSIGN TERM
    TERM()
    ASSIGNMENT()
    TERM()

def Expression():
    # Expression -> ∈ TERM OP TERM START
    match("<Assi>")
    TERM()
    OPERATOR()
    TERM()
    START()

def TERM():
    # TERM -> id | NUMBER
    token = lookahead()
    
    if token.startswith("<id,") and token.endswith(">"):
        counter = token[4:-1]  
        if counter.isdigit():
            match(token)
        else:
            raise SyntaxError(f"TERM: Invalid identifier format. Got {token}")
    
    elif token.startswith("<") and token.endswith(">") and token[1:-1].isdigit():
        match(token)
    
    elif token.startswith("<") and token.endswith(">") and "/" in token[1:-1]:
        fraction = token[1:-1]  # Extract the content inside "<>"
        numerator, *denominator = fraction.split("/")
        if numerator.isdigit() and len(denominator) == 1 and denominator[0].isdigit():
            match(token)
            
    else:
        raise SyntaxError(f"TERM: Invalid TERM. Got {token}")

def PARAMETER():
    # PARAMETER -> id Q
    match("<id,\\d+>")
    Q()

def Q():
    # Q -> , id Q | λ
    if lookahead() == "<,>":
        match("<,>")
        match("<id,\\d+>")
        Q()

def ASSIGNMENT():
    # ASSIGNMENT -> => | <> | >> | ≠>
    token = lookahead()
    if token in {"<=>", "<<>", "<>>", "<≠>"}:
        match(token)
    else:
        raise SyntaxError(f"ASSIGNMENT: Invalid ASSIGNMENT operator. Got {token}")

def OPERATOR():
    # OPERATOR -> <∨> | <-> | <∧> | <∺>
    token = lookahead()
    if token in {"<×>", "<->", "<+>", "<÷>"}:
        match(token)
    else:
        raise SyntaxError(f"OPERATOR: Invalid OPERATOR. Got {token}")

# Example Usage
if __name__ == "__main__":
    input_file = "output.txt"
    output_file = "syntax_analysis_output.txt"

    try:
        with open(input_file, "r", encoding='utf-8') as file:
            content = file.read()

            with open(output_file, "w", encoding="utf-8") as outfile:
                # Check if the file contains "Errors:"
                if "Errors:" in content:
                    message = "Lexical errors found in the file. Syntax analysis skipped.\n"
                    print(message)
                    outfile.write(message)
                else:
                    # Normalize the input to handle both inline and line-by-line tokens
                    tokens = [token.strip() for token in content.replace("\n", " ").split() if token.strip()]
                    
                    current_token_index = 0
                    try:
                        START()
                        message = "Syntax analysis completed successfully.\n"
                        print(message)
                        outfile.write(message)
                    except SyntaxError as e:
                        message = f"Syntax Error: {e}\n"
                        print(message)
                        outfile.write(message)

    except FileNotFoundError:
        message = f"Error: The file {input_file} does not exist.\n"
        print(message)
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(message)