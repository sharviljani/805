"""
Lab2.py
Sharvil Jani
1/30/2018
"""
def squared(num_list):
	"""
	"""
	new_list = []
	for num in num_list:
		sq_num = pow(num, 2)
		new_list.append(sq_num)
	return new_list