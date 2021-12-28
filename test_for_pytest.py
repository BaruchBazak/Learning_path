def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISds"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_name(name):
	return name[2]


def test_name_check():
	assert test_name("baruch") == "r"


