def extract_string(str: list[str], l: int) -> list[str]:
    """
	Write a function to extract specified size of strings from a given list of string values.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'], 6) == ['Python']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'], 9) == ['exercises']

def test_check():
    check(extract_string)

