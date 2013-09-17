def encode(char, key):
    char_ascii = ord(char)
    if char_ascii in range(65, 91) + range(97, 123):
        new_char_ascii = char_ascii + key
        if new_char_ascii in range(91, 94) + range(123, 126):
            new_char_ascii = new_char_ascii - 26
        char = chr(new_char_ascii)
    return char


def decode(char, key):
    char_ascii = ord(char)
    if char_ascii in range(65, 91) + range(97, 123):
        new_char_ascii = char_ascii - key
        if new_char_ascii in range(62, 65) + range(94, 97):
            new_char_ascii = new_char_ascii + 26
        char = chr(new_char_ascii)
    return char


def displacement(proclaim, executor, key):
    return "".join([executor(p, key) for p in proclaim])


def quit():
   raw_input('Press any key to quit.')


def main():
    proclaim = raw_input('Input the proclaim\n')
    try:
        key = int(raw_input('Please input the key: \n'))
    except ValueError:
        print 'Error input.'
    ciphertext = displacement(proclaim, encode, key)
    print ciphertext
    print displacement(ciphertext, decode, key)
    quit()


if __name__ == '__main__':
    main()
