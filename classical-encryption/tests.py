import caesar


def test_low_case():
    def encode(text):
        return caesar.caesar(text, caesar.encode)
    assert encode('a') == 'd'
    assert encode('z') == 'c'
    assert encode('A') == 'D'
    assert encode('Z') == 'C'
    assert encode('1') == '1'
    assert encode('$') == '$'
    assert encode('anbsdg@13qo') == 'dqevgj@13tr'
