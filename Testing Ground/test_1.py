test_var = [1, 2, 3]

def test_fn():
	global test_var
	test_var[0] = True
	
test_fn()
print(test_var)
