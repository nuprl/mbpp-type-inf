def get_equal(Input: list[tuple[int]]) -> bool:
    """
	Write a function to find whether all the given tuples have equal length or not.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([(11, 22, 33), (44, 55, 66)]) == True
    assert candidate([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert candidate([(1, 2), (3, 4)]) == True

def test_check():
    check(get_equal)

