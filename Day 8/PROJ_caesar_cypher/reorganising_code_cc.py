alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, input_shift, input_direction):
    if direction == "encode":
        cipher_text = ""
        for letter in input_text:
            position = alphabet.index(letter)
            new_position = position + input_shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    elif direction == "decode":
        decipher_text = ""
        for letter in input_text:
            position = alphabet.index(letter)
            new_position = position - input_shift
            new_letter = alphabet[new_position]
            decipher_text += new_letter
        print(f"The decoded text is {decipher_text}")

caesar(input_text=text, input_shift=shift, input_direction=direction)