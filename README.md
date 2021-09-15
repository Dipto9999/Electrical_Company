# Electrical Company

## Contents
* [Overview](#Overview)
* [App Modifications](#App-Modifications)
* [Tkinter GUI](#Tkinter-GUI)
    * [Further Exploration](#Further-Exploration)

## Overview

Create <b>Desktop Application</b> driven by <b>Python</b> to collect user data and store in local database.</br>

## App Modifications

### Tkinter GUI

We used the <b>Tkinter</b> standard interface to create the <b>GUI</b> for the user to interact with when running the application.

The [(`app.py`)](app.py) <b>Python</b> file must be run to add, delete, or modify customers. This can be done as shown below.

<p align="center"><img src="Images/Demonstrations/Add_Customer.JPG" height="40%" width="40%" title="Adding Customer in Application." ></p>

We can also query the database and view information for all individuals in some specified order.

<p align="center"><img src="Images/Demonstrations/Query_DB.JPG" height="40%" width="40%" title="All Customer Information" ></p>

### Further Exploration

We are considering implementing <b>Object Oriented Programming (OOP)</b> principles to add employee functionality to the company, where individuals are provided salaries, hired and fired on demand. This will allow us to simulate an income flow for the **Electrical Company**.

### Tasks

-> GUI
    - Style Treeview to Display Customers Data from SQLite
    - Add OOP to GUI
    - Menu to Access Customers, Employees, Finances
        - Finances Should Have Data Graphics (Use Matplotlib)

-> Company :
    - Calculate Income From All Customers
        - Basic (Multiplication Factor of 1)
        - Premium (Multiplication Factor of 1.5)
    - Calculate Monthly Wage to Pay All Employees
        - Fixed Wages Are Acquired From Database
        - Additional Wages Calculated As :
            - Salespeople Add New Customers (Parameter in Method), Get Commision
            - Corporate received $100 for every $1000 Net Income
            - Technical Workers Get a Bonus Every Quarter (4 Months) Based on Position
                - Specific to Each Employee and Position