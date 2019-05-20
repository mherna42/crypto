from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    mixed_string = ""
    for i in text:
        mixed_string += (rotate_character(i, rot))
    return mixed string    
    
def main():
    text = input("Type a message: ")
    rot = int(input("How much do you want to rotate by? ")
    print(encrypt(text, rot))
              
if __name__=="__main__":
    main()
