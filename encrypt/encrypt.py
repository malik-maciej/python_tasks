encrypted = {
    "a": "y", "e": "i", "i": "o", "o": "a", "y": "e"
}

decrypted = dict(zip(encrypted.values(), encrypted.keys()))


def encryption(user_text):
    encrypted_text = ""
    for letter in user_text:
        if letter in encrypted:
            encrypted_text += encrypted[letter]
        else:
            encrypted_text += letter
    return encrypted_text


def decryption(user_text):
    decrypted_text = ""
    for letter in user_text:
        if letter in decrypted:
            decrypted_text += decrypted[letter]
        else:
            decrypted_text += letter
    return decrypted_text
