def tup_string(tup1: tuple[str]) -> str:
    """
	Write a function to convert a tuple to a string.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == 'exercises'
    assert candidate(('p', 'y', 't', 'h', 'o', 'n')) == 'python'
    assert candidate(('p', 'r', 'o', 'g', 'r', 'a', 'm')) == 'program'

def test_check():
    check(tup_string)

