def eulerian_num(n: int, m: int) -> int:
    """
	Write a function to find the Eulerian number a(n, m).
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(3, 1) == 4
    assert candidate(4, 1) == 11
    assert candidate(5, 3) == 26

def test_check():
    check(eulerian_num)
