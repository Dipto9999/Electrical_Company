########################################
############## Modules #################
########################################

import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

######################################
############## Classes ###############
######################################

class DefaultPage(tk.Frame) :
    def __init__(self, frame, master) :
        # Initialize Frame.
        tk.Frame.__init__(self, frame)

        master.title('Page Information')
        master.iconbitmap('Images\Icons\Electricity.ico')

        self.config(bg = 'black')

        # TTK Colors and Fonts.
        self.button_bg = '#0D4BC5'
        self.button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        self.heading_label_bg = '#0076CE'
        self.heading_label_font = Font(family = 'Ubuntu Mono', size = 12, weight = 'bold')

        self.general_label_bg = '#0076CE'
        self.general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        self.general_entry_bg = '#6699CC'
        self.general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

class DefaultHomePage(DefaultPage) :
    def __init__(self, frame, master) :
        # Initialize Frame.
        super(DefaultHomePage, self).__init__(frame, master)

        master.title('HomePage Information')

        # Create Frames.
        self.new_records_frame = tk.Frame(self)
        self.existing_records_frame = tk.Frame(self)

        # Position Frames.
        self.new_records_frame.pack(padx = 5, pady = (5,10))
        self.existing_records_frame.pack(padx = 5, pady = (10,0))

        #########################
        ### New Records Frame ###
        #########################

        # Create Label Widgets.
        self.new_records_label = tk.Label(self.new_records_frame, text = 'New Records Information',
            bg = self.heading_label_bg, fg = 'black', font = self.heading_label_font, borderwidth = 2, relief = 'solid', anchor = tk.E)
        self.first_name_label = tk.Label(self.new_records_frame, text = 'First Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.last_name_label = tk.Label(self.new_records_frame, text = 'Last Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.email_address_label = tk.Label(self.new_records_frame, text = 'Email Address : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid',  anchor = tk.E)
        self.phone_number_label = tk.Label(self.new_records_frame, text = 'Phone Number : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid',  anchor = tk.E)

        # Create Text Entry Widgets.
        self.first_name = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.last_name = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.email_address = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.phone_number = tk.Entry(self.new_records_frame, bg = self.general_entry_bg, fg = 'black',
            font = self.general_entry_font, borderwidth = 2, relief = 'sunken')

        # Create Button Widget.
        self.addRecordButton = tk.Button(self.new_records_frame, text = 'Add Record', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, command = self.add_record)

        # Default Text For Entry Widgets.
        self.first_name.insert(0, 'First Name')
        self.last_name.insert(0, 'Last Name')
        self.email_address.insert(0, '_______@____.com')
        self.phone_number.insert(0, '+1(XXX)-XXX-XXXX')

        ##############################
        ### Existing Records Frame ###
        ##############################

        self.column_labels_in_table = (
            'Key ID',
            'First Name',
            'Last Name',
            'Email Address',
            'Phone Number',
        )

        self.key_ids_in_table = ('','')

        # Create Label Widgets.
        self.order_information_label = tk.Label(self.existing_records_frame, text = 'Order By : ', bg = self.general_label_bg,
            fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.id_box_label = tk.Label(self.existing_records_frame, text = 'Key ID : ', bg = self.general_label_bg, fg = 'black',
            font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)

        # Create Spinbox Entry Widgets.
        self.order_information = tk.Spinbox(self.existing_records_frame, values = self.column_labels_in_table,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.id_box = tk.Spinbox(self.existing_records_frame, values = self.key_ids_in_table,
            bg = self.general_entry_bg, fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')

        # Create Button Widgets.
        self.queryButton = tk.Button(self.existing_records_frame, text = 'Query', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, relief = 'raised', command = self.view_records)
        self.deleteRecordbutton = tk.Button(self.existing_records_frame, text = 'Delete Record', bg = self.button_bg, fg = 'white',
            font = self.button_font, borderwidth = 2, relief = 'raised', command = self.delete_record)
        self.editRecordbutton = tk.Button(self.existing_records_frame, text = 'Change Information',
            bg = self.button_bg, fg = 'white', font = self.button_font, borderwidth = 2, relief = 'raised', command = self.edit_record)

        # Position Widgets.
        self.order_information_label.grid(row = 0, column = 0, padx = 5, pady = (0, 5), sticky = tk.W)
        self.order_information.grid(row = 0, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.id_box_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.id_box.grid(row = 1, column = 1, padx = (0, 5), pady = 5, sticky = tk.W)

        self.queryButton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = tk.E)
        self.deleteRecordbutton.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tk.E)
        self.editRecordbutton.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tk.E)

    def add_record(self) :
         pass

    def view_records(self) :
        pass

    def edit_record(self) :
        pass

    def delete_record(self) :
        pass

    def update_widgets(self) :
        pass

class DefaultWindow(tk.Toplevel) :
    def __init__(self, home_page) :
        # Can Initialize GUI Implicitly.
        super().__init__()

        self.title('Window Information')
        self.iconbitmap('Images/Icons/Database_Icon.ico')
        self.config(bg = 'black')

        # TTK Colors and Fonts.
        self.button_bg = '#0D4BC5'
        self.button_font = Font(family = 'Arial', size = 12, weight = 'bold')

        self.heading_label_bg = '#0076CE'
        self.heading_label_font = Font(family = 'Ubuntu Mono', size = 12, weight = 'bold')

        self.general_label_bg = '#0076CE'
        self.general_label_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

        self.general_entry_bg = '#6699CC'
        self.general_entry_font = Font(family = 'Ubuntu Mono', size = 10, weight = 'normal')

class DefaultEditWindow(DefaultWindow) :
    def __init__(self, home_page) :
        super(DefaultEditWindow, self).__init__(home_page)

        self.title('Edit Window Information')
        self.iconbitmap('Images/Icons/Database_Icon.ico')
        self.config(bg = 'white')

        # Create and Position Frame.
        self.edit_frame = tk.Frame(self)
        self.edit_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.N + tk.E + tk.S + tk.W)

        # Create Label Widgets.
        self.edit_record_label = tk.Label(self.edit_frame, text = 'Update Information',
            bg = self.heading_label_bg, fg = 'black', font = self.heading_label_font, borderwidth = 2, relief = 'solid', anchor = tk.E)
        self.first_name_label = tk.Label(self.edit_frame, text = 'First Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.last_name_label = tk.Label(self.edit_frame, text = 'Last Name : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.email_address_label = tk.Label(self.edit_frame, text = 'Email Address : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)
        self.phone_number_label = tk.Label(self.edit_frame, text = 'Phone Number : ',
            bg = self.general_label_bg, fg = 'black', font = self.general_label_font, borderwidth = 1, relief = 'solid', anchor = tk.E)

        # Create Text Entry Widgets.
        self.first_name = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.last_name = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.email_address = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')
        self.phone_number = tk.Entry(self.edit_frame, bg = self.general_entry_bg,
            fg = 'black', font = self.general_entry_font, borderwidth = 2, relief = 'sunken')

        # Create Button Widget.
        self.submitButton = tk.Button(self.edit_frame, text = 'Submit Changes',
            bg = self.button_bg, fg = 'white', font = self.button_font, borderwidth = 2, relief = 'raised', command = self.submit_changes)

    def submit_changes(self) :
        pass


class DefaultRecordsWindow(DefaultWindow) :
    def __init__(self, home_page) :
        super(DefaultRecordsWindow, self).__init__(home_page)

        self.title('Records Window Information')
        self.iconbitmap('Images/Icons/Database_Icon.ico')
        self.config(bg = 'black')

        # Retrieve Table Data.
        self.column_to_organize  = str(home_page.order_information.get())

        # Create, Position, and Configure Frame.
        self.db_records_frame = tk.Frame(self)
        self.db_records_frame.pack(pady = 20)
        self.db_records_frame.config(bg = 'black')

        # Create and Position Text Label.
        self.records_data_label = tk.Label(self.db_records_frame, text = 'Records Data',
            bg = self.heading_label_bg, fg = 'black', font = self.heading_label_font, borderwidth = 2, relief = 'solid', anchor = tk.E)
        self.records_data_label.pack(padx = 5, pady = 10)

        ### Treeview Style ###

        # Create a Treeview Style.
        self.treeview_style = ttk.Style()
        self.treeview_style.theme_use('winnative')

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
        self.treeview_style.map('display_style.Treeview', background = [('selected', 'blue')])

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