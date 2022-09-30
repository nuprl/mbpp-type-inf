def colon_tuplex(tuplex: tuple[typing.Union[str, int, list[None], bool]], m: int, n: int) -> tuple[typing.Union[str, int, list[int], bool]]:
    """
	Write a function to get a colon of a tuple.
	"""
    pass

def check(candidate):
    assert candidate(('HELLO', 5, [], True), 2, 50) == ('HELLO', 5, [50], True)
    assert candidate(('HELLO', 5, [], True), 2, 100) == ('HELLO', 5, [100], True)
    assert candidate(('HELLO', 5, [], True), 2, 500) == ('HELLO', 5, [500], True)

def test_check():
    check(colon_tuplex)

