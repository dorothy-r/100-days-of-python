import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


# A function that shifts each letter of the text and prints encrypted/decrypted text


def caesar(input_text, shift_amount, code_direction):
    new_text = ""
    if code_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter = alphabet[(letter_index + shift_amount) % 26]
        else:
            new_letter = letter
        new_text += new_letter
    print(f"The {code_direction}d text is {new_text}.")


play_again = "yes"
while play_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    play_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
print("Goodbye.")
