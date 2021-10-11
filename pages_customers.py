import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

import db_customers as db

class CustomersHomePage(tk.Frame) :
    def __init__(self, frame, master) :
        # Initialize Frame.
        tk.Frame.__init__(self, frame)

        master.title('Customers Information')
        master.iconbitmap('Images\Icons\Electricity.ico')
        master.config(bg = 'black')

        self.config(bg = 'black')

        # Create the Table for the Data.
        db.create_table()

        self.button_bg = '#0D4BC5'
        self.button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        self.general_label_bg = '#09F90D'
        self.general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

        self.general_entry_bg = '#0DC5B5'
        self.general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        # Create Frames.
        self.new_records_frame = tk.Frame(self)
        self.existing_records_frame = tk.Frame(self)

        # Position Frames.
        self.new_records_frame.pack(padx = 5, pady = (5,10))
        self.existing_records_frame.pack(padx = 5, pady = (10,0))

        #########################
        ### New Records Frame ###
        #########################

        ### Entry Labels ###

        # Create Labels.
        self.new_customers_label = tk.Label(self.new_records_frame, text = 'New Customer Information',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.first_name_label = tk.Label(self.new_records_frame, text = 'First Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.last_name_label = tk.Label(self.new_records_frame, text = 'Last Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.email_address_label = tk.Label(self.new_records_frame, text = 'Email Address : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.phone_number_label = tk.Label(self.new_records_frame, text = 'Phone Number : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.subscription_plan_label = tk.Label(self.new_records_frame, text = 'Subscription Plan : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)

        # Position Labels.
        self.new_customers_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))
        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)

        ### Entry Widgets ###

        # Create Text Entry Widgets.
        self.first_name = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)
        self.last_name = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)
        self.email_address = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)
        self.phone_number = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)

        # Create Spinbox Entry Widget.
        self.subscription_plan = tk.Spinbox(self.new_records_frame, values = ('Basic', 'Premium'),
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Position Entry Widgets.
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)
        self.subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)

        # Default Text For Entry Widgets.
        self.first_name.insert(0, 'Your First Name')
        self.last_name.insert(0, 'Your Last Name')
        self.email_address.insert(0, '_______@____.com')
        self.phone_number.insert(0, '+1(XXX)-XXX-XXXX')

        self.addRecordButton = tk.Button(self.new_records_frame, text = 'Add Customer', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, command = self.add_record)
        self.addRecordButton.grid(row = 6, column = 2, padx = 10, pady = 10)

        ##############################
        ### Existing Records Frame ###
        ##############################

        self.column_labels_in_table = (
            'Key ID',
            'First Name',
            'Last Name',
            'Email Address',
            'Phone Number',
            'Subscription Plan'
        )

        self.key_ids_in_table = ('', '') if (db.number_of_records() <= 0) else db.show_all_primary_keys()

        ### Entry Widgets ###

        # Create Labels.
        self.order_information_label = tk.Label(self.existing_records_frame, text = 'Order By : ', bg = self.general_label_bg,
            fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.id_box_label = tk.Label(self.existing_records_frame, text = 'Key ID : ', bg = self.general_label_bg, fg = 'black',
            font = self.general_label_font, borderwidth = 2, anchor = tk.E)

        # Position Labels.
        self.order_information_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))
        self.id_box_label.grid(row = 1, column = 0, padx = 5, pady = 5)

        # Create Spinbox Entry Widgets.
        self.order_information = tk.Spinbox(self.existing_records_frame, values = self.column_labels_in_table,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.id_box = tk.Spinbox(self.existing_records_frame, values = self.key_ids_in_table,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Position Spinbox Entry Widgets.
        self.order_information.grid(row = 0, column = 1, padx = (0, 5), pady = 5)
        self.id_box.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

        # Create Button Widgets.
        self.queryButton = tk.Button(self.existing_records_frame, text = 'Query', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, command = self.view_records)
        # Create Delete Record Button Widget.
        self.deleteRecordbutton = tk.Button(self.existing_records_frame, text = 'Delete Customer', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, command = self.delete_record)
        self.editRecordbutton = tk.Button(self.existing_records_frame, text = 'Change Information',
            bg = self.button_bg, fg = 'white', font = self.button_font, borderwidth = 2, command = self.edit_record)

        # Position Button Widgets.
        self.queryButton.grid(row = 1, column = 2, padx = 5, pady = 5)
        self.deleteRecordbutton.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.editRecordbutton.grid(row = 2, column = 1, padx = 10, pady = 10)

    def add_record (self) :
        self.new_record = [
            self.first_name.get(),
            self.last_name.get(),
            self.email_address.get(),
            self.phone_number.get(),
            self.subscription_plan.get()
        ]
        db.add_records(
            str(self.new_record[db.FIRST_NAME]), # First Name
            str(self.new_record[db.LAST_NAME]), # Last Name
            str(self.new_record[db.EMAIL]), # Email Address
            str(self.new_record[db.PHONE_NUMBER]), # Phone Number
            str(self.new_record[db.SUBSCRIPTION_PLAN]) # Subscription Plan
        )

        self.update_widgets()

    def view_records(self) :
        try :
            self.view_records_window.destroy()
        except Exception as WindowDoesNotExist :
            pass
        finally :
            self.view_records_window = CustomersRecordsWindow(self)

    def edit_record(self) :
        self.edit_records_window = CustomersEditWindow(self)

    def delete_record(self) :
        self.id_to_delete = int(self.id_box.get())

        db.delete_record(self.id_to_delete)

        self.update_widgets()

    def update_widgets(self) :
        if (db.number_of_records() == 0) :
            # Disable Buttons That Access Customers Table.
            self.queryButton.config(state = 'disabled')
            self.deleteRecordbutton.config(state = 'disabled')
            self.editRecordbutton.config(state = 'disabled')

            # Empty Table
            self.key_ids_in_table = ('', '')

        elif (db.number_of_records() >= 1) :
            # Enable Buttons That Access Customers Table.
            self.queryButton.config(state = 'normal')
            self.deleteRecordbutton.config(state = 'normal')
            self.editRecordbutton.config(state = 'normal')

            # Non-Empty Table
            self.key_ids_in_table = db.show_all_primary_keys()

        # Update Spinbox Widgets.
        self.id_box.config(values = self.key_ids_in_table)

class CustomersEditWindow(tk.Toplevel) :
    def __init__(self, home_page) :

        # Can Initialize GUI Implicitly.
        super().__init__()

        self.title('Customer Information')
        self.iconbitmap('Images/Icons/Database_Icon.ico')
        self.config(bg = 'black')

        self.button_bg = '#0D4BC5'
        self.button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        self.general_label_bg = '#09F90D'
        self.general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

        self.general_entry_bg = '#0DC5B5'
        self.general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        # Retrieve Table Data.
        self.id_to_change = int(home_page.id_box.get())
        self.record_information = db.show_single_record(self.id_to_change)
        self.subscription_options = ('Basic', 'Premium')

        # Create and Position Frame.
        self.edit_frame = tk.Frame(self)
        self.edit_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.N + tk.E + tk.S + tk.W)

        ### Entry Labels ###

        # Create Labels.
        self.edit_record_label = tk.Label(self.edit_frame, text = 'Update Information',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.first_name_label = tk.Label(self.edit_frame, text = 'First Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.last_name_label = tk.Label(self.edit_frame, text = 'Last Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.email_address_label = tk.Label(self.edit_frame, text = 'Email Address : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.phone_number_label = tk.Label(self.edit_frame, text = 'Phone Number : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)
        self.subscription_plan_label = tk.Label(self.edit_frame, text = 'Subscription Plan : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)

        # Position Labels.
        self.edit_record_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)

        ### Entry Widgets ###

        # Create Text Entry Widgets.
        self.first_name = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.last_name = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.email_address = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.phone_number = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.subscription_plan = tk.Spinbox(self.edit_frame, values = self.subscription_options,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Position Text Entry Widgets.
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)
        self.subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)

        # Default Text For Entry Widgets.
        self.first_name.insert(0, self.record_information[db.FIRST_NAME])
        self.last_name.insert(0, self.record_information[db.LAST_NAME])
        self.email_address.insert(0, self.record_information[db.EMAIL])
        self.phone_number.insert(0, self.record_information[db.PHONE_NUMBER])
        self.subscription_plan.delete(0, tk.END) # Get Rid of Current List Item.
        self.subscription_plan.insert(0, self.record_information[db.SUBSCRIPTION_PLAN])

        self.submitButton = tk.Button(self.edit_frame, text = 'Submit Changes',
            bg = self.button_bg, fg = 'white', font = self.button_font, borderwidth = 2, command = self.submit_changes)
        self.submitButton.grid(row = 6, column = 2, padx = 5, pady = 5)

    def submit_changes(self) :
        self.first_name = self.first_name.get()
        self.last_name = self.last_name.get()

        self.email_address = self.email_address.get()
        self.phone_number = self.phone_number.get()

        self.subscription_plan = str(self.subscription_plan.get())

        db.change_single_record(
            self.id_to_change, self.first_name,
            self.last_name, self.email_address,
            self.phone_number, self.subscription_plan
        )

        # Close the Edit Window.
        self.destroy()

class CustomersRecordsWindow(tk.Toplevel) :
    def __init__(self, home_page) :

        # Can Initialize GUI Implicitly.
        super().__init__()

        self.title('Customer Information')
        self.iconbitmap('Images/Icons/Database_Icon.ico')
        self.config(bg = 'white')

        self.button_bg = '#0D4BC5'
        self.button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        self.general_label_bg = '#09F90D'
        self.general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

        self.general_entry_bg = '#0DC5B5'
        self.general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        # Retrieve Table Data.
        self.column_to_organize  = str(home_page.order_information.get())
        self.records_df = db.show_all_records(self.column_to_organize)

        # Create, Position, and Configure Frame.
        self.db_records_frame = tk.Frame(self)
        self.db_records_frame.pack(pady = 20)
        self.db_records_frame.config(bg = 'black')

        # Create and Position Text Label.
        self.records_data_label = tk.Label(self.db_records_frame, text = 'Customers Data',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 5, anchor = tk.E)
        self.records_data_label.pack(padx = 5, pady = 10)

        ### Treeview Style ###

        # Create a Treeview Style.
        self.treeview_style = ttk.Style()
        # Treeview Body Style.
        self.treeview_style.configure('display_style.Treeview',
            highlightthickness = 2, bd = 2, font = self.general_entry_font,
            background = 'lightblue', foreground = 'black', rowheight = 25, fieldbackground = 'silver'
        )
        # Treeview Heading Style.
        self.treeview_style.configure(
            'display_style.Treeview.Heading',
            highlightthickness = 5, bd = 5, font = self.general_label_font,
            background = 'lightgreen', foreground = 'black', rowheight = 25, fieldbackground = 'silver'
        )
        # Change Color of Selected Row.
        self.treeview_style.map('display_style.Treeview', background = [('selected', 'white')])

        ### Treeview ###

        # Create and Position Scrollbar for Treeview.
        self.tree_scroll = tk.Scrollbar(self.db_records_frame)
        self.tree_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        # Create Treeview.
        self.records_tree = ttk.Treeview(
            self.db_records_frame,
            yscrollcommand = self.tree_scroll.set,
            style = 'display_style.Treeview'
        )
        # Configure Scrollbar for Treeview.
        self.tree_scroll.config(command = self.records_tree.yview)
        # Assign Treeview Column Headings.
        self.records_tree['column'] = list(self.records_df.columns)
        self.records_tree['show'] = 'headings'
        for column in self.records_tree['column'] :
            self.records_tree.heading(column, text = column)
        # Assign Treeview Rows.
        records_df_rows = self.records_df.to_numpy().tolist()
        for current_row in records_df_rows :
            self.records_tree.insert('', tk.END, values = current_row)

        self.records_tree.pack()
