import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('star_crm')


# try connection to sheet



def print_menu():
    """
    Prints the menu so that the user can choose what they want to do. 
    """
    menu_options = {
        1: 'Add contact',
        2: 'Print all contacts',
        3: 'Search contact',
        4: 'Exit',
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
                add_contact()
                exit()
            elif option == 2:
                print_all_contacts()
                exit()
            elif option == 3:
                search_contact()
                exit()
            elif option == 4:
                print('Thank you for using Text Analyzer. Shutting down...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')


def add_contact():
    """
    Gives the user an input to enter a website URL that will be analyzed.
    """
    print('Add new customer record')
    
    first = input('Enter First Name: ')
    company = input('Enter Company Name: ')
    sheet1 = SHEET.worksheet('sheet1')
    sheet1.append_row([first, company])
    print( "Added successfully!")


def print_all_contacts():
    """
    Gives the user an input field to paste a chunk of text to be analyzed.
    """
    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    print(data)
  

def search_contact():
    """
    Let user search
    """
    print('let us look what we got')

"""
Run program
"""
print("Welcome to Text Analyzer")
print_menu()