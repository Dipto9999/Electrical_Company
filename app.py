import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox

import database as db

# Create Tk Window.
customers_window = tk.Tk()
customers_window.title('Customers Information')
customers_window.iconbitmap('Images\Icons\Database_Icon.ico')

# Initialize customization variables for GUI Widgets.
button_bg = '#0D4BC5'
button_font = Font(family = 'Arial', size = 12, weight = 'bold')

general_label_bg = '#09F90D'
general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

general_entry_bg = '#0DC5B5'
general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

##############################################
############## New Customers #################
##############################################

# Create a Frame for Widgets regarding New Customers.
new_customers_frame = tk.Frame(customers_window)
# Position Frame onto Screen.
new_customers_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

# Create the Table to Contain Customer Information.
db.create_table_customers()

# Create Entry Field Labels for New Customers.
new_customers_label = tk.Label(new_customers_frame, text = 'New Customer Information',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
new_customers_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))

first_name_label = tk.Label(new_customers_frame, text = 'First Name : ', 
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)

last_name_label = tk.Label(new_customers_frame, text = 'Last Name : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)

email_address_label = tk.Label(new_customers_frame, text = 'Email Address : ', 
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2,  anchor = tk.E)
email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)

# Create Entry Widgets for New Customers.
first_name = tk.Entry(new_customers_frame, width = 30, bg = general_entry_bg, fg = 'black', 
    font = general_entry_font, borderwidth = 2)
first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

last_name = tk.Entry(new_customers_frame, width = 30, bg = general_entry_bg, fg = 'black', 
    font = general_entry_font, borderwidth = 2)
last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)

email_address = tk.Entry(new_customers_frame, width = 30, bg = general_entry_bg, fg = 'black', 
    font = general_entry_font, borderwidth = 2)
email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)

# Insert Default Text to Entry Widgets.
first_name.insert(0, 'First Name')
last_name.insert(0, 'Last Name')
email_address.insert(0, 'Email Address')

def add_customer () :
    new_customer = [first_name.get(), last_name.get(), email_address.get()]
    db.add_records_customers(str(new_customer[0]), str(new_customer[1]), str(new_customer[2]))

# Create Add Customer Button.
addCustomerButton = tk.Button(new_customers_frame, text = 'Add Customer', bg = button_bg, 
    fg = 'white', font = button_font, borderwidth = 2, command = add_customer)
addCustomerButton.grid(row = 4, column = 2, padx = 10, pady = 10)

############################################################
################ Access and Delete Records ##################
############################################################

# Create a Frame for Access and Delete Record Functions.
query_delete_frame = tk.Frame(customers_window)
# Position Frame onto Screen.
query_delete_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

def show_customer_records () :
    column_to_organize = str(order_information.get())
    customer_records = db.show_records_all_customers(column_to_organize)

    # Create a Pop Up Informatic for the Customer Records.
    messagebox.showinfo('Customer Records', str(customer_records))

# Create Label for Order Information.
order_information_label = tk.Label(query_delete_frame, text = 'Order By : ', bg = general_label_bg, 
    fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
order_information_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))

# Create Entry Widget for Order Information.
order_information = tk.Entry(query_delete_frame, width = 30, bg = general_entry_bg, fg = 'black', 
    font = general_entry_font, borderwidth = 2)
order_information.grid(row = 0, column = 1, padx = (0, 5), pady = 5)
order_information.insert(0, 'Column Name')

# Create Query Button.
queryButton = tk.Button(query_delete_frame, text = 'Query', bg = button_bg, fg = 'white', 
    font = button_font, borderwidth = 2, command = show_customer_records)
queryButton.grid(row = 0, column = 2, padx = 5, pady = 5)

# Create Label for ID.
id_box_label = tk.Label(query_delete_frame, text = 'Key ID : ', bg = general_label_bg, fg = 'black', 
    font = general_label_font, borderwidth = 2, anchor = tk.E)
id_box_label.grid(row = 1, column = 0, padx = 5, pady = 5)

# Create Entry Widget for ID.
id_box = tk.Entry(query_delete_frame, width = 30, bg = general_entry_bg, fg = 'black', 
    font = general_entry_font, borderwidth = 2)
id_box.grid(row = 1, column = 1, padx = (0, 5), pady = 5)
id_box.insert(0, 'Enter Key ID to Change/Delete')

def delete_customer() :
    id_to_delete = id_box.get()
    db.delete_record_customer(id_to_delete)

# Create Delete Record Button.
deleteRecordButton = tk.Button(query_delete_frame, text = 'Delete Customer', bg = button_bg, fg = 'white', 
    font = button_font, borderwidth = 2, command = delete_customer)
deleteRecordButton.grid(row = 2, column = 0, padx = 10, pady = 10)

def open_customer_edit_window() :
    # Create Tk Window.
    global edit_window
    edit_window = tk.Tk()
    edit_window.title('New Information')
    edit_window.iconbitmap('Images/Icons/Database_Icon.ico')

    id_to_change = id_box.get()

    customer_to_modify = db.show_record_specific_customer(id_to_change)

    print(customer_to_modify)

    # Create Entry Field Labels for New Customer.
    edit_customer_label = tk.Label(edit_window, text = 'New Customer Information', 
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_customer_label.grid(row = 0, column = 0, padx = 5, pady = 5)

    edit_first_name_label = tk.Label(edit_window, text = 'First Name : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)

    edit_last_name_label = tk.Label(edit_window, text = 'Last Name : ',         
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)

    edit_email_address_label = tk.Label(edit_window, text = 'Email Address : ', 
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)

    # Create Entry Widgets for New Customers.
    global edit_first_name
    edit_first_name = tk.Entry(edit_window, width = 30, bg = general_entry_bg, 
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)
    edit_first_name.insert(0, customer_to_modify[0])

    global edit_last_name
    edit_last_name = tk.Entry(edit_window, width = 30, bg = general_entry_bg, 
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)
    edit_last_name.insert(0, customer_to_modify[1])

    global edit_email_address
    edit_email_address = tk.Entry(edit_window, width = 30, bg = general_entry_bg, 
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)
    edit_email_address.insert(0, customer_to_modify[2])

    # Create Submit Button.
    submitButton = tk.Button(edit_window, text = 'Submit Information',
        bg = button_bg, fg = 'white', font = button_font, borderwidth = 2, command = modify_customer)
    submitButton.grid(row = 4, column = 2, padx = 5, pady = 5)

def modify_customer () :
    id_to_change = id_box.get()
    modified_first_name = edit_first_name.get()
    modified_last_name = edit_last_name.get()
    modified_email_address = edit_email_address.get()
    db.change_record_specific_customer(id_to_change, modified_first_name, 
        modified_last_name, modified_email_address)

    # Close the Edit Window.
    edit_window.destroy()

# Create Modify Record Button.
modifyRecordButton = tk.Button(query_delete_frame, text = 'Change Information', 
    bg = button_bg, fg = 'white', font = button_font, borderwidth = 2, command = open_customer_edit_window)
modifyRecordButton.grid(row = 2, column = 1, padx = 10, pady = 10)

# Infinite Loop -> Interrupted by Keyboard or Mouse.
customers_window.mainloop()