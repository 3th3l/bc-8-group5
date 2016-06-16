class Employee(object):

	"""Creates an Employee class """


	def __init__(self, name, gender, num_transaction, salary):
		"""
		Initializes the Employee class
		Takes the following attributes: name, gender, num_transaction, salary
		 """ 


		self.name = name
		self.gender = gender
		self.num_transaction = num_transaction
		self.salary = salary


	def track_tran(self, num):
		"""Method that tracks the number of transactions """
		self.num_transaction += num


	def review_sal(self, num_tran):
		"""Method that reviews salaries based on number of transactions"""
		self.salary *= num_tran/10



class Inventory(object):
	"""Creates an Inventory class"""


	def __init__(self, stock_id, stock_name, stock_qty):
		"""Initializes the Inventory class"""
		self.stock_id = stock_id
		self.stock_name = stock_name
		self.stock_qty = stock_qty


	def dec_stock(self, qty):
		"""Method that tracks stock usage"""
		self.stock_qty -= qty


	def inc_stock(self, qty):
		"""Method that replenishes stock"""
		self.stock_qty += qty


emp1 = Employee("Ethel Jackie Hannah", "Female", 0, 50000)

inv1 = Inventory(00011, "Omo 1 KG", 33)

return inv1.stock_qty
return emp1.num_transaction

#Sell Omo
inv1.dec_stock(4)

#Update "Ethel Jackie Hannah" transactions
emp1.track_tran(1)

return inv1.stock_qty
return emp1.num_transaction





