import sqlite3
import pandas as pd

# Create a table.
def create_table_customers() :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Create a table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            first_name text,
            last_name text,
            email_address text)
        """)

    # Commit our command and close our connection.
    conn.commit()
    conn.close()

# Query the database and return all records ordered by specified column.
def show_records_all_customers(column_information) :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Query the database.
    if (column_information == 'First Name') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY first_name""")
    elif (column_information == 'Last Name') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY last_name""")
    elif (column_information == 'Email Address') :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY email_address""")
    else :
        cursor.execute(""" SELECT *, rowid FROM customers ORDER BY rowid""")

    items = cursor.fetchall()

    name_column = []
    email_address_column = []
    key_column = []

    for item in range(len(items)) :
        name_column.append(items[item][0] + ' ' + items[item][1])
        email_address_column.append(items[item][2])
        key_column.append(str(items[item][3]))

        ## Print item appended to column lists to screen. - > Mainly for debugging purposes.
        ## print ('*Item Added*')
        ## print('Name Column Item: ' + str(name_column[item]))
        ## print('Email_Address Column Item: ' + str(email_address_column[item]))
        ## print('Primary Key Item: ' + str(key_column[item]) + '\n')

    ## Print all column lists to screen. - > Mainly for debugging purposes.
    ## print ('*Lists Complete*')
    ## print('Name Column: ' + str(name_column) + '\n')
    ## print('Email_Address Column: ' + str(email_address_column) + '\n')
    ## print('Primary Key: ' + str(key_column) + '\n\n')

    # Convert the list to a series for each column.
    name_series = pd.DataFrame(name_column)
    email_address_series = pd.DataFrame(email_address_column)
    key_series = pd.DataFrame(key_column)

    ## Print all series to screen. - > Mainly for debugging purposes.
    ## print ('*Series Converted*')
    ## print('Name Series: ', str(name_series) + '\n')
    ## print('Email_Address Column: ' + str(email_address_series) + '\n')
    ## print('Primary Key: ' +str(key_series) + '\n\n')

    # Combine the series into a new dataframe.
    combined_dataframe = pd.concat([name_series, email_address_series, key_series], axis = 1)
    combined_dataframe.columns = ['NAME', 'EMAIL', 'PRIMARY KEY']

    ## Print records to screen. - > Mainly for debugging purposes.
    ## print('All Records :')
    ## print(combined_dataframe + '\n')

    # Close our connection.
    conn.close()

    return combined_dataframe

key_list = []
# Function to remove list nestings. This is used to
# acquire the current primary keys in the table.
def remove_nestings(nested_list) :
    for item in nested_list :
        if type(item) == list :
            remove_nestings(item)
        else :
            key_list.append(item)

# Query the database and return all primary keys in order.
def show_primary_keys_all_customers() :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Query the database.
    cursor.execute(""" SELECT rowid FROM customers ORDER BY rowid""")

    key_series = pd.DataFrame(cursor.fetchall())
    key_nested_list = key_series.values.tolist()

    # Reinitialize the list of primary keys.
    global key_list
    key_list = []

    remove_nestings(key_nested_list)
    key_tuple = tuple(key_list)

    ## Print primary keys to screen. - > Mainly for debugging purposes.
    ## print('Primary Keys :')
    ## print(key_tuple)
    ## print('\n')

    # Close our connection.
    conn.close()

    return key_tuple

# Query the database and return a specific record.
def show_record_specific_customer(key) :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Query the database.
    cursor.execute(""" SELECT * FROM customers WHERE rowid = (?) """, str(key))
    customer_found = cursor.fetchall()

    ## Print record to screen. - > Mainly for debugging purposes.
    ## print(customer_found)

    # Commit our command and close our connection.
    conn.commit()
    conn.close()

    return customer_found[0]

# Add new records to the table.
def add_records_customers(new_first_name, new_last_name, new_email_address) :
    ## Print parameters passed into function. - > Mainly for debugging purposes.]
    ## print('New Customer To Be Added :')
    ## print('First Name : ' + str(first_name_new))
    ## print('Last Name : ' + str(last_name_new))
    ## print('Email Address : ' + str(email_address_new) + '\n')

    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    try :
        # Insert a single record into database.
        cursor.execute(""" INSERT INTO customers VALUES (?, ?, ?) """,
            (new_first_name, new_last_name, new_email_address)
        )

        ## Print record added to screen. - > Mainly for debugging purposes.
        ## print('New Customer Added :')
        ## print('First Name : ' + first_name_new)
        ## print('Last Name : ' + last_name_new)
        ## print('Email Address : ' + email_address_new + '\n')

        # Commit our command.
        conn.commit()
    except Exception as manyCustomers :
        new_customers = []

        for i in range(len(new_first_name)) :
            new_customers.append((new_first_name[i], new_last_name[i], new_email_address[i]))
        ## Print record just added to screen. - > Mainly for debugging purposes.
        ## print('New Customer # ' + str(new_customer + 1) :')
        ## print('First Name : ' + str(new_customers[new_customer][0])')
        ## print('Last Name : ' + str(new_customers[new_customer][1])')
        ## print('Email Address : ' + str(new_customers[new_customer][2]) + '\n')

        ## Print records to be added to screen. - > Mainly for debugging purposes.
        ## print('All New Customers :')
        ## print(str(new_customers) + '\n')

        # Insert many records into database.
        cursor.executemany(""" INSERT INTO customers VALUES (?, ?, ?) """,
            (new_customers)
        )

        ## Print records added to screen. - > Mainly for debugging purposes.
        ## print(str(len(new_customers)) + 'Customers Added :')
        ## print(new_customers + '\n')

        # Commit our command.
        conn.commit()
    finally :
        # Close our connection.
        conn.close()

# Change the information regarding a specific customer.
def change_record_specific_customer(key, first_name_new, last_name_new, email_address_new) :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Query the database.
    cursor.execute(""" UPDATE customers SET
            first_name = :first_name,
            last_name = :last_name,
            email_address = :email_address
            WHERE rowid = :key """,

            {
                'first_name' : first_name_new,
                'last_name' : last_name_new,
                'email_address' : email_address_new,
                'key' : str(key)
            }
        )

    # Commit our command and close our connection.
    conn.commit()
    conn.close()

# Delete a record from the table.
def delete_record_customer(key) :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    cursor.execute(""" DELETE from customers WHERE rowid = (?) """, str(key))

    # Commit our command and close our connection.
    conn.commit()
    conn.close()

# Return the number of customers in the table.
def number_of_customers() :
    try :
        customer_count = len(show_records_all_customers('Primary Key').index)
        return customer_count
    except Exception as NoCustomers :
        return 0

def test_database() :
    # Create the table.
    create_table_customers()

    # Add a customer to the table.
    add_records_customers('Muntakim', 'Rahman', 'muntakim.rahman@gmail.com')

    print('**Added 1 Customer**')
    print(str(show_records_all_customers('First Name')) + '\n')
    muntakim_information = show_record_specific_customer(1)
    print('First Name : ', muntakim_information[0])
    print('Last Name : ', muntakim_information[1])
    print('Email Address : ', muntakim_information[2] + '\n')

    print('There is ' + str(number_of_customers()) + ' customer in the table.\n')
    print('Keys in Order : ', show_primary_keys_all_customers())


    # Add three customers to the table.
    add_records_customers(
        ['Janice', 'Jim', 'Apple', 'Happy'],
        ['Morison', 'Johns', 'Bee', 'Wilson'],
        ['Janice@gmail.com', 'jimmy@gmail.com', 'honeybee@gmail.com', 'hw@yahoo.com']
    )

    print('**Added 3 Customers**')
    print('Current Customers in Table (Arranged by Primary Key) :')
    print(str(show_records_all_customers('Gibberish')) + '\n')

    print('There are ' + str(number_of_customers()) + ' customers in the table.\n')
    print('Keys in Order : ', show_primary_keys_all_customers())

    print('JJ Current Data :')
    jj_information = show_record_specific_customer(3)
    print('First Name : ', jj_information[0])
    print('Last Name : ', jj_information[1])
    print('Email Address : ', jj_information[2] + '\n')

    # Modify JJ's data in table.
    change_record_specific_customer(3, 'Jimminy', 'John', 'JJ@gmail.com')

    print('**Changed JJ Name and Email Address**')
    print('JJ New Data :')
    jj_first_name, jj_last_name, jj_email_address = (show_record_specific_customer(3))
    print('First Name : ', jj_first_name)
    print('Last Name : ', jj_last_name)
    print('Email Address : ', jj_email_address + '\n')

    # Delete JJ from the table.
    delete_record_customer(3)

    print('**Removed JJ**')
    print('Current Customers in Table (Arranged by Email) :')
    print(str(show_records_all_customers('Email Address')) + '\n')

    print('There are ' + str(number_of_customers()) + ' customers in the table.\n')
    print('Keys in Order : ', show_primary_keys_all_customers())

## Test the functionality of the Python script.
test_database()