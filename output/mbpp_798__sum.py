def _sum(arr: list[int]) -> int:
    """
	Write a python function to find the sum of an array.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3]) == 6
    assert candidate([15, 12, 13, 10]) == 50
    assert candidate([0, 1, 2]) == 3

def test_check():
    check(_sum)
