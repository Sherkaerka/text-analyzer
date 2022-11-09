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
SHEET = GSPREAD_CLIENT.open('text_analyzer')


def print_menu():
    """
    Prints the menu so that the user can choose what they want to do. 
    """
    menu_options = {
        1: 'Add contact',
        2: 'Print all contacts',
        3: 'Search contact',
        4: 'Remove contact',
        5: 'Exit',
    }

    def print_menu_options():
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )

    if __name__=='__main__':
        while(True):
            print('---Main menu---')
            print_menu_options()
            option = ''
            try:
                option = int(input('What do you want to do: '))
            except:
                print('Invalid input. Please enter a number.')
            
            if option == 1:
                add_contact()
            elif option == 2:
                print_all_contacts()
            elif option == 3:
                search_contact()
            elif option == 4:
                remove_contact()
            elif option == 5:
                print('Thank you for using Text Analyzer CRM. Shutting down...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')


def add_contact():
    """
    Creates a new customer record with contact details.
    """
    print('Add new customer record')
    
    company = input('Enter Company Name: ')
    name = input('Enter Name of contact: ')
    email = input('Enter e-mail: ')
    phone = input('Enter phone number: ')
    sheet1 = SHEET.worksheet('sheet1')
    sheet1.append_row([company, name, email, phone])
    print( "New Customer record added successfully!")

def print_all_contacts():
    """
    Prints all contacts in the CRM to the terminal.
    """
    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    print(data)
  

def search_contact():
    """
    Let user search within the customer database and returns
    """
    search_for = input('What or whom are you looking for: \n')

    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    
    for list in data:
        if search_for in list:
            print(list)
            print_menu()
        else:
            print('No record found')
            print_menu()

def remove_contact():
    """
    Prints all contacts in the CRM to the terminal.
    """
    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    
    for i in enumerate(data):
        print(i)
        
    edit_list = input('Enter index on record you want to delete: \n')
    actual_row = int(edit_list) + 1
    sheet1.delete_rows(actual_row)


"""
Run program
"""
print("Welcome to Text Analyzer Inc. CRM-system")
print_menu()