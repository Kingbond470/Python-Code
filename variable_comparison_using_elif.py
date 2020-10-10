variable_name='hello'
variable_zoo='lion'

if (type(variable_name) == type('')) or (type(variable_zoo)==type('')):
	print("string available")
elif variable_name<variable_zoo:
	print("bigger")
elif variable_name==variable_zoo:
	print("equal")
else:
	print("smaller ")
