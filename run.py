import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

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
    Prints the menu so that the user can choose what 
    they want to do. 
    """
    
    menu_options = {
        1: 'Add contact',
        2: 'Print all contacts',
        3: 'Search contact',
        4: 'Edit contact',
        5: 'Remove contact',
        6: 'Exit',
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
                option = int(input('What do you want to do: \n'))
            except:
                print('Invalid input. Please enter a number.')
            
            if option == 1:
                add_contact()
            elif option == 2:
                print_all_contacts()
            elif option == 3:
                search_contact()
            elif option == 4:
                edit_contact()
            elif option == 5:
                remove_contact()
            elif option == 6:
                print('Thank you for using Text Analyzer CRM. Shutting down...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 6.')


def add_contact():
    """
    Creates a new customer record with contact details.
    """
    print('Add new customer record')
    
    company = input('Enter Company Name: \n')
    fname = input('Enter First name of contact: \n')
    lname = input('Enter Last name of contact: \n')
    email = input('Enter e-mail: \n')
    phone = input('Enter phone number: \n')
    sheet1 = SHEET.worksheet('sheet1')
    sheet1.append_row([company, fname, lname, email, phone])
    print( "New Customer record added successfully!")

def print_all_contacts():
    """
    Tabulates and print all contacts in the CRM to 
    the terminal.
    """
    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    
    print(tabulate(data))
  

def search_contact():
    """
    Let user search within the customer database and 
    returns the row or rows with a match. 
    """
    search_for = input('Search for any input in the contacts: \n')
    if search_for == "":
        print('Please give input')
        search_contact()

    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()
    
    for list in data:
        if search_for in list:
            print(tabulate([list], headers= ["Company","First name","Last name", "Email", "Phone"]))


    search_result = input('Do you wanna search again? y/n: \n')

    if search_result == 'y':
        search_contact()
    else:
        print_menu()



def edit_contact():
    """
    Use search function based on Company name. 
    Retrieves row number and ask for wich index user wish to edit. 
    Ask user wich data to be adjusted and the update specific cell.
    """
    
    
    search_for = str(input('Search for Company name: \n'))
    if search_for == "":
        print('Please give input')
        edit_contact()

    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()

    for list in data:
        if search_for in list:
            company_col = sheet1.col_values(1)
            rownum = company_col.index(search_for) + 1
            row = sheet1.row_values(rownum)
            print(rownum, row) 

    search_result = input('Do you wanna [s] search again or [c] continue or [x]exit? s/c/x: \n')

    if search_result == 's':
        edit_contact()
    elif search_result == 'x':
        print_menu()
    

    edit_list = input('Enter index on record you want to edit or [x] to exit to main menu: \n')
    
    if edit_list == "":
        print('Please give input')
        edit_contact()
    elif edit_list == 'x':
        print_menu()
    

    actual_row = int(edit_list)
    
    if actual_row != rownum:    
        print('You are trying to edit another record')
        print_menu()


    edit_menu = {
        1: 'Company name',
        2: 'First name',
        3: 'Last name',
        4: 'Email',
        5: 'Phone',
        6: 'Exit',
    }
        
    def print_edit_menu():
        for key in edit_menu.keys():
            print (key, '--', edit_menu[key] )

    if __name__=='__main__':
        while(True):
            print('---Edit menu---')
            print_edit_menu()
            option = ''
            try:
                option = int(input('What do you want to edit: \n'))
            except:
                print('Invalid input. Please enter a number.')
            
            if option == 1:
                new_input = input('Please enter new input: \n')
                col = 'A'
                cell = col + str(actual_row)
                sheet1.update(cell, new_input)
                print('Company record updated successfully')
                print_menu()
            elif option == 2:
                new_input = input('Please enter new input: \n')
                col = 'B'
                cell = col + str(actual_row)
                sheet1.update(cell, new_input)
                print('First name record updated successfully')
                print_menu()
            elif option == 3:
                new_input = input('Please enter new input: \n')
                col = 'C'
                cell = col + str(actual_row)
                sheet1.update(cell, new_input)
                print('Last name record updated successfully')
                print_menu()
            elif option == 4:
                new_input = input('Please enter new input: \n')
                col = 'D'
                cell = col + str(actual_row)
                sheet1.update(cell, new_input)
                print('Email record updated successfully')
                print_menu()
            elif option == 5:
                new_input = input('Please enter new input: \n')
                col = 'E'
                cell = col + str(actual_row)
                sheet1.update(cell, new_input)
                print('Phone record updated successfully')
                print_menu()
            elif option == 6:
                print('Thank you for using Text Analyzer CRM. Shutting down...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 6.')

    

def remove_contact():
    """
    Use search function based on Company name. Retrieves row number 
    and ask for wich index user wish to delete.
    """

    search_for = str(input('Search for Company name: \n'))
    if search_for == "":
        print('Please give input')
        edit_contact()

    sheet1 = SHEET.worksheet('sheet1')
    data = sheet1.get_all_values()

    for list in data:
        if search_for in list:
            company_col = sheet1.col_values(1)
            rownum = company_col.index(search_for) + 1
            row = sheet1.row_values(rownum)
            print(rownum, row) 

    search_result = input('Do you wanna [s] search again or [c] continue or [x]exit? s/c/x: \n')

    if search_result == 's':
        remove_contact()
    elif search_result == 'x':
        print_menu()
    

    edit_list = input('Enter index on record you want to remove or [x] to exit to main menu: \n')
    
    if edit_list == "":
        print('Please give input')
        remove_contact()
    elif edit_list == 'x':
        print_menu()
    

    actual_row = int(edit_list)
    
    if actual_row != rownum:    
        print('You are trying to edit another record')
        print_menu()
    elif actual_row == rownum:
        sheet1.delete_rows(actual_row)
        print("Contact removed successfully")
    elif actual_row == 9:
        print_menu()
    else:
        print('You are trying to remove another record')
     

"""
Run program
"""
print("Welcome to Text Analyzer Inc. CRM-system")
print_menu()