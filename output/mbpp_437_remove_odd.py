def remove_odd(str1: str) -> str:
    """
	Write a function to remove odd characters in a string.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate('python') == 'yhn'
    assert candidate('program') == 'rga'
    assert candidate('language') == 'agae'

def test_check():
    check(remove_odd)

