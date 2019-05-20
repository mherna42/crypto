from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
 
    result = ""
    for char in text:
        result += rotate_character(char, rot)
    return result

def main():
    text = input("Type a message: ")
    rot = int(input("How much do you want to rotate by? "))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
