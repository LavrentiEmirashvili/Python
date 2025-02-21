alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from caesarart import logo

def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    text = list(text)
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode": 
        decrypt(text, shift)   
    reset()
print(logo)




def encrypt(text, shift):
    for i in range (0,len(text)):
        if text[i] not in alphabet:
            text[i] = text[i]
        else:
            text[i] = alphabet[alphabet.index(text[i])+ shift % len(alphabet) - len(alphabet)]
    print("".join(text))
def decrypt(text, shift):
    for i in range (0,len(text)):
        text[i] = alphabet[alphabet.index(text[i])- shift % len(alphabet) - len(alphabet)]
    print("".join(text))

def reset():
    if input("Do you want to run again?:Y/N\n".lower()) == "y":
        run() 
run()