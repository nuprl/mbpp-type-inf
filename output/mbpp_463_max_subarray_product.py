def max_subarray_product(arr: list[int]) -> int:
    """
	Write a function to find the maximum product subarray of the given array.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, -2, -3, 0, 7, -8, -2]) == 112
    assert candidate([6, -3, -10, 0, 2]) == 180
    assert candidate([-2, -40, 0, -2, -3]) == 80

def test_check():
    check(max_subarray_product)

