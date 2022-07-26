########################################
############## Modules #################
########################################

import tkinter as tk

from gui_default import *

import db_employees as db

########################################
############## Constants ###############
########################################

MIN_WAGE = 2400
MAX_WAGE = 1000000

######################################
############## Classes ###############
######################################

class EmployeesHomePage(DefaultHomePage) :
    def __init__(self, frame, master) :
        super(EmployeesHomePage, self).__init__(frame, master)

        # Create the Table for the Data.
        db.create_table()

        #########################
        ### New Records Frame ###
        #########################

        self.department_options = db.show_all_departments() if (db.show_all_departments()) else ('', '')

        # Create and Configure Label Widgets.
        self.new_records_label.config(text = 'New Employee Information')
        self.department_label = tk.Label(self.new_records_frame, text = 'Department : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.job_title_label = tk.Label(self.new_records_frame, text = 'Job Title : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.monthly_wage_label = tk.Label(self.new_records_frame, text = 'Monthly Wage : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)

        # Create Text Entry Widget.
        self.job_title = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)

        # Create Spinbox Entry Widgets.
        self.department = tk.Spinbox(self.new_records_frame, values = self.department_options,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.monthly_wage = tk.Spinbox(self.new_records_frame, values = tuple(range(MIN_WAGE, 1000250, 250)),
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Configure Button Widget.
        self.addRecordButton.config(text = 'Add Employee')

        # Position Widgets.
        self.new_records_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5), sticky = tk.W)

        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.department_label.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.department.grid(row = 1, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.job_title_label.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.job_title.grid(row = 2, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.monthly_wage_label.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.monthly_wage.grid(row = 3, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.addRecordButton.grid(row = 5, column = 4, padx = 10, pady = 10, sticky = tk.E)

        # Default Text For Entry Widget.
        self.job_title.insert(0, 'Title')

        ##############################
        ### Existing Records Frame ###
        ##############################

        self.column_labels_in_table = (
            'Key ID',
            'First Name',
            'Last Name',
            'Email Address',
            'Phone Number',
            'Department',
            'Job Title',
            'Monthly Wage',
        )

        self.key_ids_in_table = ('', '') if (db.number_of_records() <= 0) else db.show_all_primary_keys()

        # Configure Widgets.
        self.order_information.config(values = self.column_labels_in_table)
        self.id_box.config(values = self.key_ids_in_table)
        self.deleteRecordbutton.config(text = "Delete Employee")

    ##################
    ### Add Record ###
    ##################

    def add_record(self) :
        self.new_record = [
            self.first_name.get(),
            self.last_name.get(),
            self.email_address.get(),
            self.phone_number.get(),
            self.department.get(),
            self.job_title.get(),
            self.monthly_wage.get()
        ]
        db.add_records(
            str(self.new_record[db.FIRST_NAME]), # First Name
            str(self.new_record[db.LAST_NAME]), # Last Name
            str(self.new_record[db.EMAIL]), # Email Address
            str(self.new_record[db.PHONE_NUMBER]), # Phone Number
            str(self.new_record[db.DEPARTMENT]), # Department
            str(self.new_record[db.JOB_TITLE]), # Job Title
            float(self.new_record[db.MONTHLY_WAGE]) # Monthly Wage
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
            self.view_records_window = EmployeesRecordsWindow(self)

    ###################
    ### Edit Record ###
    ###################

    def edit_record(self) :
        self.edit_records_window = EmployeesEditWindow(self)

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
            # Disable Buttons That Access Employees Table.
            self.queryButton.config(state = 'disabled')
            self.deleteRecordbutton.config(state = 'disabled')
            self.editRecordbutton.config(state = 'disabled')

            # Empty Table
            self.key_ids_in_table = ('', '')

        elif (db.number_of_records() >= 1) :
            # Enable Buttons That Access Employees Table.
            self.queryButton.config(state = 'normal')
            self.deleteRecordbutton.config(state = 'normal')
            self.editRecordbutton.config(state = 'normal')

            # Non-Empty Table
            self.key_ids_in_table = db.show_all_primary_keys()

        self.department_options = ('', '') if (db.show_all_departments() == None) else db.show_all_departments()

        # Update Spinbox Widgets.
        self.id_box.config(values = self.key_ids_in_table)
        self.department.config(values = self.department_options)

class EmployeesEditWindow(DefaultEditWindow) :
    def __init__(self, home_page) :
        super(EmployeesEditWindow, self).__init__(home_page)

        self.title('Employee Information')

        # Retrieve Table Data.
        self.id_to_change = int(home_page.id_box.get())
        self.record_information = db.show_single_record(self.id_to_change)
        self.department_options = db.show_all_departments() if (db.show_all_departments()) else ('', '')

        # Create Label Widgets.
        self.department_label = tk.Label(self.edit_frame, text = 'Department : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.job_title_label = tk.Label(self.edit_frame, text = 'Job Title : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)
        self.monthly_wage_label = tk.Label(self.edit_frame, text = 'Monthly Wage : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 2,  anchor = tk.E)

        # Create Text Entry Widget.
        self.job_title = tk.Entry(self.edit_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2)

        # Create Spinbox Entry Widgets.
        self.department = tk.Spinbox(self.edit_frame, values = self.department_options,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)
        self.monthly_wage = tk.Spinbox(self.edit_frame, values = tuple(range(MIN_WAGE, MAX_WAGE + 250, 250)),
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2)

        # Position Widgets.
        self.edit_record_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5), sticky = tk.W)

        self.first_name_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.first_name.grid(row = 1, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.last_name_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.last_name.grid(row = 2, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.email_address_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.email_address.grid(row = 3, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.phone_number_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.phone_number.grid(row = 4, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.department_label.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.department.grid(row = 1, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.job_title_label.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.job_title.grid(row = 2, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.monthly_wage_label.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = tk.W)
        self.monthly_wage.grid(row = 3, column = 3, padx = (0, 5), pady = 5, sticky = tk.W)

        self.submitButton.grid(row = 5, column = 4, padx = 5, pady = 5, sticky = tk.E)

        # Default Text For Entry Widgets.
        self.first_name.insert(0, self.record_information[db.FIRST_NAME])
        self.last_name.insert(0, self.record_information[db.LAST_NAME])
        self.email_address.insert(0, self.record_information[db.EMAIL])
        self.phone_number.insert(0, self.record_information[db.PHONE_NUMBER])

        self.department.delete(0, tk.END) # Get Rid of Current List Item.
        self.department.insert(0, self.record_information[db.DEPARTMENT])

        self.job_title.insert(0, self.record_information[db.JOB_TITLE])

        self.monthly_wage.delete(0, tk.END) # Get Rid of Current List Item.
        self.monthly_wage.insert(0, self.record_information[db.MONTHLY_WAGE])

    ######################
    ### Submit Changes ###
    ######################

    def submit_changes(self) :
        self.first_name = self.first_name.get()
        self.last_name = self.last_name.get()

        self.email_address = self.email_address.get()
        self.phone_number = self.phone_number.get()

        self.department = str(self.department.get())
        self.job_title = str(self.job_title.get())
        self.monthly_wage = float(self.monthly_wage.get())

        db.change_single_record(
            self.id_to_change, self.first_name,
            self.last_name, self.email_address,
            self.phone_number, self.department,
            self.job_title, self.monthly_wage
        )

        # Destroy the Edit Window.
        self.destroy()

class EmployeesRecordsWindow(DefaultRecordsWindow) :
    def __init__(self, home_page) :
        super(EmployeesRecordsWindow, self).__init__(home_page)

        self.title('Employee Information')
        self.records_df = db.show_all_records(self.column_to_organize)

        # Configure Text Label.
        self.records_data_label.config(text = 'Employee Data')

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
