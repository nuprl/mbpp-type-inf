def text_match_three(text: str) -> bool:
    """
	Write a function that matches a string that has an a followed by three 'b'.
	"""
    pass

### Unit tests below ###
def check(candidate):
    assert not candidate('ac')
    assert not candidate('dc')
    assert candidate('abbbba')
    assert candidate('caacabbbba')

def test_check():
    check(text_match_three)
