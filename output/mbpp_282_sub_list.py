def sub_list(nums1: list[int], nums2: list[int]) -> list[int]:
    """
	Write a function to subtract two lists element-wise.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert candidate([1, 2], [3, 4]) == [-2, -2]
    assert candidate([90, 120], [50, 70]) == [40, 50]

def test_check():
    check(sub_list)
