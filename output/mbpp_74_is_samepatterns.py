def is_samepatterns(colors: list[str], patterns: list[str]) -> bool:
    """
	Write a function to check whether it follows the sequence given in the patterns array.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(['red', 'green', 'green'], ['a', 'b', 'b']) == True
    assert candidate(['red', 'green', 'greenn'], ['a', 'b', 'b']) == False
    assert candidate(['red', 'green', 'greenn'], ['a', 'b']) == False

def test_check():
    check(is_samepatterns)

