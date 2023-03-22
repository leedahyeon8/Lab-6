# Day 3/7/23 worked with Ryan

def encode(password):
    encoded = ""
    for i in password:
        new = str(int(i) + 3)
        if len(new) > 1:
            encoded += new[1:]
        else:
            encoded += new
    return encoded


def decoder(password):
    decoded = ""
    for char in password:
        decoded += str(int(char) - 3)
    return decoded


def main():
    original = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            original = input("Please enter your password to encode: ")
            encoded_pw = encode(original)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_pw = decoder(encoded_pw)
            print(f"The encoded password is {encoded_pw}, and the original password is {original}.")
        elif option == 3:
            break


main()
