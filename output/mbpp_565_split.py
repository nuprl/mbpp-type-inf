def split(word: str) -> list[str]:
    """
	Write a python function to split a string into characters.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate('python') == ['p', 'y', 't', 'h', 'o', 'n']
    assert candidate('Name') == ['N', 'a', 'm', 'e']
    assert candidate('program') == ['p', 'r', 'o', 'g', 'r', 'a', 'm']

def test_check():
    check(split)

