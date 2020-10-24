# Python3
# backend.py

# The user to upload their debits
    # Enter the item, $ amount, date
    # The backend can allocate the items into categories
# The user to be able to upload their credits
    # $amount, date, item -> where it came from

import sys
import sqlite3

def create_table():
    pass

def insert_date():
    pass

def update_data():
    pass

def view_data():
    pass

def delete_data():
    pass

def main(dev_mode, item, amount, debit_credit, date):


    return item, amount, debit_credit, date






if __name__ == "__main__":
    # This code block is for the developer switch
    try:
        flag = sys.argv[1]  # This will establish a command line argument as a variable
        if flag == '-d':
            dev_mode = 1  # 1 being on, 0 being off
    except Exception as e:
        dev_mode = 0

    item = input("What is the item? ")
    item = str(item)
    item = item.lower()

    amount = input("What is the amount? ")
    amount = float(amount) # Make sure this goes to second decimal place

    debit_credit = input("Is this a debit or credit? ")
    debit_credit = str(debit_credit)
    debit_credit = debit_credit.lower()  # To make sure the input it exactly either debit or credit
    if debit_credit != 'debit' or debit_credit != 'credit':
        print("This input has to be debit or credit.")
        sys.exit(0)
    else:
        pass


    date = input("what is the date? ")
    date = str(date) # This is a proper date MM/DD/YYYY

    x = main(dev_mode, item, amount, debit_credit, date)
    print(x)


 
    

