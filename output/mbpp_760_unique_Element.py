def unique_Element(arr: list[int]) -> bool:
    """
	Write a python function to check whether a list of numbers contains only one distinct element or not.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 1]) == True
    assert candidate([1, 2, 1, 2]) == False
    assert candidate([1, 2, 3, 4, 5]) == False

def test_check():
    check(unique_Element)

