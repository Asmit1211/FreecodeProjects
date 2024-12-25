def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)
    key_len = len(key)
    key = key.lower()
    result = []

    for i, char in enumerate(message.lower()):
        if char.isalpha():
            # Find the corresponding shift value from the key
            offset = alphabet.index(key[i % key_len])
            index = alphabet.index(char)
            new_index = (index + direction * offset) % alphabet_len
            result.append(alphabet[new_index])
        else:
            # Preserve non-alphabetic characters
            result.append(char)
    
    return ''.join(result)

def encrypt(message, key):
    return vigenere(message, key, direction=1)

def decrypt(message, key):
    return vigenere(message, key, direction=-1)

if __name__ == "__main__":
    text = input("Enter the string: ")
    custom_key = 'happycoding'
    
    encrypted = encrypt(text, custom_key)
    print(f'\nEncrypted text: {encrypted}')
    
    decrypted = decrypt(encrypted, custom_key)
    print(f'\nDecrypted text: {decrypted}\n')
