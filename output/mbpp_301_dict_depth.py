def dict_depth(d: dict[typing.Any, typing.Union[int, dict[str, dict[str, dict[None, None]]], dict[str, str], str, dict[int, dict[int, str]]]]) -> int:
    """
	Write a function to find the depth of a dictionary.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate({'a': 1, 'b': {'c': {'d': {}}}}) == 4
    assert candidate({'a': 1, 'b': {'c': 'python'}}) == 2
    assert candidate({1: 'Sun', 2: {3: {4: 'Mon'}}}) == 3

def test_check():
    check(dict_depth)

