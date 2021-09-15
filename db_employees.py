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

DEPARTMENT = 4
ROLE = 5
MONTHLY_WAGE = 6

PRIMARY_KEY = 7

key_list = []

########################################
############## Functions ###############
########################################

# Function to Remove List Nestings. This is Used to
# Acquire the Current Primary Keys in the Table.
def remove_nestings(nested_list) :

    for item in nested_list :
        if type(item) == list :
            remove_nestings(item)
        else :
            key_list.append(item)

# Create a Table For the Employees.
def create_table() :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Create a Table.
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS
            employees (
                first_name text,
                last_name text,

                email_address text,
                phone_number text,

                department text,
                role text,
                monthly_wage real)
        """)

    # Commit our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Query the Employees Table and Return a Specific Record.
def show_single_record(key) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Employees Table.
    cursor.execute(""" SELECT * FROM employees WHERE rowid = (?) """, [str(key)])
    employee_found = cursor.fetchall()

    # Commit Our Command and Close Our Connection.
    conn.commit()
    conn.close()

    return employee_found[0]

# Query the Employees Table and Return All Records Ordered by Specified Column.
def show_all_records(column_information) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Employees Table.
    if (column_information == 'First Name') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY first_name""")
    elif (column_information == 'Last Name') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY last_name""")

    elif (column_information == 'Email Address') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY email_address""")
    elif (column_information == 'Phone Number') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY phone_number""")

    elif (column_information == 'Department') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY department""")
    elif (column_information == 'Role') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY role""")
    elif (column_information == 'Monthly Wage') :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY monthly_wage DESC""")

    else :
        cursor.execute(""" SELECT *, rowid FROM employees ORDER BY rowid""")

    items = cursor.fetchall()

    name_column = []

    email_address_column = []
    phone_number_column = []

    department_column = []
    role_column = []
    monthly_wage_column = []

    key_column = []

    for current_item in range(len(items)) :
        name_column.append(items[current_item][FIRST_NAME] + ' ' + items[current_item][LAST_NAME])

        email_address_column.append(items[current_item][EMAIL])
        phone_number_column.append(items[current_item][PHONE_NUMBER])

        department_column.append(items[current_item][DEPARTMENT])
        role_column.append(items[current_item][ROLE])
        monthly_wage_column.append(items[current_item][MONTHLY_WAGE])

        key_column.append(str(items[current_item][PRIMARY_KEY]))

    # Convert the List To a Series For Each Column.
    name_series = pd.DataFrame(name_column)

    email_address_series = pd.DataFrame(email_address_column)
    phone_number_series = pd.DataFrame(phone_number_column)

    department_series = pd.DataFrame(department_column)
    role_series = pd.DataFrame(role_column)
    monthly_wage_series = pd.DataFrame(monthly_wage_column)

    key_series = pd.DataFrame(key_column)

    # Combine the Series Into a New DataFrame.
    combined_dataframe = pd.concat(
        [
            name_series,

            email_address_series,
            phone_number_series,

            department_series,
            role_series,
            monthly_wage_series,

            key_series
        ],
        axis = 1
    )

    combined_dataframe.columns = [
        'NAME',
        'EMAIL',
        'PHONE NUMBER',
        'DEPARTMENT',
        'ROLE',
        'MONTHLY WAGE',
        'KEY ID'
    ]

    # Close our Connection.
    conn.close()

    return combined_dataframe

# Query the Employees Table and Return All Primary Keys In Order.
def show_all_primary_keys() :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Employees Table.
    cursor.execute(""" SELECT rowid FROM employees ORDER BY rowid""")

    key_series = pd.DataFrame(cursor.fetchall())
    key_nested_list = key_series.values.tolist()

    # Reinitialize the List of Primary Keys.
    global key_list
    key_list = []

    remove_nestings(key_nested_list)
    key_tuple = tuple(key_list)

    # Close our Connection.
    conn.close()

    return key_tuple

# Add New Records To The Employees Table.
def add_records(first_name_new, last_name_new, email_address_new,
    phone_number_new, department_new, role_new, monthly_wage_new) :

    # Connect to database.
    conn = sqlite3.connect('company.db')
    # Create a cursor.
    cursor = conn.cursor()

    try :
        # Insert a Single Record Into Employees Table.
        cursor.execute(
            """ INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?) """,
            (
                first_name_new,
                last_name_new,

                email_address_new,
                phone_number_new,

                department_new,
                role_new,
                monthly_wage_new
            )
        )

        # Commit Our Command.
        conn.commit()
    except Exception as manyEmployees :
        new_employees = []

        for i in range(len(first_name_new)) :
            new_employees.append(
                (
                    first_name_new[i],
                    last_name_new[i],

                    email_address_new[i],
                    phone_number_new[i],

                    department_new[i],
                    role_new[i],
                    monthly_wage_new[i]
                )
            )

        # Insert Many Records Into Database.
        cursor.executemany(
            """ INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?) """,
            (new_employees)
        )

        # Commit Our Command.
        conn.commit()
    finally :
        # Close Our Connection.
        conn.close()

# Change the Information Regarding a Specific Employee.
def change_single_record(key, first_name_new, last_name_new, email_address_new,
    phone_number_new, department_new, role_new, monthly_wage_new) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Employees Table.
    cursor.execute(
        """ UPDATE employees SET
            first_name = :first_name,
            last_name = :last_name,

            email_address = :email_address,
            phone_number = :phone_number,

            department = :department,
            role = :role,
            monthly_wage = :monthly_wage
            WHERE rowid = :key """, {
                'first_name' : first_name_new,
                'last_name' : last_name_new,

                'email_address' : email_address_new,
                'phone_number' : phone_number_new,

                'department' : department_new,
                'role' : role_new,
                'monthly_wage' : monthly_wage_new,

                'key' : str(key)
            }
    )

    # Commit our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Delete a Record From The Employees Table.
def delete_record(key) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    cursor.execute(""" DELETE from employees WHERE rowid = (?) """, str(key))

    # Commit Our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Return The Number of Employees In The Table.
def number_of_records() :

    try :
        return len(show_all_records('Primary Key').index)
    except Exception as NoEmployees :
        return 0

def print_record(key) :

    employee_information = show_single_record(key)

    print('First Name : ', employee_information[FIRST_NAME])
    print('Last Name : ', employee_information[LAST_NAME])
    print('Email Address : ', employee_information[EMAIL])
    print('Phone Number : ', employee_information[PHONE_NUMBER])
    print('Department : ', employee_information[DEPARTMENT])
    print('Role : ', employee_information[ROLE])
    print('Monthly Wage : ', str(employee_information[MONTHLY_WAGE]) + '\n')

def test_script() :
    # Create the Table.
    create_table()

    # Add an Employee to the Table.
    add_records(
        'Jordan', # First Name
        'Leonel', # Last Name

        'jordan@gmail.com', # Email Address
        '213-333-4340', # Phone Number

        'Corporate', # Department
        'CEO', # Role
        10000.32 # Monthly Wage
    )

    print(str(show_all_records('First Name')) + '\n')


    print('**Added 1 Employee**')
    print_record(key = 1)

    print('There is ' + str(number_of_records()) + ' employee in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    # Add 4 Employees To The Table.
    add_records(
        ['Janice', 'Jim', 'Irina', 'Oliver'], # First Names
        ['Morison', 'Johns', 'Polish', 'Wilson'], # Last Names
        ['Janice@gmail.com', 'jimmy@gmail.com', 'i_polish@gmail.com', 'oliver@yahoo.com'], # Email Addresses
        ['555-222-2323', '255-212-4442', '735-212-2573', '565-857-2323'], # Phone Numbers
        ['Corporate', 'Sales', 'Engineering', 'Human Resources'], # Departments
        ['CFO', 'Salesperson', 'Technical Advisor', 'Manager'], # Roles
        [8000.21, 2320.21, 5000.32, 4000.45] # Monthly Wages
    )

    print('**Added 3 Employees**')
    print('Current Employees in Table (Arranged by Department) :')
    print(str(show_all_records('Department')) + '\n')

    print('There are ' + str(number_of_records()) + ' employees in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    print('JJ Current Data :')
    print_record(key = 3)

    # Modify Irina's Data in Table.
    change_single_record(
        4, # Key ID
        'Irina', # First Name
        'Irish', # Last Name
        'i_irish@gmail.com', # Email Address
        '823-232-4848', # Phone Number
        'Engineering', # Department
        'Research Lead', # Role
        7000.54 # Wage
    )

    print('**Changed Irina Information**')
    print('Irina New Data :')
    print_record(key = 4)

    # Delete Oliver From The Table.
    delete_record(key = 5)

    print('**Removed Oliver**')
    print('Current Employees in Table (Arranged by Key ID) :')
    print(str(show_all_records('Garbage')) + '\n')

    print('Current Employees in Table (Arranged by Monthly Wage) :')
    print(str(show_all_records('Monthly Wage')) + '\n')

    print('There are ' + str(number_of_records()) + ' employees in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

## Test the Functionality of the Python Script.
## test_script()