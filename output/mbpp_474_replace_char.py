def replace_char(str1: str, ch: str, newch: str) -> str:
    """
	Write a function to replace characters in a string.
	"""
    pass

def check(candidate):
    assert candidate('polygon', 'y', 'l') == 'pollgon'
    assert candidate('character', 'c', 'a') == 'aharaater'
    assert candidate('python', 'l', 'a') == 'python'

def test_check():
    check(replace_char)

