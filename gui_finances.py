import tkinter as tk
from tkinter import ttk

import db_finances as db

class FinancesPage(tk.Frame) :

    def __init__(self, frame, master) :
        # Initialize Frame.
        tk.Frame.__init__(self, frame)

        master.title('Finances Information')
        master.iconbitmap('Images\Icons\Electricity.ico')
        master.config(bg = 'black')

        # Create the Table for the Data.
        db.create_table()

        self.label = tk.Label(self, text = 'Finances')
        self.label.pack(pady = 10, padx = 10)