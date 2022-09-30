def sum(a: int, b: int) -> int:
    """
	Write a python function to find the sum of common divisors of two given numbers.
	"""
    pass

def check(candidate):
    assert candidate(10, 15) == 6
    assert candidate(100, 150) == 93
    assert candidate(4, 6) == 3

def test_check():
    check(sum)

