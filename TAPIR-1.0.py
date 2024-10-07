# TAPIR Encoder/Decoder
tapir_table = {
    'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06',
    'G': '07', 'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12',
    'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
    'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
    'Y': '25', 'Z': '26', '0': '27', '1': '28', '2': '29', '3': '30',
    '4': '31', '5': '32', '6': '33', '7': '34', '8': '35', '9': '36',
    'GE': '37', 'BE': '38', 'TE': '39', 'SPACE': '40'  # Add your codes as needed
}

# Function to encode a message
def tapir_encode(message):
    encoded_message = []
    words = message.split(' ')  # Split message into words
    for word in words:
        i = 0
        while i < len(word):
            # Check for 'GE', 'BE', etc. which are two-letter mappings
            if word[i:i+2].upper() in tapir_table:
                encoded_message.append(tapir_table[word[i:i+2].upper()])
                i += 2  # Skip next character since it's part of the 2-letter code
            else:
                encoded_message.append(tapir_table.get(word[i].upper(), '?'))  # Encode single char
                i += 1
        encoded_message.append(tapir_table['SPACE'])  # Add space after each word
    
    # Join encoded messages into one string, removing the last space
    encoded_str = ''.join(encoded_message[:-1])  # Remove the last added space

    # Pad only the final group to make it 5 characters, if needed
    remainder = len(encoded_str) % 5
    if remainder != 0:
        padding_needed = 5 - remainder
        encoded_str += '40' * padding_needed  # Add padding using '40' (encoded space)

    # Group the encoded message into sets of 5 characters
    grouped_encoded_str = ' '.join(encoded_str[i:i + 5] for i in range(0, len(encoded_str), 5))
    
    return grouped_encoded_str

# Function to decode a message
def tapir_decode(encoded_message):
    decoded_message = []
    encoded_numbers = encoded_message.replace(' ', '')  # Remove spaces for decoding
    for i in range(0, len(encoded_numbers), 2):  # Read 2 characters at a time
        number = encoded_numbers[i:i + 2]
        # Find the letter corresponding to the number
        found = next((k for k, v in tapir_table.items() if v == number), None)
        if found:
            decoded_message.append(found)
        else:
            decoded_message.append('?')  # Use '?' for unrecognized codes
    
    return ''.join(decoded_message).replace('SPACE', ' ')  # Replace 'SPACE' with actual space

def main():
    print("Welcome to M0KVI's TAPIR encoder/decoder")
    print("Please use uppercase letters, numbers, and spaces only.")
    print("Enter 'x' at any prompt to quit.")
    
    while True:
        action = input("Would you like to (e)ncode, (d)ecode a message, or (x) to exit? ").strip().lower()
        
        if action == 'e':
            message = input("Enter the message to encode: ")
            if message.lower() == 'q':
                break
            encoded = tapir_encode(message)
            print("\n====================")
            print("Encoded message:")
            print(encoded)
            print("====================\n")
        elif action == 'd':
            encoded_message = input("Enter the encoded message (numbers separated by spaces): ")
            if encoded_message.lower() == 'q':
                break
            decoded = tapir_decode(encoded_message)
            print("\n====================")
            print("Decoded message:")
            print(decoded)
            print("====================\n")
        elif action == 'x':  # Check for 'x' to exit
            break
        else:
            print("Invalid option selected. Please choose 'e' for encode, 'd' for decode, or 'x' to exit.")

if __name__ == '__main__':
    main()

