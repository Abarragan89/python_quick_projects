alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play = 'Yes'
def ceasar_cipher(text, shift):
    newString = ''
    for letter in text:
        if letter == ' ':
            newString += ' '
            continue
        position = alphabet.index(letter)
        if direction == "encode":
            new_char_index = (position + shift) % 26
        elif direction == "decode":
            new_char_index = (position - shift) % 26
        newString += alphabet[new_char_index]
    print(f"Your encoded message is: {newString}")

while play == 'yes':
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar_cipher(text, shift)
    play = input("Would you like to play again? 'Yes' or 'No'").lower()
