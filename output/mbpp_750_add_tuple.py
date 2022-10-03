def add_tuple(test_list: list[int], test_tup: tuple[int]) -> list[int]:
    """
	Write a function to add the given tuple to the given list.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert candidate([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert candidate([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]

def test_check():
    check(add_tuple)

