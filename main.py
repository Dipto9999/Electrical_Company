########################################
############## Modules #################
########################################

import tkinter as tk

from gui_finances import FinancesPage
from gui_employees import EmployeesHomePage
from gui_customers import CustomersHomePage

########################################
############## Constants ###############
########################################

STARTING_PAGE = 'FinancesPage'
STARTING_TITLE = 'Finances Information'

######################################
############## Classes ###############
######################################

class GUI(tk.Tk) :
    def __init__(self) :
        # Can Initialize GUI Implicitly.
        super().__init__()

        self.title('Electrical Company')
        self.iconbitmap('Images\Icons\Electricity.ico')
        self.config(bg = 'black')

        # Add Menu Bar to Application.
        self.toplevel_menu = tk.Menu(self)
        self.config(menu = self.toplevel_menu)

        # Add Pages Cascade.
        self.pages_menu = tk.Menu(self.toplevel_menu)
        self.toplevel_menu.add_cascade(label = 'Pages', menu = self.pages_menu)

        # Call Functions to Change Pages.
        self.pages_menu.add_command(label = 'Finances', command = lambda: self.openPage('FinancesPage', 'Finances Information'))
        self.pages_menu.add_command(label = 'Employees', command = lambda: self.openPage('EmployeesHomePage', 'Employee Information'))
        self.pages_menu.add_command(label = 'Customers', command = lambda: self.openPage('CustomersHomePage', 'Customers Information'))

        self.toplevel_frame = tk.Frame(self)

        self.toplevel_frame.pack(
            side = 'top',
            fill = 'both',
            expand = True
        )

        # Configure Rows and Columns to be Uniform in Application.
        self.toplevel_frame.grid_rowconfigure(0, weight = 1)
        self.toplevel_frame.grid_columnconfigure(0, weight = 1)

        # Initialize Dictionaries With Page Classes.
        self.pages = {}
        for Page in (FinancesPage, CustomersHomePage, EmployeesHomePage) :
            self.current_page = Page(frame = self.toplevel_frame, master = self)

            self.pages[Page.__name__] = self.current_page

            # Must Use Grid System for Positioning Pages on Window.
            self.current_page.grid(row = 0, column = 0, sticky = 'nsew')

        self.openPage(STARTING_PAGE, STARTING_TITLE)

    def openPage(self, page_name, page_title) :
        # Show a Frame for the Given Page.
        self.current_page = self.pages[page_name]
        self.current_page.tkraise()

        self.title(page_title)

###################################
############## Main ###############
###################################

if __name__ == '__main__' :
    gui = GUI()

    gui.mainloop()