def rearrange_bigger(n: int) -> typing.Any:
    """
	Write a function to create the next bigger number by rearranging the digits of a given number.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(12) == 21
    assert candidate(10) == False
    assert candidate(102) == 120

def test_check():
    check(rearrange_bigger)
