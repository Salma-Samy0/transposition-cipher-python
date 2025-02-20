def display_header():
    print("\n" + "=" * 120)
    print("Row and Column Transposition Cipher Program")
    print("=" * 120 + "\n")

def get_transposition_choice():
    while True:
        print("Choose the transposition method:")
        print("1. Row Transposition")
        print("2. Column Transposition")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice! Please enter a number between 1 and 3.\n")

def get_operation_choice():
    while True:
        print("Choose the operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter your choice (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice! Please enter 1 or 2.\n")

def get_inputs():
    text = input("Enter the text: ").strip()
    key = input("Enter the key (word or number): ").strip()
    return text, key

def row_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    #Calculate Grid Dimensions
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)  # Ceiling division for rows
    padded_plaintext = plaintext.ljust(num_rows * num_columns, '$')

    grid = [padded_plaintext[i:i + num_columns] for i in range(0, len(padded_plaintext), num_columns)]

    #Splits the padded plaintext into rows
    key_order = sorted(range(len(key)), key=lambda x: key[x])

    #characters are rearranged
    encrypted_rows = [''.join(grid[row][key_order[i]] for i in range(num_columns)) for row in range(num_rows)]
    ciphertext = ''.join(encrypted_rows)
    return ciphertext

def row_decrypt(ciphertext, key):
    #Calculate Grid Dimensions
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns

    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    index = 0
    for row in range(num_rows):
        for col_index in key_order:
            grid[row][col_index] = ciphertext[index]
            index += 1

    plaintext = ''.join(''.join(row) for row in grid).rstrip('$')
    return plaintext

def column_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").lower()
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)

    padding_chars = ['$'] * (num_rows * num_columns - len(plaintext))
    padded_plaintext = plaintext + "".join(padding_chars)

    grid = [padded_plaintext[i:i + num_columns] for i in range(0, len(padded_plaintext), num_columns)]
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = "".join("".join(row[i] for row in grid) for i in sorted_key_indices)
    return ciphertext

def column_transposition_decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns

    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    grid = [["" for _ in range(num_columns)] for _ in range(num_rows)]

    # fill the grid column by column
    index = 0
    for col_index in sorted_key_indices:
        for row in range(num_rows):
            grid[row][col_index] = ciphertext[index]
            index += 1
#Reads the grid row by row to reconstruct the plaintext.
    plaintext = "".join("".join(row) for row in grid).rstrip("$")
    return plaintext

def main():
    display_header()
    while True:
        transposition_choice = get_transposition_choice()

        if transposition_choice == '3':
            print("Exiting program. Goodbye!")
            break

        operation_choice = get_operation_choice()
        text, key = get_inputs()

        if transposition_choice == '1':  # Row Transposition
            if operation_choice == '1':
                ciphertext = row_encrypt(text, key)
                print("\nCiphertext (Row Transposition):", ciphertext)
            elif operation_choice == '2':
                plaintext = row_decrypt(text, key)
                print("\nPlaintext (Row Transposition):", plaintext)

        elif transposition_choice == '2':  # Column Transposition
            if operation_choice == '1':
                ciphertext = column_transposition_encrypt(text, key)
                print("\nCiphertext (Column Transposition):", ciphertext)
            elif operation_choice == '2':
                plaintext = column_transposition_decrypt(text, key)
                print("\nPlaintext (Column Transposition):", plaintext)

#Execution Control
#main() function (which contains the core logic of your program)
# runs only when the script is executed directly, not when it is imported as a module.
if __name__ == "__main__":
    main()
