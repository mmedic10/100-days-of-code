from art import logo
import math


def caesar (text,shift,direction):
    nueva_palabra = ""
    if direction == "decode":
        shift*=-1
    for i in text:
        if i in alphabet:
            pos = alphabet.index(i)   
            new_pos = pos + shift
            nueva_palabra += alphabet[new_pos]
        else:
            nueva_palabra += i
    print(f"The {direction}d text is {nueva_palabra}")


print(logo)
continuar = 'yes'
while continuar == 'yes':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text=text,shift=shift,direction=direction)
    continuar = input("Do you want to restart the cipher program? yer or no\n").lower()
    if continuar != 'yes':
        print("Good Bye!")

                  



