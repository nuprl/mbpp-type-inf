def volume_cube(l: int) -> int:
    """
	Write a function to find the volume of a cube given its side length.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(3) == 27
    assert candidate(2) == 8
    assert candidate(5) == 125

def test_check():
    check(volume_cube)

