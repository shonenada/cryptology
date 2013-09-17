import random

import displacement


def encode(text, key):
    return displacement.displacement(text, displacement.encode, key)


def decode(text, key):
    return displacement.displacement(text, displacement.decode, key)


def test_lower_case():
    assert encode('a', 0) == 'a'
    assert encode('a', 1) == 'b'
    assert encode('a', 2) == 'c'
    assert encode('a', 3) == 'd'

    assert encode('z', 3) == 'c'
    assert encode('y', 3) == 'b'

    assert decode('a', 0) == 'a'
    assert decode('b', 1) == 'a'
    assert decode('d', 3) == 'a'
    assert decode('k', 3) == 'h'
    assert decode('b', 3) == 'y'

    assert encode('x', 3) != 'x'
    assert encode('x', 3) != 'y'

    assert decode('x', 3) != 'x'
    assert decode('y', 3) != 'x'
 

def test_upper_case():
    assert encode('A', 0) == 'A'
    assert encode('A', 1) == 'B'
    assert encode('A', 3) == 'D'
    assert encode('Z', 3) == 'C'
    assert encode('Y', 3) == 'B'

    assert decode('D', 3) == 'A'
    assert decode('C', 3) == 'Z'
    assert decode('B', 3) == 'Y'

    assert encode('X', 3) != 'X'
    assert encode('X', 3) != 'Y'

    assert decode('X', 3) != 'X'
    assert decode('Y', 3) != 'X'


def test_digital():
    for digital in range(0, 10):
        digital_char = str(digital)
        random_key = int(random.random() * 10)
        assert encode(digital_char, random_key) == digital_char
        assert decode(digital_char, random_key) == digital_char


def test_symbol():
    assert encode('!', 4) == '!'
    assert encode('@', 1) == '@'
    assert encode('#', 5) == '#'
    assert encode('$', 2) == '$'
    assert encode('^', 6) == '^'
    assert encode('%', 2) == '%'
    assert encode('&', 8) == '&'
    assert encode('*', 2) == '*'
    assert encode('(', 3) == '('
    assert encode(')', 9) == ')'

    assert decode('!', 1) == '!'
    assert decode('@', 5) == '@'
    assert decode('#', 2) == '#'
    assert decode('$', 7) == '$'
    assert decode('^', 8) == '^'
    assert decode('%', 2) == '%'
    assert decode('&', 7) == '&'
    assert decode('*', 3) == '*'
    assert decode('(', 8) == '('
    assert decode(')', 1) == ')'


def test_lower_string():
    assert encode('anbsdgqo', 0) == 'anbsdgqo'
    assert encode('anbsdgqo', 3) == 'dqevgjtr'
    assert encode('gnroiwegnwebxsda', 3) == 'jqurlzhjqzheavgd'

    assert decode('anbsdgqo', 0) == 'anbsdgqo'
    assert decode('dqevgjtr', 3) == 'anbsdgqo'
    assert decode('jqurlzhjqzheavgd', 3) == 'gnroiwegnwebxsda'


def test_upper_string():
    assert encode('ABESYER', 1) == 'BCFTZFS'
    assert encode('ANBSDGQO', 3) == 'DQEVGJTR'
    assert encode('GNROIWEGNWEBXSDA', 3) == 'JQURLZHJQZHEAVGD'

    assert decode('BCFTZFS', 1) == 'ABESYER'
    assert decode('DQEVGJTR', 3) == 'ANBSDGQO'
    assert decode('JQURLZHJQZHEAVGD', 3) == 'GNROIWEGNWEBXSDA'
