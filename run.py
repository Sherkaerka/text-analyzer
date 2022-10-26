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
                analyze_website()
                exit()
            elif option == 2:
                analyze_text_input()
                exit()
            elif option == 3:
                print('Thank you for using Text Analyzer. Shutting down...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')


def analyze_website():
    """
    Gives the user an input to enter a website URL that will be analyzed.
    """
    print('Let us look at the page')


def analyze_text_input():
    """
    Gives the user an input field to paste a chunk of text to be analyzed.
    """
    print('Paste your input')
  

"""
Run program
"""
print("Welcome to Text Analyzer")
print_menu()