def encode(char):
    char_ascii = ord(char)
    if char_ascii in range(65, 91) + range(97, 123):
        new_char_ascii = char_ascii + 3
        if new_char_ascii in range(91, 94) + range(123, 126):
            new_char_ascii = new_char_ascii - 26
        char = chr(new_char_ascii)
    return char


def decode(char):
    char_ascii = ord(char)
    if char_ascii in range(65, 91) + range(97, 123):
        new_char_ascii = char_ascii - 3
        if new_char_ascii in range(62, 65) + range(94, 97):
            new_char_ascii = new_char_ascii + 26
        char = chr(new_char_ascii)
    return char


def caesar(proclaim, executor):
    return "".join(map(executor, proclaim))


def quit():
    raw_input('Press any key to quit.')


def main():
    proclaim = raw_input('Input the proclaim\n')
    ciphertext = caesar(proclaim, encode)
    print ciphertext
    print caesar(ciphertext, decode)
    quit()


if __name__ == '__main__':
    main()
