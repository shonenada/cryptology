import caesar


def encode(text):
    return caesar.caesar(text, caesar.encode)


def decode(test):
    return caesar.caesar(text, caesar.decode)


def test_lower_case():
    assert encode('a') == 'd'
    assert encode('z') == 'c'
    assert encode('d') == 'g'
    assert encode('h') == 'k'
    assert encode('y') == 'b'

    assert decode('d') == 'a'
    assert decode('c') == 'z'
    assert decode('g') == 'd'
    assert decode('k') == 'h'
    assert decode('b') == 'y'

    assert encode('x') != 'x'
    assert encode('x') != 'y'

    assert decode('x') != 'x'
    assert decode('y') != 'x'
 

def test_upper_case():
    assert encode('A') == 'D'
    assert encode('Z') == 'C'
    assert encode('D') == 'G'
    assert encode('H') == 'K'
    assert encode('Y') == 'B'

    assert decode('D') == 'A'
    assert decode('C') == 'Z'
    assert decode('G') == 'D'
    assert decode('K') == 'H'
    assert decode('B') == 'Y'

    assert encode('X') != 'X'
    assert encode('X') != 'Y'

    assert decode('X') != 'X'
    assert decode('Y') != 'X'


def test_digital():
    for digital in range(0, 10):
        assert encode(digital) == digital
        assert decode(digital) == digital


def test_symbol():
    assert encode('!') == '!'
    assert encode('@') == '@'
    assert encode('#') == '#'
    assert encode('$') == '$'
    assert encode('^') == '^'
    assert encode('%') == '%'
    assert encode('&') == '&'
    assert encode('*') == '*'
    assert encode('(') == '('
    assert encode(')') == ')'

    assert decode('!') == '!'
    assert decode('@') == '@'
    assert decode('#') == '#'
    assert decode('$') == '$'
    assert decode('^') == '^'
    assert decode('%') == '%'
    assert decode('&') == '&'
    assert decode('*') == '*'
    assert decode('(') == '('
    assert decode(')') == ')'


def test_lower_string():
    assert encode('anbsdgqo') == 'dqevgjtr'
    assert encode('gnroiwegnwebxsda') == 'jqurlzhjqlzeazgd'

    assert decode('dqevgjtr') == 'anbsdgqo'
    assert decode('jqurlzhjqlzeazgd') == 'gnroiwegnwebxsda'


def test_upper_string():
    assert encode('ANBSDGQO') == 'DQEVGJTR'
    assert encode('GNROIWEGNWEBXSDA') == 'JQURLZHJQLZEAZGD'

    assert decode('DQEVGJTR') == 'ANBSDGQO'
    assert decode('JQURLZHJQLZEAZGD') == 'GNROIWEGNWEBXSDA'
