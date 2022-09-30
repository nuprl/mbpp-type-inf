def extract_even(test_tuple: tuple[typing.Union[int, tuple[typing.Union[int, tuple[int]]]]]) -> tuple[typing.Union[int, tuple[typing.Union[int, tuple[int]]]]]:
    """
	Write a function to remove uneven elements in the nested mixed tuple.
	"""
    pass

def check(candidate):
    assert candidate((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert candidate((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert candidate((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

def test_check():
    check(extract_even)

