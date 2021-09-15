#############################
######### Modules ###########
#############################

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

import pandas as pd
import db_customers as db

#############################
###### Tkinter Window #######
#############################

# Create Tk Window.
default_window = tk.Tk()
default_window.title('Customers Information')
default_window.iconbitmap('Images\Icons\Electricity.ico')
default_window.config(bg = 'black')

##########################
######## Styling #########
##########################

button_bg = '#0D4BC5'
button_font = Font(family = 'Arial', size = 12, weight = 'bold')

general_label_bg = '#09F90D'
general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

general_entry_bg = '#0DC5B5'
general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

# Create the Table to Contain Customer Information.
db.create_table()

###########################
######## Menues ###########
###########################

#############################
####### New Records #########
#############################

# Create a Frame for Widgets regarding New Records.
new_records_frame = tk.Frame(default_window)
# Position Frame Onto Screen.
new_records_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.N + tk.E + tk.S + tk.W)

################################ Entry Labels ##################################################

new_customers_label = tk.Label(new_records_frame, text = 'New Customer Information',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
new_customers_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))

first_name_label = tk.Label(new_records_frame, text = 'First Name : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)

last_name_label = tk.Label(new_records_frame, text = 'Last Name : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)

email_address_label = tk.Label(new_records_frame, text = 'Email Address : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2,  anchor = tk.E)
email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)

phone_number_label = tk.Label(new_records_frame, text = 'Phone Number : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2,  anchor = tk.E)
phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)

subscription_plan_label = tk.Label(new_records_frame, text = 'Subscription Plan : ',
    bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 2,  anchor = tk.E)
subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)

####################################### Entry Widgets ##########################################

# Create Text Entry Widgets.
first_name = tk.Entry(new_records_frame, bg = general_entry_bg, fg = 'black',
    font = general_entry_font, borderwidth = 2)
first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

last_name = tk.Entry(new_records_frame, bg = general_entry_bg, fg = 'black',
    font = general_entry_font, borderwidth = 2)
last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)

email_address = tk.Entry(new_records_frame, bg = general_entry_bg, fg = 'black',
    font = general_entry_font, borderwidth = 2)
email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)

phone_number = tk.Entry(new_records_frame, bg = general_entry_bg, fg = 'black',
    font = general_entry_font, borderwidth = 2)
phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)

# Insert Default Text to Entry Widgets.
first_name.insert(0, 'Your First Name')
last_name.insert(0, 'Your Last Name')
email_address.insert(0, '________@_____.com')
phone_number.insert(0, '+1(XXX)-XXX-XXXX')

# Create Spinbox Widget for Subscription Plan.
subscription_plan = tk.Spinbox(new_records_frame,
    values = ('Basic', 'Premium'),
    bg = general_entry_bg, fg = 'black', font = general_entry_font, borderwidth = 2)
subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)

#####################################################
################ Access All Records #################
#####################################################

# Create a Frame for Dealing With Existing Records.
existing_records_frame = tk.Frame(default_window)
# Position Frame Onto Screen.
existing_records_frame.grid(row = 1, column = 0, padx = 10, pady = 10,  sticky = tk.N + tk.E + tk.S + tk.W)

# Create Label for Order Information.
order_information_label = tk.Label(existing_records_frame, text = 'Order By : ', bg = general_label_bg,
    fg = 'Black', font = general_label_font, borderwidth = 2, anchor = tk.E)
order_information_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))

# Create Spinbox Widget for Order Information.
order_information = tk.Spinbox(existing_records_frame,
    values = ('Key ID', 'First Name', 'Last Name', 'Email Address', 'Phone Number', 'Subscription Plan'),
    bg = general_entry_bg, fg = 'black', font = general_entry_font, borderwidth = 2)
order_information.grid(row = 0, column = 1, padx = (0, 5), pady = 5)

#########################################################################################

#######################################
########## Display Records ############
#######################################

def display_records () :

    # Declare Window as Global Variable.
    global show_records_window

    delete_display()

    # Get Records from Database.
    column_to_organize = str(order_information.get())
    records_df = db.show_all_records(column_to_organize)

    # Create Tk Window.
    show_records_window = tk.Toplevel()
    show_records_window.title('Customers Information')
    show_records_window.iconbitmap('Images\Icons\Database_Icon.ico')
    show_records_window.config(bg = 'White')

    # Create Tk Frame.
    show_records_frame = tk.Frame(show_records_window)
    show_records_frame.pack(pady = 20)
    show_records_frame.config(bg = 'Black')

    # Create Text Label for Data.
    records_data_label = tk.Label(show_records_frame, text = 'Customers Data',
        bg = general_label_bg, fg = 'Black', font = general_label_font, borderwidth = 5, anchor = tk.E)
    records_data_label.pack(padx = 5, pady = 10)

    # Create a Scrollbar for Treeview for Y axis.
    tree_scroll = tk.Scrollbar(show_records_frame)
    tree_scroll.pack(side = tk.RIGHT, fill = tk.Y)

    # Style the Treeview.
    treeview_style = ttk.Style()

    # Modify the Body of the Treeview.
    treeview_style.configure(
        'display_style.Treeview',
        highlightthickness = 2,
        bd = 2,
        font = general_entry_font,
        background = 'lightblue',
        foreground = 'black',
        rowheight = 25,
        fieldbackground = 'silver'
    )

    # Modify the Heading of the Treeview.
    treeview_style.configure(
        'display_style.Treeview.Heading',
        highlightthickness = 5,
        bd = 5,
        font = general_label_font,
        background = 'lightgreen',
        foreground = 'black',
        rowheight = 25,
        fieldbackground = 'silver'
    )

    # Change Color of Selected Row.
    treeview_style.map('display_style.Treeview', background = [('selected', 'white')])

    # Create Treeview.
    records_tree = ttk.Treeview(
        show_records_frame,
        yscrollcommand = tree_scroll.set,
        style = 'display_style.Treeview'
    )

    tree_scroll.config(command = records_tree.yview)

    # Set Up New Treeview Columns as DataFrame Columns.
    records_tree['column'] = list(records_df.columns)
    records_tree['show'] = 'headings'

    # Set Treeview Columns as Headings.
    for column in records_tree['column'] :
        records_tree.heading(column, text = column)

    # Separate DataFrame Rows into Lists.
    records_df_rows = records_df.to_numpy().tolist()

    # Insert Each DataFrame Row Into Treeview At a Time.
    for row in records_df_rows :
        records_tree.insert('', tk.END, values = row)

    records_tree.pack()

def delete_display() :

    # Declare Window as Global Variable.
    global show_records_window

    # Destroy the Tk Window If It Exists.
    try :
        show_records_window.destroy()
    except Exception as WindowDoesNotExist :
        pass


# Create Query Button.
queryButton = tk.Button(existing_records_frame, text = 'Query', bg = button_bg, fg = 'white',
    font = button_font, borderwidth = 2, command = display_records)
queryButton.grid(row = 0, column = 2, padx = 5, pady = 5)

########################################################################################

##########################################################
################ Access Specific Records #################
##########################################################

# Create Label for ID.
id_box_label = tk.Label(existing_records_frame, text = 'Key ID : ', bg = general_label_bg, fg = 'black',
    font = general_label_font, borderwidth = 2, anchor = tk.E)
id_box_label.grid(row = 1, column = 0, padx = 5, pady = 5)

if (db.number_of_records() > 0) :
    key_ids_in_table = db.show_all_primary_keys()
else :
    # Need at Least Two Values in Spinbox
    key_ids_in_table = ('', '')

# Create Spinbox Widget for ID.
id_box = tk.Spinbox(existing_records_frame, values = key_ids_in_table,
    bg = general_entry_bg, fg = 'black', font = general_entry_font, borderwidth = 2)
id_box.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

########################################################################################

############################
####### Add Record #########
############################

def add_record () :

    new_record = [
        first_name.get(),
        last_name.get(),
        email_address.get(),
        phone_number.get(),
        str(subscription_plan.get())]
    db.add_records(
        str(new_record[db.FIRST_NAME]), # First Name
        str(new_record[db.LAST_NAME]), # Last Name
        str(new_record[db.EMAIL]), # Email Address
        str(new_record[db.PHONE_NUMBER]), # Phone Number
        str(new_record[db.SUBSCRIPTION_PLAN]) # Subscription Plan
    )

    update_relevant_widgets()

# Create Add Record Button (In New Records Frame, But Modifies ID Spinbox).
addRecordButton = tk.Button(new_records_frame, text = 'Add Customer', bg = button_bg,
    fg = 'white', font = button_font, borderwidth = 2, command = add_record)
addRecordButton.grid(row = 5, column = 2, padx = 10, pady = 10)

########################################################################################

###############################
####### Delete Record #########
###############################

def delete_record() :
    id_to_delete = int(id_box.get())

    db.delete_record(id_to_delete)

    update_relevant_widgets()

# Create Delete Record Button.
deleteRecordbutton = tk.Button(existing_records_frame, text = 'Delete Customer', bg = button_bg, fg = 'white',
    font = button_font, borderwidth = 2, command = delete_record)
deleteRecordbutton.grid(row = 2, column = 0, padx = 10, pady = 10)

########################################################################################

###################################
######### Edit Record #############
###################################

# Need to Invoke Function By User Interaction With Tkinter Button.
def edit_record() :

    #############################
    ###### Tkinter Window #######
    #############################

    # Declare as Global Variable to Access Outside This Function.
    global edit_records_window

    global edit_first_name
    global edit_last_name

    global edit_email_address
    global edit_phone_number

    global edit_subscription_plan

    # Create Tk Window.
    edit_records_window = tk.Toplevel()
    edit_records_window.title('Customer Information')
    edit_records_window.iconbitmap('Images/Icons/Database_Icon.ico')

    edit_records_window.config(bg = 'black')

    # Create a Frame for Widgets regarding New Records.
    edit_records_frame = tk.Frame(edit_records_window)
    # Position Frame Onto Screen.
    edit_records_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.N + tk.E + tk.S + tk.W)

    # Get the Existing Record Information.
    id_to_change = int(id_box.get())
    existing_record_information = db.show_single_record(id_to_change)

    ################################ Entry Labels ##################################################

    edit_record_label = tk.Label(edit_records_frame, text = 'Update Information',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_record_label.grid(row = 0, column = 0, padx = 5, pady = 5)

    edit_first_name_label = tk.Label(edit_records_frame, text = 'First Name : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)

    edit_last_name_label = tk.Label(edit_records_frame, text = 'Last Name : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)

    edit_email_address_label = tk.Label(edit_records_frame, text = 'Email Address : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)

    edit_phone_number_label = tk.Label(edit_records_frame, text = 'Phone Number : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)

    edit_subscription_plan_label = tk.Label(edit_records_frame, text = 'Subscription Plan : ',
        bg = general_label_bg, fg = 'black', font = general_label_font, borderwidth = 2, anchor = tk.E)
    edit_subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)

    ################################ Entry Widgets ##################################################

    edit_first_name = tk.Entry(edit_records_frame, bg = general_entry_bg,
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)
    edit_first_name.insert(0, existing_record_information[db.FIRST_NAME])

    edit_last_name = tk.Entry(edit_records_frame, bg = general_entry_bg,
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)
    edit_last_name.insert(0, existing_record_information[db.LAST_NAME])

    edit_email_address = tk.Entry(edit_records_frame, bg = general_entry_bg,
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)
    edit_email_address.insert(0, existing_record_information[db.EMAIL])

    edit_phone_number = tk.Entry(edit_records_frame, bg = general_entry_bg,
        fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)
    edit_phone_number.insert(0, existing_record_information[db.PHONE_NUMBER])

    edit_subscription_plan = tk.Spinbox(edit_records_frame, values = ('Basic', 'Premium'),
        bg = general_entry_bg, fg = 'black', font = general_entry_font, borderwidth = 2)
    edit_subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)
    edit_subscription_plan.delete(0, tk.END)
    edit_subscription_plan.insert(0, existing_record_information[db.SUBSCRIPTION_PLAN])

    # Create Submit Button.
    submitButton = tk.Button(edit_records_frame, text = 'Submit Changes',
        bg = button_bg, fg = 'white', font = button_font, borderwidth = 2, command = submit_record_changes)
    submitButton.grid(row = 4, column = 2, padx = 5, pady = 5)

def submit_record_changes () :

    id_to_change = int(id_box.get())

    modified_first_name = edit_first_name.get()
    modified_last_name = edit_last_name.get()

    modified_email_address = edit_email_address.get()
    modified_phone_number = edit_phone_number.get()

    modified_subscription_plan = str(edit_subscription_plan.get())

    db.change_single_record(id_to_change,
        modified_first_name, modified_last_name,
        modified_email_address, modified_phone_number,
        modified_subscription_plan)

    # Close the Edit Window.
    edit_records_window.destroy()

# Create Edit Record Button.
editRecordbutton = tk.Button(existing_records_frame, text = 'Change Information',
    bg = button_bg, fg = 'white', font = button_font, borderwidth = 2, command = edit_record)
editRecordbutton.grid(row = 2, column = 1, padx = 10, pady = 10)

#############################################################################################

# Custom Modification of Widgets Depending on Number of Records.
def update_relevant_widgets () :

    if (db.number_of_records() == 0) :
        # Disable Buttons That Query or Change The Database.
        queryButton.config(state = 'disabled')
        deleteRecordbutton.config(state = 'disabled')
        editRecordbutton.config(state = 'disabled')

        # Empty Table
        key_ids_in_table = ('', '')

    elif (db.number_of_records() >= 1) :
        # Enable Buttons That Query or Change The Database.
        queryButton.config(state = 'normal')
        deleteRecordbutton.config(state = 'normal')
        editRecordbutton.config(state = 'normal')

        # Non-Empty Table
        key_ids_in_table = db.show_all_primary_keys()

    # Update ID Spinbox Widget.
    id_box.config(values = key_ids_in_table)

update_relevant_widgets()

# Infinite Loop -> Interrupted by Keyboard or Mouse.
default_window.mainloop()