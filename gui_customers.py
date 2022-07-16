########################################
############## Modules #################
########################################

import tkinter as tk

from gui_default import *

import db_customers as db

######################################
############## Classes ###############
######################################

class CustomersHomePage(DefaultHomePage) :
    def __init__(self, frame, master) :
        super(CustomersHomePage, self).__init__(frame, master)

        # Create the Table for the Data.
        db.create_table()

        #########################
        ### New Records Frame ###
        #########################

        # Create and Configure Label Widgets.
        self.new_records_label.config(text = 'New Customer Information')
        self.subscription_plan_label = tk.Label(self.new_records_frame, text = 'Subscription Plan : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)

        # Create Spinbox Entry Widget.
        self.subscription_plan = tk.Spinbox(self.new_records_frame, values = ('Basic', 'Premium'),
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Configure Button Widget.
        self.addRecordButton.config(text = 'Add Customer')

        # Position Widgets.
        self.new_records_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5))

        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)

        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)

        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)

        self.subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)

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

        # Configure Widgets.
        self.order_information.config(values = self.column_labels_in_table)
        self.id_box.config(values = self.key_ids_in_table)
        self.deleteRecordbutton.config(text = "Delete Customer")

    ##################
    ### Add Record ###
    ##################

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

    ####################
    ### View Records ###
    ####################

    def view_records(self) :
        try :
            self.view_records_window.destroy()
        except Exception as WindowDoesNotExist :
            pass
        finally :
            self.view_records_window = CustomersRecordsWindow(self)

    ###################
    ### Edit Record ###
    ###################

    def edit_record(self) :
        self.edit_records_window = CustomersEditWindow(self)

    ######################
    ### Delete Record ####
    ######################

    def delete_record(self) :
        self.id_to_delete = int(self.id_box.get())

        db.delete_record(self.id_to_delete)

        self.update_widgets()

    ######################
    ### Update Widgets ###
    ######################

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

class CustomersEditWindow(DefaultEditWindow) :
    def __init__(self, home_page) :
        super(CustomersEditWindow, self).__init__(home_page)

        self.title('Customer Information')

        # Retrieve Table Data.
        self.id_to_change = int(home_page.id_box.get())
        self.record_information = db.show_single_record(self.id_to_change)
        self.subscription_options = ('Basic', 'Premium')

        # Create Label Widget.
        self.subscription_plan_label = tk.Label(self.edit_frame, text = 'Subscription Plan : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2, anchor = tk.E)

        # Create Spinbox Entry Widget.
        self.subscription_plan = tk.Spinbox(self.edit_frame, values = self.subscription_options,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Position Widgets.
        self.edit_record_label.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5)

        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5)

        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5)

        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5)

        self.subscription_plan_label.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.subscription_plan.grid(row = 5, column = 1, padx = (0, 5), pady = 5)

        self.submitButton.grid(row = 6, column = 2, padx = 5, pady = 5)

        # Default Text For Entry Widgets.
        self.first_name.insert(0, self.record_information[db.FIRST_NAME])
        self.last_name.insert(0, self.record_information[db.LAST_NAME])
        self.email_address.insert(0, self.record_information[db.EMAIL])
        self.phone_number.insert(0, self.record_information[db.PHONE_NUMBER])

        self.subscription_plan.delete(0, tk.END) # Get Rid of Current List Item.
        self.subscription_plan.insert(0, self.record_information[db.SUBSCRIPTION_PLAN])

    ######################
    ### Submit Changes ###
    ######################

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

        # Destroy the Edit Window.
        self.destroy()

class CustomersRecordsWindow(DefaultRecordsWindow) :
    def __init__(self, home_page) :
        super(CustomersRecordsWindow, self).__init__(home_page)

        self.title('Customer Information')
        self.records_df = db.show_all_records(self.column_to_organize)

        # Configure Text Label.
        self.records_data_label.config(text = 'Customer Data')

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
