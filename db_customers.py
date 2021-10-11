########################################
############## Modules #################
########################################

import sqlite3
import pandas as pd

########################################
############## Constants ###############
########################################

FIRST_NAME = 0
LAST_NAME = 1

EMAIL = 2
PHONE_NUMBER = 3

SUBSCRIPTION_PLAN = 4

PRIMARY_KEY = 5

########################################
############## Functions ###############
########################################

# Create a Table For the Customers.
def create_table() :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Create a Table.
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS
            customers (
                first_name text,
                last_name text,

                email_address text,
                phone_number text,

                subscription_plan text)
        """)

    # Commit our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Query the Customers Table and Return a Specific Record.
def show_single_record(key) :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Customers Table.
    cursor.execute(""" SELECT * FROM customers WHERE rowid = (?) """, [str(key)])
    customer_found = cursor.fetchall()

    # Commit Our Command and Close Our Connection.
    conn.commit()
    conn.close()

    return customer_found[0]

# Query the Customers Table and Return All Records Ordered by Specified Column.
def show_all_records(column_information) :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Customers Table.
    if (column_information == 'First Name') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY first_name""")
    elif (column_information == 'Last Name') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY last_name""")

    elif (column_information == 'Email Address') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY email_address""")
    elif (column_information == 'Phone Number') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY phone_number""")

    elif (column_information == 'Subscription Plan') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY subscription_plan""")

    else :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY rowid""")

    items = cursor.fetchall()

    name_column = []

    email_address_column = []
    phone_number_column = []

    subscription_plan_column = []

    key_column = []

    for current_item in range(len(items)) :
        name_column.append(items[current_item][FIRST_NAME] + ' ' + items[current_item][LAST_NAME])

        email_address_column.append(items[current_item][EMAIL])
        phone_number_column.append(items[current_item][PHONE_NUMBER])

        subscription_plan_column.append(items[current_item][SUBSCRIPTION_PLAN])

        key_column.append(str(items[current_item][PRIMARY_KEY]))

    # Convert the List To a Series For Each Column.
    name_series = pd.DataFrame(name_column)

    email_address_series = pd.DataFrame(email_address_column)
    phone_number_series = pd.DataFrame(phone_number_column)

    subscription_plan_series = pd.DataFrame(subscription_plan_column)

    key_series = pd.DataFrame(key_column)

    # Combine the Series Into a New DataFrame.
    combined_dataframe = pd.concat(
        [
            name_series,

            email_address_series,
            phone_number_series,

            subscription_plan_series,

            key_series
        ],
        axis = 1
    )

    combined_dataframe.columns = ['NAME', 'EMAIL', 'PHONE NUMBER', 'SUBSCRIPTION PLAN', 'KEY ID']

    # Close our Connection.
    conn.close()

    return combined_dataframe

# Query the Customers Table and Return All Primary Keys In Order.
def show_all_primary_keys() :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Customers Table.
    cursor.execute(""" SELECT rowid FROM customers ORDER BY rowid""")

    key_series = pd.DataFrame(cursor.fetchall())

    key_list = []
    for nested_list in key_series.to_numpy().tolist():
        for key in nested_list :
            key_list.append(key)

    # Close our Connection.
    conn.close()

    return key_list

# Add New Records To The Customers Table.
def add_records(first_name_new, last_name_new, email_address_new, phone_number_new, subscription_plan_new) :
    # Connect to database.
    conn = sqlite3.connect('company.db')
    # Create a cursor.
    cursor = conn.cursor()

    try :
        # Insert a Single Record Into Customers Table.
        cursor.execute(
            """ INSERT INTO customers VALUES (?, ?, ?, ?, ?) """,
            (first_name_new, last_name_new, email_address_new, phone_number_new, subscription_plan_new)
        )

        # Commit Our Command.
        conn.commit()
    except Exception as manyCustomers :
        new_customers = []

        for i in range(len(first_name_new)) :
            new_customers.append(
                (
                    first_name_new[i],
                    last_name_new[i],

                    email_address_new[i],
                    phone_number_new[i],

                    subscription_plan_new[i]
                )
            )

        # Insert Many Records Into Database.
        cursor.executemany(
            """ INSERT INTO customers VALUES (?, ?, ?, ?, ?) """,
            (new_customers)
        )

        # Commit Our Command.
        conn.commit()
    finally :
        # Close Our Connection.
        conn.close()

# Change the Information Regarding a Specific Customer.
def change_single_record(key, first_name_new, last_name_new, email_address_new, phone_number_new, subscription_plan_new) :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Customers Table.
    cursor.execute(
        """ UPDATE customers SET
            first_name = :first_name,
            last_name = :last_name,

            email_address = :email_address,
            phone_number = :phone_number,

            subscription_plan = :subscription_plan
            WHERE rowid = :key """, {
                'first_name' : first_name_new,
                'last_name' : last_name_new,

                'email_address' : email_address_new,
                'phone_number' : phone_number_new,

                'subscription_plan' : subscription_plan_new,

                'key' : str(key)
            }
    )

    # Commit our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Delete a Record From The Customers Table.
def delete_record(key) :
    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    cursor.execute(""" DELETE from customers WHERE rowid = (?) """, [str(key)])

    # Commit Our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Return The Number of Customers In The Table.
def number_of_records() :
    try :
        return len(show_all_records('Primary Key').index)
    except Exception as NoCustomers :
        return 0

def print_record(key) :
    customer_information = show_single_record(key)

    print('First Name : ', customer_information[FIRST_NAME])
    print('Last Name : ', customer_information[LAST_NAME])

    print('Email Address : ', customer_information[EMAIL])
    print('Phone Number : ', customer_information[PHONE_NUMBER])

    print('Subscription Plan : ', customer_information[SUBSCRIPTION_PLAN] + '\n')

def test_script() :
    # Create the Table.
    create_table()

    # Add a Customer to the Table.
    add_records(
        'Muntakim', # First Name
        'Rahman', # Last Name

        'muntakim.rahman@gmail.com', # Email Address
        '647-907-8430', # Phone Number

        'Basic' # Subscription Plan
    )

    print(str(show_all_records('First Name')) + '\n')

    print('**Added 1 Customer**')
    print_record(key = 1)

    print('There is ' + str(number_of_records()) + ' customer in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    # Add Three Customers To The Table.
    add_records(
        ['Janice', 'Jim', 'Apple', 'Happy'], # First Names
        ['Morison', 'Johns', 'Bee', 'Wilson'], # Last Names

        ['Janice@gmail.com', 'jimmy@gmail.com', 'honeybee@gmail.com', 'hw@yahoo.com'], # Email Addresses
        ['555-222-2323', '255-212-4442', '735-212-2573', '565-857-2323'], # Phone Numbers

        ['Premium', 'Premium', 'Basic', 'Premium'] # Subscription Plans
    )

    print('**Added 3 Customers**')

    print('Current Customers in Table (Arranged by Key ID) :')
    print(str(show_all_records('Gibberish')) + '\n')

    print('There are ' + str(number_of_records()) + ' customers in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    print_record(key = 3)

    # Modify AB's Data in Table.
    change_single_record(
        4, # Key ID
        'Abby', # First Name
        'Bumblebee', # Last Name
        'AB@gmail.com', # Email Address
        '823-232-4848', # Phone Number
        'Premium' # Subscription Plan
    )

    print('**Changed Apple Bee Name and Email Address**')
    print_record(key = 4)

    # Delete AB From The Table.
    delete_record(key = 4)

    print('**Removed AB**')
    print('Current Customers in Table (Arranged by Email) :')
    print(str(show_all_records('Email Address')) + '\n')

    print('There are ' + str(number_of_records()) + ' customers in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

## Test the Functionality of the Python Script.
## test_script()