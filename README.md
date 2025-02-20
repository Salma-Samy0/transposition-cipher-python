# transposition-cipher-python
A Python-based implementation of Row and Column Transposition Ciphers for text encryption and decryption. Features an interactive CLI interface, support for custom keys, and automated padding handling for secure text transformation.



## Features

- Two types of transposition ciphers:
  - Row Transposition
  - Column Transposition
- Support for both encryption and decryption
- Interactive command-line interface
- Automatic padding for incomplete blocks
- Case-insensitive key handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Salma-Samy0/transposition-cipher-python.git
cd transposition-cipher
```

2. No additional dependencies required - the program uses only Python standard library.

## Usage

Run the program:
```bash
python project.py
```

Follow the interactive prompts to:
1. Choose the transposition method (Row/Column)
2. Select operation (Encrypt/Decrypt)
3. Enter the text to process
4. Provide the encryption/decryption key

### Example

```
================================================================================================
Row and Column Transposition Cipher Program
================================================================================================

Choose the transposition method:
1. Row Transposition
2. Column Transposition
3. Exit

Enter your choice (1-3): 1
Enter your choice (1-2): 1
Enter the text: HELLO WORLD
Enter the key: KEY

Ciphertext: HLRLO$OWLED
```

## How It Works

### Row Transposition
1. Removes spaces from the input text
2. Creates a grid based on key length
3. Fills the grid row by row
4. Rearranges columns based on key
5. Reads off row by row

### Column Transposition
1. Removes spaces and converts to lowercase
2. Creates a grid based on key length
3. Fills the grid row by row
4. Rearranges columns based on key
5. Reads off column by column

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
