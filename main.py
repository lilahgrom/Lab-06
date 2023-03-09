#Lilah Grom
def main():
    def encode(password):
        encoded_password = ""
        for digit in password:
            new_digit = str(int(digit) + 5)
            encoded_password += new_digit
        return encoded_password



    while True:
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit")
        choice = input("Please enter an option: ")
        if choice == '1':
            password = input("\nPlease enter a password to encode")
            encode_password = encode(password)
            print("\nYour password has been encoded and stored!")

        if choice == '2':
            pass

        if choice == '3':
            break

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
