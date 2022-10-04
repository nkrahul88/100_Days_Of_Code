alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list_lgth = len(alphabet)
# print(list_lgth)

# def encode(shift, text):
#   display = []
#   final_display = []
#   output = ""
#   for char in text:
#     display += char
#     for position in range(list_lgth):
#       if alphabet[position] == char:
#           final_display += alphabet[position + shift]
#   print(output.join(final_display))

def encode(shift, text):
  encoded_text = ""
  for char in text:
    position = alphabet.index(char)
    new_position = position + shift
    encoded_text += alphabet[new_position]
  print(encoded_text)  

def decode(shift, text):
  encoded_text = ""
  for char in text:
    position = alphabet.index(char)
    new_position = position - shift
    encoded_text += alphabet[new_position]
  print(encoded_text)  

# def decode(shift, text):
#   display = []
#   final_display = []
#   output = ""
#   for char in text:
#     display += char
#     for position in range(list_lgth):
#       if alphabet[position] == char:
#           final_display += alphabet[position - shift]
#   print(output.join(final_display))  

def caesar(shift, text, direction):
  encoded_text = ""
  for char in text:
    if char in alphabet:
        position = alphabet.index(char)
        if direction == "encode":
            new_position = position + shift
        elif direction == "decode":
            new_position = position - shift
        else:
            print("Invalid input, try again")
            exit()
        encoded_text += alphabet[new_position]
    else:
        encoded_text += char
  print(encoded_text)  

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(shift, text, direction)
    # if direction == "encode":
    #   encode(shift, text)
    # elif direction == "decode":
    #   decode(shift, text)
    result = input("Type yes to continue or no to exit out: \n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")