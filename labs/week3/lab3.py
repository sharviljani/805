"""
Lab3.py
Sharvil Jani
2/12/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared
	"""
	new_list = []
	for num in num_list:
		sq_num = pow(num, 2)
		new_list.append(sq_num)
	return new_list

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and aren't title case
	title_list:list of strings
	Returns:list of strings tat are titles
	"""
	new_list = []
	for word in title_list:
		if word.istitle():
			new_list.append(word)
	return new_list

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
    key: string that is the name of the inventory item
    value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
	new_dict = {} # Makes New Dictionary
	for k, v in inventory.items(): #Runs the loop over the key to access values
		new_dict[k] = v +10 # Adds 10 to the inventory of the key
	return new_dict # Returns the new dictionary with updated values.

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
    key: tring that is the name of the inventory item
    value: nteger that equals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	""" 
	key_list = []
	for k, v in inventory.items(): #Runs the loop over the key to access values
		if inventory[k] == 0: # condition for Value of key as 0
			key_list.append(k) # Append the list of keys with value 0
	for items in key_list: # iterate through the list
		del inventory[items] # delete the keys woth value 0 as given in above condition
	return inventory # Returns the new dictionary with updated values.

def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	"""
	avgDict = {} # creates new empty dictionary
	for k,v in grades.items():# Runs loop to access Key and values in the dictionary
		# v is the list of grades for student k
		avgDict[k] = sum(v)/ float(len(v)) #Averages the values for key in the dictionary
	return avgDict# returns the updated dictionary with average of the values