def overlapping(list1: list[int], list2: list[int]) -> bool:
    """
	Write a python function to check whether any value in a sequence exists in a sequence or not.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3, 4, 5], [6, 7, 8, 9]) == False
    assert candidate([1, 2, 3], [4, 5, 6]) == False
    assert candidate([1, 4, 5], [1, 4, 5]) == True

def test_check():
    check(overlapping)

