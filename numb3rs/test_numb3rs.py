from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1")
    assert validate("192.168.1.1")
    assert validate("255.255.255.255")
    assert validate("0.0.0.0")

def test_invalid():
    assert not validate("256.1.1.1")
    assert not validate("192.168.1.256")
    assert not validate("192.168.1")
    assert not validate("192.168.1.1.1")
    assert not validate("cat")
    assert not validate("1.2.3.4.5")

def test_leading_zeroes():
    assert not validate("01.2.3.4")
    assert not validate("1.02.3.4")
    assert not validate("1.2.03.4")
    assert not validate("1.2.3.04")
