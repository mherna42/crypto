alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    for i in range(len(alphabet)):
        if alphabet[i] == lettter.lower():
            return i


def rotate_character(char, rot):
    if no char.isalpha():
        return char
    char_index = alphabet_position(char)
    rot_index = (char_index + rot) % 26
    if char.isupper() == True:
        return alphabet[rot_index].upper()
    return alphabet[rot_index]
