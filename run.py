def print_menu():
    """
    Prints the menu so that the user can choose what they want to do. 
    """
    menu_options = {
        1: 'Analyze website',
        2: 'Analyze text input',
        3: 'Exit',
    }

    def print_menu_options():
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )

    if __name__=='__main__':
        while(True):
            print_menu_options()
            option = ''
            try:
                option = int(input('What do you want to do: '))
            except:
                print('Invalid input. Please enter a number.')
            
            if option == 1:
                option1()
                exit()
            elif option == 2:
                option2()
                exit()
            elif option == 3:
                print('Thank you for using Text Analyzer')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')


def option1():
    print('Let us look at the page')


def option2():
    print('Paste your input')


def main():
    """
    Run all programs
    """
    print_menu()

print("Welcome to Text Analyzer")
main()