def tuple_modulo(test_tup1: tuple[int], test_tup2: tuple[int]) -> tuple[int]:
    """
	Write a function which takes two tuples of the same length and performs the element wise modulo.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert candidate((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert candidate((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

def test_check():
    check(tuple_modulo)
