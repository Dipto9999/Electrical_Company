#############################
######### Constants #########
#############################

LOW_USAGE_RATE = 0.13
REGULAR_USAGE_RATE = 0.105
HIGH_USAGE_RATE = 0.075

HIGH_DEMAND_RATE = 8.60
REGULAR_DEMAND_RATE = 5.40
LOW_DEMAND_RATE = 0

HIGH_DEMAND_FLOOR = 115
LOW_DEMAND_CEILING = 35

LOW_USAGE_CEILING = 100
HIGH_USAGE_FLOOR = 200

class Individual :
    def __init__(self, first_name, last_name, email_address) :
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

class Customer(Individual) :
    # Class Attribute to Keep Track of Number of Customers.
    number_of_customers = 0

    def __init__(self, first_name, last_name, email_address) :
        super().__init__(first_name, last_name, email_address)
        Customer.add_customer()

    def pay_bill(self, total_usage, peak_demand) :
        usage_charge = 0
        demand_charge = 0

        if (total_usage > HIGH_USAGE_FLOOR) :
            usage_charge += (total_usage - HIGH_USAGE_FLOOR) * HIGH_USAGE_RATE
            total_usage = HIGH_USAGE_FLOOR
        if (total_usage > LOW_USAGE_CEILING) :
            usage_charge += (total_usage - LOW_USAGE_CEILING) * REGULAR_USAGE_RATE
            total_usage = LOW_USAGE_CEILING
        usage_charge += (total_usage) * LOW_USAGE_RATE

        if (peak_demand > HIGH_DEMAND_FLOOR) :
            demand_charge += (peak_demand - HIGH_DEMAND_FLOOR) * HIGH_DEMAND_RATE
            peak_demand = HIGH_DEMAND_FLOOR
        if (peak_demand > LOW_DEMAND_CEILING) :
            demand_charge += (peak_demand - LOW_DEMAND_CEILING) * REGULAR_DEMAND_RATE
            peak_demand = LOW_DEMAND_CEILING
        demand_charge += peak_demand * LOW_DEMAND_RATE

        return (usage_charge + demand_charge)

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

def test_script() :
    test_customer = Customer("Mahir", "Rahman", "mahir@gmail.com")
    print("Bill Amount : $", test_customer.pay_bill(250, 130))
    print("Number of Customers : ", Customer.number_of_customers)

# Test the Functionality of Python Script.
## test_script();
