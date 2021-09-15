import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

import pandas as pd

import db_finances
import db_customers
import db_employees

STARTING_PAGE = 'FinancesPage'

class GUI(tk.Tk) :

    def __init__(self) :

        # Can Initialize GUI Implicitly.
        super().__init__()

        self.title('Electrical Company')
        self.iconbitmap('Images\Icons\Electricity.ico')
        self.config(bg = 'black')

        # Create the Tables for the Data.
        db_finances.create_table()
        db_employees.create_table()
        db_customers.create_table()

        # Add Menu Bar to Application.
        toplevel_menu = tk.Menu(self)
        self.config(menu = toplevel_menu)

        pages_menu = tk.Menu(toplevel_menu)
        toplevel_menu.add_cascade(label = 'Pages', menu = pages_menu)

        pages_menu.add_command(label = 'Customers', command = lambda: self.openPage('CustomersPage'))
        pages_menu.add_command(label = 'Finances', command = lambda: self.openPage('FinancesPage'))
        pages_menu.add_command(label = 'Employees', command = lambda: self.openPage('EmployeesPage'))

        toplevel_frame = tk.Frame(self)

        toplevel_frame.pack(
            side = 'top',
            fill = 'both',
            expand = True
        )

        # Configure Rows and Columns to be Uniform in Application.
        toplevel_frame.grid_rowconfigure(0, weight = 1)
        toplevel_frame.grid_columnconfigure(0, weight = 1)

        self.pages = {}
        for Page in (FinancesPage, CustomersPage, EmployeesPage) :
            current_page = Page(root = toplevel_frame, controller = self)

            self.pages[Page.__name__] = current_page

            current_page.grid(row = 0, column = 0, sticky = 'nsew')

        self.openPage(STARTING_PAGE)

    def openPage(self, page_name) :

        # Show a Frame for the Given Page.
        current_page = self.pages[page_name]
        current_page.tkraise()

class FinancesPage(tk.Frame) :

    def __init__(self, root, controller) :

        # Must Initialize Frame Explicitly.
        tk.Frame.__init__(self, root)

        label = tk.Label(self, text = 'Finances')
        label.pack(pady = 10, padx = 10)

class CustomersPage(tk.Frame) :

    def __init__(self, root, controller) :

        # Must Initialize Frame Explicitly.
        tk.Frame.__init__(self, root)

        controller.title('Customers Information')
        controller.iconbitmap('Images\Icons\Electricity.ico')
        controller.config(bg = 'black')

        button_bg = '#0D4BC5'
        button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        general_label_bg = '#09F90D'
        general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'bold')

        general_entry_bg = '#0DC5B5'
        general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        # Create a Frame for Widgets regarding New Records.
        new_records_frame = tk.Frame(self)
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



class EmployeesPage(tk.Frame) :

    def __init__(self, root, controller) :

        # Must Initialize Frame Explicitly.
        tk.Frame.__init__(self, root)

        label = tk.Label(self, text = 'Employees')
        label.pack(pady = 10, padx = 10)



if __name__ == '__main__' :
    gui = GUI()

    gui.mainloop()
