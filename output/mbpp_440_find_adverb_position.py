def find_adverb_position(text: str) -> tuple[typing.Union[int, str]]:
    """
	Write a function to find the first adverb and their positions in a given sentence.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert candidate('clearly!! we can see the sky') == (0, 7, 'clearly')
    assert candidate('seriously!! there are many roses') == (0, 9, 'seriously')
    assert candidate('unfortunately!! sita is going to home') == (0, 13, 'unfortunately')

def test_check():
    check(find_adverb_position)

