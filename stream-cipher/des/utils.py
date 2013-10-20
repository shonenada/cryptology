import tables


def replace_selection(binary_array, table):
    output = []
    for sele in table:
        output.append(binary_array[sele - 1])
    return "".join(output)


def char2bin(text):
    binary = []
    for ch in text:
        char_bin = bin(ord(ch))
        format_bin = char_bin[2:].zfill(8)
        binary.append(format_bin)
    # or
    # binary = [ bin(ord(ch))[2:].zfill(8) for ch in text ]
    return "".join(binary)


def bin2int(text):
    length = len(text)
    count = 0
    for i in range(0, length):
        num = int(text[length-i-1])
        count = count + 2**i * num
    return count


def bin2char(binary):
    chars = []
    for i in range(0, 8):
        bin = binary[i*8 : (i+1)*8]
        c = chr(bin2int(bin))
        chars.append(c)
    return "".join(chars)


def left_move(key, offset):
    C = "".join(key[:28])
    D = "".join(key[28:])
    C_out = [C[(i+offset) % 28] for i in range(0, 28)]
    D_out = [D[(i+offset) % 28] for i in range(0, 28)]
    new_key = "".join(C_out) + "".join(D_out)
    return new_key


def loop_step(cipher, key):
    box_result = ""
    L = cipher[:32]
    R = cipher[32:]
    ext_R = replace_selection(R, tables.E)
    xor = xor_bits(ext_R, key, 48)

    for i in range(0, 8):
        box_param = xor[i*6 : i*6+6]
        row_num = bin2int(box_param[0] + box_param[5])
        column_num = bin2int("".join([x for x in box_param[1:5]]))
        r = tables.SBOX[i][row_num][column_num]
        box_result = box_result + str(bin(r)[2:].zfill(4))
    PB = replace_selection(box_result, tables.P)
    new_R = xor_bits(PB, L, 32)
    return R + "".join(new_R)


def xor_bits(a, b, n):
    output = ""
    for i in range(0, n):
        bin_a = char2bin(a[i])
        bin_b = char2bin(b[i])
        output = output + str(int(bin_a) ^ int(bin_b))
    return output
