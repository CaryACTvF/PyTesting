from calculations import *

def test_add_4and5():
	total = add(4,5)
	assert total == 9

def test_add_6and7():
	total = add(6,7)
	assert total == 13

def test_multiply():
	total = multiply(4,5)
	assert total == 20