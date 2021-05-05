import sqlite3
import pandas as pd

# Create a table.
def create_table() :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Create a table.
    cursor.execute("""
        CREATE TABLE customers (
            first_name text,
            last_name text,
            email_address text)
        """)

    # Commit our command.
    conn.commit()

    # Close our connection.
    conn.close()


# Query the database and return all records
def show_records_all() :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    # Query the database.
    cursor.execute(""" SELECT rowid, * FROM customers """)
    items = cursor.fetchall()

    key_column = []
    name_column = []
    email_address_column = []

    for item in items :
        key_column.append(str(item[0]))
        name_column.append(item[1] + ' ' + item[2])
        email_address_column.append(item[3]) 

    # Convert the list to a series for each column.
    key_series = pd.DataFrame(key_column)
    name_series = pd.DataFrame(name_column)
    email_address_series = pd.DataFrame(email_address_column)

    # Combine the series into a new dataframe.
    combined_dataframe = pd.concat([key_series, name_series, email_address_series], axis = 1)
    combined_dataframe.columns = ['PRIMARY KEY', 'NAME', 'EMAIL']

    # Print records to screen.
    print(combined_dataframe)

    # Close our connection.
    conn.close()

# Add new records to the table.
def add_record(first_name, last_name, email_address) :
    # Connect to database.
    conn = sqlite3.connect('finances.db')
    # Create a cursor.
    cursor = conn.cursor()

    new_customers = [ (first_name[i], last_name[i], email_address[i]) for i in range(len(first_name))] 

    # Insert records into database.
    cursor.executemany(""" INSERT INTO customers VALUES (?, ?, ?) """, new_customers)

    # Commit our command.
    conn.commit()

    # Close our connection.
    conn.close()


