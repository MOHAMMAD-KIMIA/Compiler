# Compiler Project

This project is a custom compiler written in Python for a unique programming language. It performs **lexical analysis** to break down source code into meaningful tokens, such as keywords, operators, constants, identifiers, and more. Additionally, it includes **syntax analysis** to validate the structure of the code, ensuring it adheres to the language's predefined rules. 

The project is designed to demonstrate the fundamental processes of a compiler, making it ideal for understanding how source code is analyzed and validated.

## Features

- **Lexical Analysis**:
  - Breaks down the input source code into tokens.
  - Supports keywords, custom operators, constants, and identifiers.
  - Detects and reports unrecognized tokens with detailed error messages including line and word position.

- **Syntax Analysis**:
  - Ensures the program's structure follows specified grammar rules.
  - Reports syntax errors with contextual information.

- **Custom Token Rules**:
  - Recognizes user-defined operators (e.g., `<=>`, `<+>`, `<->`).
  - Supports identifiers enclosed in hyphens (e.g., `-myVar-`).
  - Handles numeric constants, including fractions (e.g., `123`, `45/67`).

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

## How It Works

1. **Input**: 
   - The source code is read from a file (`input.txt`).

2. **Tokenization**: 
   - The code is split into words and matched against predefined rules for:
     - Keywords (e.g., `GO`, `CON`, `SAYSUBTO`).
     - Operators (e.g., `<+>`, `<->`).
     - Identifiers (`-identifier-` format).
     - Numbers and fractions (`123`, `45/67`).

3. **Error Handling**:
   - Unrecognized tokens or invalid constructs are logged with their line number and position in the line.

4. **Output**:
   - Tokens are written to an output file (`output.txt`).
   - Errors are detailed in the same file, or printed to the console for debugging.

## Example Workflow

1. Write your source code into `input.txt`:
    ```plaintext
    GO <=> 123/45
    -variable- SUB xyz
    ```

2. Run the compiler:
    ```bash
    COM.py
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
    ```

## Usage

1. Clone the repository.
2. Install Python 3.7 or later.
3. Place your source code in `input.txt`.
4. Run the compiler with:
   ```bash
   COM.py
   ```
5. Check `output.txt` for tokens and errors.

## Contributions

Contributions are welcome! Feel free to create issues or submit pull requests to enhance the compiler. Examples include adding new token rules, improving syntax analysis, or optimizing performance.
