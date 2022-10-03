def pack_consecutive_duplicates(list1: list[typing.Any]) -> list[list[typing.Any]]:
    """
	Write a function to pack consecutive duplicates of a given list elements into sublists.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert candidate([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert candidate(['a', 'a', 'b', 'c', 'd', 'd']) == [['a', 'a'], ['b'], ['c'], ['d', 'd']]

def test_check():
    check(pack_consecutive_duplicates)

