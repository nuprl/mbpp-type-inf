def is_perfect_square(n: int) -> bool:
    """
	Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert not candidate(10)
    assert candidate(36)
    assert not candidate(14)
    assert candidate(14 * 14)
    assert not candidate(125)
    assert candidate(125 * 125)

def test_check():
    check(is_perfect_square)

