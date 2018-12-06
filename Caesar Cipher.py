'''
Encrypt a message using a Caesar cipher. The user will enter a key that will encrypt
the message by right shifting the alphabet a fixed number of places (i.e. key value).
This will map each individial letter to a different, specific, letter in the alphabet.
'''

def get_key():
    '''
    The user will be prompted to enter their encyption key, which will be used to
    shift the alphaet a fixed number of spaces to the right. A valid key should be
    an integer from 1 to 26, inclusive. Parse user input and only return a valid key.

    :return: User encryption key
    :rtype: int
    '''
    print('To encypt a message using Caesar cipher first enter your encryption key: ' \
        'any integer 1 through 26, inclusive...\n')

    # Prompt user for key. Valid key is an integer 1 through 26 inclusive. If the
    # key is invalid, the user will be prompted again.
    while True:
        try:
            user_key = int(input('Enter key >>> '))
            if user_key < 1 or user_key > 26:
                print("\nKey must be an integer from 1 through 26\n")
                continue
        except:
            print('\nKey must be an integer\n')
        else:
            break

    return user_key

def get_message():
    '''
    The user will be prompted for their message to be encrypted. A valid message
    will consist of only letters (uppercase or lowercase) and spaces. Parse user
    input and only return a valid message.

    :return: User message to be encrypted
    :rtype: string
    '''
    print('\nEnter your message, must contain only letters and spaces...\n')

    # Prompy user for message. Valid message with contain only letters and spaces.
    # If the message is invalid, the user will be prompted again.
    while True:
        user_msg = input('Enter message >>> ')
        valid = True
        for char in user_msg:
            if char != ' ' and not char.isalpha():
                print('\nMessage must contain letters and spaces only\n')
                valid = False
                break

        if valid:
            break
        else:
            continue

    return user_msg

def cipher(key, message):
    '''
    Encrypt the user message using given user key.
    '''
    encrypted_msg = ''

    # Iterate through each character in user message, encrypting one character per
    # interation. Identifies each character via unicode, utilizing built-in functions
    # ord() and chr(), in order to efficiently encrypt message using given user key.
    # ord('A') = 65, ..., ord('Z') = 90
    # ord('a') = 97, ..., ord('z') = 122
    # chr() inverts numbers to characters.
    for char in message:
        # Skip spaces to preserve correct word count
        if char == ' ':
            encrypted_msg += ' '
            continue

        # Encrypted character right shifted by user key
        num = ord(char) + key

        # If encrypted character is shifted past letter 'Z' (uppercase) or 'z'
        # (lowercase), the alphabet wraps around to 'A' or 'a' respectively.
        # Preserves correct character shift thoughout.
        if char.isupper():
            if num > ord('Z'):
                num -= 26
        else:
            if num > ord('z'):
                num -= 26

        encrypted_msg += chr(num)

    return encrypted_msg

def main():
    key = get_key()
    msg = get_message()
    encrypted = cipher(key, msg)

    print()
    print(f'Key:                {key}')
    print(f'Message:            {msg}')
    print(f'Encrypted Message:  {encrypted}')

if __name__ == '__main__':
    main()
