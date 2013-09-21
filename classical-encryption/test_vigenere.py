import vigenere


def encode(text, key):
    return vigenere.encrypto(text, key)


def decode(text, key):
    return vigenere.decrypto(text, key)


def test_lower_case():
    assert encode('a', 'a') == 'a'
    assert encode('c', 'a') == 'c'
    assert encode('z', 'b') == 'a'

    assert decode('a', 'a') == 'a'
    assert decode('c', 'a') == 'c'
    assert decode('a', 'b') == 'z'


def test_lower_string():
    assert encode('anbsdgqo', 'd') == 'dqevgjtr'
    assert encode('gnroiwegnwebxsda', 'ddd') == 'jqurlzhjqzheavgd'
    assert encode('anviwe', 'acd') == 'apyiyh'

    assert decode('dqevgjtr', 'd') == 'anbsdgqo'
    assert decode('jqurlzhjqzheavgd', 'ddd') == 'gnroiwegnwebxsda'
    assert decode('apyiyh', 'acd') == 'anviwe'
