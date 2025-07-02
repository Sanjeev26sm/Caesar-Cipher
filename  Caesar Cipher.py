alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Enter 'encode' to encrypt and 'decode' to decrypt:").lower()
text = input("Enter the message:")
shift = int(input("Enter the number of shift to be done:"))

def caesar(original_text,shift_ammount,encode_or_decode):
    output = ""
    if encode_or_decode == 'decode':
                shift_ammount *= -1
    for letter in original_text:
        
        if letter not in alphabet:
            output += letter
        else:
                
            shift_position = alphabet.index(letter) + shift_ammount #7 + 2 -> 9
            shift_position %= len(alphabet)
            output += alphabet[shift_position]

    print(f"Here is the {encode_or_decode}d message: {output}")
con = True
while con:

    direction = input("Enter 'encode' to encrypt and 'decode' to decrypt:").lower()
    text = input("Enter the message:")
    shift = int(input("Enter the number of shift to be done:"))
    caesar(original_text=text,shift_ammount=shift,encode_or_decode=direction)

    restart =input("Type 'yes' if you want to continue\nOtherwise type 'no' if you want to exit:").lower()
    if restart == 'no':
        con = False
        print("Good Bye!")


