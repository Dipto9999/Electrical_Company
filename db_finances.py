########################################
############## Modules #################
########################################

import sqlite3
import pandas as pd

########################################
############## Constants ###############
########################################

DATE = 0

MONTHLY_REVENUE = 1
MONTHLY_EXPENDITURES = 2
MONTHLY_NET_INCOME = 3
TOTAL_BALANCE = 4

NUMBER_OF_CUSTOMERS = 5
NUMBER_OF_EMPLOYEES = 6
NUMBER_OF_DEPARTMENTS = 7

PRIMARY_KEY = 8

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

# Create a Table For the Finances.
def create_table() :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Create a Table.
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS
            finances (
                date text,

                monthly_revenue real,
                monthly_expenditures real,
                monthly_net_income real,
                total_balance real,

                number_of_customers int,
                number_of_employees int,
                number_of_departments int)
        """)

    # Commit our Command and Close Our Connection.
    conn.commit()
    conn.close()

# Query the Finances Table and Return a Record for a Specific Date.
def show_single_record(key) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Finances Table.
    cursor.execute(""" SELECT * FROM finances WHERE rowid = (?) """, [str(key)])
    record_found = cursor.fetchall()

    # Commit Our Command and Close Our Connection.
    conn.commit()
    conn.close()

    return record_found[0]

# Query the Finances Table and Return All Records Ordered by Specified Column.
def show_all_records(column_information) :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Finances Table.
    if (column_information == 'Date') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY date""")

    elif (column_information == 'Monthly Revenue') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY monthly_revenue DESC""")
    elif (column_information == 'Monthly Expenditures') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY monthly_expenditures DESC""")
    elif (column_information == 'Monthly Net Income') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY monthly_net_income DESC""")
    elif (column_information == 'Total Balance') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY total_balance DESC""")

    elif (column_information == 'Number of Customers') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY number_of_customers DESC""")
    elif (column_information == 'Number of Employees') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY number_of_employees DESC""")
    elif (column_information == 'Number of Departments') :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY number_of_departments DESC""")
    else :
        cursor.execute(""" SELECT *, rowid FROM finances ORDER BY rowid""")

    items = cursor.fetchall()

    date_column = []

    monthly_revenue_column = []
    monthly_expenditures_column = []
    monthly_net_income_column = []
    total_balance_column = []

    number_of_customers_column = []
    number_of_employees_column = []
    number_of_departments_column = []

    key_column = []

    for current_item in range(len(items)) :
        date_column.append(items[current_item][DATE])

        monthly_revenue_column.append(items[current_item][MONTHLY_REVENUE])
        monthly_expenditures_column.append(items[current_item][MONTHLY_EXPENDITURES])
        monthly_net_income_column.append(items[current_item][MONTHLY_NET_INCOME])
        total_balance_column.append(items[current_item][TOTAL_BALANCE])

        number_of_customers_column.append(items[current_item][NUMBER_OF_CUSTOMERS])
        number_of_employees_column.append(items[current_item][NUMBER_OF_EMPLOYEES])
        number_of_departments_column.append(items[current_item][NUMBER_OF_DEPARTMENTS])

        key_column.append(str(items[current_item][PRIMARY_KEY]))

    # Convert the List To a Series For Each Column.
    date_series = pd.DataFrame(date_column)

    monthly_revenue_series = pd.DataFrame(monthly_revenue_column)
    monthly_expenditures_series = pd.DataFrame(monthly_expenditures_column)
    monthly_net_income_series = pd.DataFrame(monthly_net_income_column)
    total_balance_series = pd.DataFrame(total_balance_column)

    number_of_customers_series = pd.DataFrame(number_of_customers_column)
    number_of_employees_series = pd.DataFrame(number_of_employees_column)
    number_of_departments_series = pd.DataFrame(number_of_departments_column)

    key_series = pd.DataFrame(key_column)

    # Combine the Series Into a New DataFrame.
    combined_dataframe = pd.concat(
        [
            date_series,

            monthly_revenue_series,
            monthly_expenditures_series,
            monthly_net_income_series,
            total_balance_series,

            number_of_customers_series,
            number_of_employees_series,
            number_of_departments_series,

            key_series
        ],
        axis = 1
    )

    combined_dataframe.columns = [
        'DATE',

        'MONTHLY REVENUE',
        'MONTHLY EXPENDITURES',
        'MONTHLY NET INCOME',
        'TOTAL BALANCE',

        'NUMBER OF CUSTOMERS',
        'NUMBER OF EMPLOYEES',
        'NUMBER OF DEPARTMENTS',

        'KEY ID'
    ]

    # Close our Connection.
    conn.close()

    return combined_dataframe

# Query the Finances Table and Return All Primary Keys In Order.
def show_all_primary_keys() :

    # Connect to Database.
    conn = sqlite3.connect('company.db')
    # Create a Cursor.
    cursor = conn.cursor()

    # Query the Finances Table.
    cursor.execute(""" SELECT rowid FROM finances ORDER BY rowid""")

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

# Add New Records To The Finances Table.
def add_records(date_new,
    monthly_revenue_new, monthly_expenditures_new, monthly_net_income_new, total_balance_new,
    current_number_of_customers, current_number_of_employees, current_number_of_departments) :

    # Connect to database.
    conn = sqlite3.connect('company.db')
    # Create a cursor.
    cursor = conn.cursor()

    try :
        # Insert a Single Record Into Finances Table.
        cursor.execute(
            """ INSERT INTO finances VALUES (?, ?, ?, ?, ?, ?, ?, ?) """,
            (
                date_new,

                monthly_revenue_new,
                monthly_expenditures_new,
                monthly_net_income_new,
                total_balance_new,

                current_number_of_customers,
                current_number_of_employees,
                current_number_of_departments
            )
        )

        # Commit Our Command.
        conn.commit()
    # Should Not Be Allowed to Add More Than One Record At Once.
    except Exception as manyRecords :
        cursor.execute(
            """ INSERT INTO finances VALUES (?, ?, ?, ?, ?, ?, ?, ?) """,
            (
                date_new[0],

                monthly_revenue_new[0],
                monthly_expenditures_new[0],
                monthly_net_income_new[0],
                total_balance_new[0],

                current_number_of_customers[0],
                current_number_of_employees[0],
                current_number_of_departments[0]
            )
        )

        # Commit Our Command.
        conn.commit()
    finally :
        # Close Our Connection.
        conn.close()

# Return The Number of Records In The Table.
def number_of_records() :

    try :
        return len(show_all_records('Primary Key').index)
    except Exception as NoRecords :
        return 0

def print_record(key) :

    record_information = show_single_record(key)

    print('Date : ', record_information[DATE])

    print('Monthly Revenue : ', str(record_information[MONTHLY_REVENUE]))
    print('Monthly Expenditures : ', str(record_information[MONTHLY_EXPENDITURES]))
    print('Monthly Net Income : ', str(record_information[MONTHLY_NET_INCOME]))
    print('Total Balance : ', str(record_information[TOTAL_BALANCE]))

    print('Number of Customers : ', str(record_information[NUMBER_OF_CUSTOMERS]))
    print('Number of Employees : ', str(record_information[NUMBER_OF_EMPLOYEES]))
    print('Number of Departments : ', str(record_information[NUMBER_OF_DEPARTMENTS]) + '\n')

def test_script() :

    # Create the Table.
    create_table()

    # Add a Record to the Table.
    add_records(
        '2021-01-01', # Date

        500.12, # Monthly Revenue
        800.23, # Monthly Expenditures
        -300.21, # Monthly Net Income
        -300.21, # Total Blance

        80, # Number of Customers
        42, # Number of Employees
        4 # Number of Departments
    )

    print(str(show_all_records('Date')) + '\n')

    print('**Added 1 Record**')
    print_record(key = 1)

    print('There is ' + str(number_of_records()) + ' record in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    # Try To Add 3 Records To The Table. (Only 1 Record Should Be Added.)
    add_records(
        ['2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'], # Dates
        [1332.21, 4444.23, 3323.21, 5221.23], # Monthly Revenue
        [1532.21, 2444.23, 3523.21, 3221.23], # Monthly Expenditures
        [-200.00, 2000.00, -200.00, 2000.00], # Monthly Net Income
        [-500.21, 1499.79, 1299.79, 3299.79], # Total Balance
        [201, 103, 345, 500], # Number of Customers
        [54, 55, 123, 65], # Number of Employees
        [5, 4, 5, 5]  # Number of Departments
    )

    print('**Added 1 New Record**')
    print('Current Records in Table (Arranged by Monthly Net Income) :')
    print(str(show_all_records('Monthly Net Income')) + '\n')

    print('There are ' + str(number_of_records()) + ' employees in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    # Add Another Record To The Table.
    add_records(
        '2021-03-01', # Date

        4444.23, # Monthly Revenue
        2444.23, # Monthly Expenditures
        2000.00, # Monthly Net Income
        1499.79, # Total Balance

        103, # Number of Customers
        55, # Number of Employees
        4 # Number of Departments
    )

    print('**Added 1 New Record**')
    print('Current Records in Table (Arranged by Number of Customers) :')
    print(str(show_all_records('Number of Customers')) + '\n')

    print('Current Records in Table (Arranged by Monthly Net Income) :')
    print(str(show_all_records('Monthly Net Income')) + '\n')

    print('There are ' + str(number_of_records()) + ' employees in the table.\n')
    print('Keys in Order : ', str(show_all_primary_keys()) + '\n')

    print('Record 2 Data :')
    print_record(key = 2)

## Test the Functionality of the Python Script.
## test_script()