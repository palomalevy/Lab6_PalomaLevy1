# “12345555” will become “45678888”

def print_menu():
    # Prints menu
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')

def encoder(password):
    # Encodes the password inputed by user
    list = [] # Makes the string a list

    for item in password: # Checks each item in the list

        item = int(item)

        # Encodes each item
        if item == 9:
            item = 2
        elif item == 8:
            item = 1
        elif item == 7:
            item = 0
        else:
            item = int(item) + 3

        list.append(item)

    encoded_pwd = ''.join(map(str, list)) # joins the list and makes it a string

    return encoded_pwd

def main():

    while True:

        print_menu()

        menu_option = int(input('Please enter an option:')) # User inputs option

        # Executes different menu options
        if menu_option == 1:
            original_pwd = input('Please enter your password to encode:')

            # new_pwd is the saved encoded password
            new_pwd = encoder(original_pwd)

            print('Your password has been encoded and stored!\n')

        elif menu_option == 2:
            pass

        elif menu_option == 3:
            break

if __name__ == '__main__':
    main()
