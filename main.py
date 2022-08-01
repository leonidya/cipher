
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(text, shift, direction):
    cipher_text = ""
    for letter_from_the_word in text:
        index = alphabet.index(letter_from_the_word)
        if direction == "encode":
            index +=shift
            if index > 26:
                index = index%26
        elif direction == "decode":
            index -=shift
            if index < 0:
                index = index+26
        cipher_text += alphabet[index]
    print(f'The {direction}d text is {cipher_text}.')

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter_from_the_word in text:
#         index = alphabet.index(letter_from_the_word)
#         index +=shift
#         if index > 26:
#             index = index%26
#         cipher_text += alphabet[index]
#     print(f'The encoded text is {cipher_text}.')

# def decrypt(text, shift):
#     cipher_text = ""
#     for letter_from_the_word in text:
#         index = alphabet.index(letter_from_the_word)
#         index -=shift
#         if index < 0:
#             index = index+26
#         cipher_text += alphabet[index]
#     print(f'The encoded text is {cipher_text}.')

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ceaser(text, shift, direction)