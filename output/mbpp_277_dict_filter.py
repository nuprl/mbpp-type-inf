def dict_filter(dict: dict[str, int], n: int) -> dict[str, int]:
    """
	Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 180) == {'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 190) == {'Pierre Cox': 190}

def test_check():
    check(dict_filter)

