# Compiler Project

This project is a custom compiler written in Python for a unique programming language. It performs two critical phases of compilation: **lexical analysis** and **syntax analysis**. These phases are designed to break down and validate source code, ensuring it adheres to predefined rules and structure.

The project is an educational tool, showcasing how compilers analyze and validate source code.

## Features

### Lexical Analysis
- Breaks down the input source code into tokens.
- Supports keywords, custom operators, constants, and identifiers.
- Detects and reports unrecognized tokens with detailed error messages, including line and word position.

### Syntax Analysis
- Validates the program's structure according to specified grammar rules.
- Ensures correct relationships and sequences between tokens.
- Reports syntax errors with contextual information to aid debugging.

### Custom Token Rules
- Recognizes user-defined operators (e.g., `<=>`, `<+>`, `<->`).
- Supports identifiers enclosed in hyphens (e.g., `-myVar-`).
- Handles numeric constants, including fractions (e.g., `123`, `45/67`).

## Grammar Rules

**Version 1:**

```plaintext
START -> StmtList | id Expression | $
StmtList -> IfStmt | WhileStmt | ForStmt | FuncStmt | CallFunc
IfStmt -> CON | Condition | THEN: { START }; X
X -> ElseStmt | START | λ
ElseStmt -> NOTOK { START }; Y
Y -> START | λ
WhileStmt -> GO | UNTIL Condition | { START }; Y
ForStmt -> GOCON | WITH Condition UNTIL Condition NEXT Condition | { START }; Y
FuncStmt -> SUB(id, PARAMETER) { START }; Y
CallFunc -> SAYSUBTO(id, PARAMETER) Y
Condition -> TERM ASSIGN TERM
Expression -> ∈ TERM OP TERM
TERM -> id | integer | float
PARAMETER -> id Q
Q -> , PARAMETER | λ
ASSIGN -> <=> | <<> | <>> | <≠>
OP -> <∨> | <-> | <∧> | <∺>
```

**First/Follow Analysis:**
- **START:**
  - **Firsts:** `<CON_TK>`, `<GO_TK>`, `<GOCON_TK>`, `<SUB_TK>`, `<SAYSUBTO_TK>`, `<id,number>`
  - **Follows:** `}`, `$`

- **StmtList:**
  - **Firsts:** `<CON_TK>`, `<GO_TK>`, `<GOCON_TK>`, `<SUB_TK>`, `<SAYSUBTO_TK>`
  - **Follows:** `}`, `$`

- **IfStmt:**
  - **Firsts:** `<CON_TK>`
  - **Follows:** `}`, `$`

- **WhileStmt:**
  - **Firsts:** `<GO_TK>`
  - **Follows:** `}`, `$`

- **ForStmt:**
  - **Firsts:** `<GOCON_TK>`
  - **Follows:** `}`, `$`

- **FuncStmt:**
  - **Firsts:** `<SUB_TK>`
  - **Follows:** `}`, `$`

- **CallFunc:**
  - **Firsts:** `<SAYSUBTO_TK>`
  - **Follows:** `}`, `$`

- **Condition:**
  - **Firsts:** `<id,number>`
  - **Follows:** `UNTIL`, `NEXT`

- **Expression:**
  - **Firsts:** `∈`
  - **Follows:** `}`, `$`

- **TERM:**
  - **Firsts:** `<id,number>`
  - **Follows:** `}`, `$`

- **PARAMETER:**
  - **Firsts:** `<id,number>`
  - **Follows:** `)`

- **ASSIGN:**
  - **Firsts:** `<=>`, `<<>`, `<>>`, `<≠>`
  - **Follows:** `<id,number>`

- **OP:**
  - **Firsts:** `<∨>`, `<->`, `<∧>`, `<∺>`
  - **Follows:** `<id,number>`

## Example Code

An example of the source code processed by the compiler:

```plaintext
GO CON -identifier- 
123 <+> 456 
invalid-token SAYSUBTO -anotherIdentifier-
```

### Expected Output

**Tokens:**
```
<GO>
<CON>
<id,1>
<123>
<<+>>
<456>
<SAYSUBTO>
<id,2>
```

**Errors:**
```
Line 1, Word 4: 'invalid-token' - Unrecognized token
```

### Syntax Errors Example

Input:
```plaintext
GO 123 <->
CON -variable- SAYSUBTO
```

Output:
```
Syntax Errors:
Line 1: Incomplete expression after '123'.
Line 2: Unexpected command 'SAYSUBTO' following an identifier.
```

## How It Works

### 1. **Input**
- The source code is read from a file (`input.txt`).

### 2. **Lexical Analysis**
- The code is split into words and matched against predefined rules for:
  - Keywords (e.g., `GO`, `CON`, `SAYSUBTO`).
  - Operators (e.g., `<+>`, `<->`).
  - Identifiers (`-identifier-` format).
  - Numbers and fractions (`123`, `45/67`).

### 3. **Syntax Analysis**
- The tokens are organized into a parse tree based on grammar rules.
- Relationships between tokens are validated for correctness.
- Syntax errors are logged with line numbers and contextual details.

### 4. **Error Handling**
- Unrecognized tokens or invalid constructs are logged with their line number and position in the line.

### 5. **Output**
- Tokens are written to an output file (`output.txt`).
- Syntax and lexical errors are detailed in the same file or printed to the console for debugging.

## Example Workflow

1. Write your source code into `input.txt`:
    ```plaintext
    GO <=> 123/45
    -variable- SUB xyz
    ```

2. Run the compiler:
    ```bash
    python COM.py
    ```

3. Check the output in `output.txt`:
    ```
    <GO>
    <=>
    <123/45>
    <id,1>
    <SUB>

    Errors:
    Line 2, Word 3: 'xyz' - Unrecognized token
    Line 2: Syntax error: Missing operator or invalid sequence after 'SUB'.
    ```

## Usage

1. Clone the repository.
2. Install Python 3.7 or later.
3. Place your source code in `input.txt`.
4. Run the compiler with:
   ```bash
   python COM.py
   ```
5. Check `output.txt` for tokens and errors.

## Contributions

Contributions are welcome! Feel free to create issues or submit pull requests to enhance the compiler. Examples include adding new token rules, improving syntax analysis, or optimizing performance.

