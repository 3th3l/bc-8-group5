class Employee(object):
    
    """
Employee class which receives information about an employee. Details
should include:- name, gender, number of transaction and salary
    """

    def __init__(self, name, gender, num_transaction, salary):
                
        self.name = name
        self.gender = gender
        self.num_transaction = num_transaction
        self.salary = salary

    def track_tran(self, num):
        """
Adds the number of transactions made
        """

        self.num_transaction += num

    def review_sal(self, num_tran):
        """
Reviews employee salary depending on the number of transactions
        """

        self.salary *= num_tran/10

class Inventory(object):
    
    """
Inventory class that takes details of an inventory. These are:-
stock id, stock name and stock quantity
    """

    def __init__(self, stock_id, stock_name, stock_qty):
        
        self.stock_id = stock_id
        self.stock_name = stock_name
        self.stock_qty = stock_qty

    def dec_stock(self, qty):
        
        """
A function that deducts the quantity when stock has been bought
        """

        self.stock_qty -= qty

    def inc_stock(self, qty):
        """
A functions that adds new stock
        """

        self.stock_qty += qty

emp1 = Employee("Hannah Maslah", "Female", 1, 50000)

inv1 = Inventory(11, "Omo 1 KG", 33)

print (inv1.stock_qty)
print (emp1.num_transaction)

#Sell Omo
inv1.dec_stock(4)

#Update "Hannah Maslah's" transactions
emp1.track_tran(1)

print (inv1.stock_qty)
print (emp1.num_transaction)





