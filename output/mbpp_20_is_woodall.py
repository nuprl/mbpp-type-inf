def is_woodall(x: int) -> bool:
    """
	Write a function to check if the given number is woodball or not.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(383) == True
    assert candidate(254) == False
    assert candidate(200) == False

def test_check():
    check(is_woodall)
