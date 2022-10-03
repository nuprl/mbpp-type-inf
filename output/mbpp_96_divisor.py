def divisor(n: int) -> int:
    """
	Write a python function to find the number of divisors of a given integer.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(15) == 4
    assert candidate(12) == 6
    assert candidate(9) == 3

def test_check():
    check(divisor)

