from __future__ import division

def encrypto(str_input, str_key):

    key = [ord(char) for char in str_key]
    input = [ord(char) for char in str_input]

    input_len = len(input)
    key_len = len(key)

    quotient = input_len // key_len
    remainder = input_len % key_len

    output = ''

    for i in range(0, quotient):
        for j in range(0, key_len):
            output += chr((input[i * key_len + j] - 97 * 2 + key[j]) % 26 + 97)

    for i in range(0, remainder):
        output += chr(
            (input[quotient * key_len + i] - 97 * 2 + key[i]) % 26 + 97
        )

    return output


def decrypto(str_input, str_key):

    key = [ord(char) for char in str_key]
    input = [ord(char) for char in str_input]

    key_len = len(key)
    input_len = len(input)

    quotient = input_len // key_len
    remainder = input_len % key_len

    output = ''

    for i in range(0, quotient):
        for j in range(0, key_len):
            output += chr(
                (input[i * key_len + j] + 26 - key[j]) % 26 + 97
            )

    for i in range(0, remainder):
        output += chr(
            (input[quotient * key_len + i] + 26 - key[i]) % 26 + 97
        )
    
    return output


def main():
    print encrypto('gnroiwegnwebxsda', 'ddd')
    print decrypto('jqurlzhjqzheavgd', 'ddd')


if __name__ == '__main__':
    main()
