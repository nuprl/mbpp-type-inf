def sum_average(number: int) -> tuple[typing.Union[int, float]]:
    """
	Write a function to find sum and average of first n natural numbers.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(10) == (55, 5.5)
    assert candidate(15) == (120, 8.0)
    assert candidate(20) == (210, 10.5)

def test_check():
    check(sum_average)
