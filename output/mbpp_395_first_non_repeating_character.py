def first_non_repeating_character(str1: str) -> typing.Optional[str]:
    """
	Write a python function to find the first non-repeated character in a given string.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate('abcabc') == None
    assert candidate('abc') == 'a'
    assert candidate('ababc') == 'c'

def test_check():
    check(first_non_repeating_character)

