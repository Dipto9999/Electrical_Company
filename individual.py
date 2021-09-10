class Individual :
    def __init__(self, first_name, last_name, email_address) :
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

class Customer(Individual) :
    # Class Attribute to Keep Track of Number of Customers.
    number_of_customers = 0

    def __init__(self) :
        super().__init__()

        Customer.add_customer()

    def pay_bill(self) :
        pass

    # Increment the Number of Customers.
    @classmethod
    def add_customer(cls) :
        cls.number_of_customers += 1

class Employee(Individual) :
    # Class Attribute to Keep Track of Number of Employees.
    number_of_employees = 0

    def __init__(self, employee_id, starting_wage) :
        super().__init__()

        self.employee_id = employee_id
        self.starting_wage = starting_wage

        Employee.add_employee()

    def fire(self) :
        pass

    def wage_raise(self) :
        pass

    # Increment the Number of Employees.
    @classmethod
    def add_employee(cls) :
        cls.number_of_employees += 1
