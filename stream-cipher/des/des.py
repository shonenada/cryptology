import tables
from utils import *


def generate_key(raw_key):
    if len(raw_key) != 8:
        raise ValueError("Key must be 8 bits.")
    keys = []
    binary = char2bin(raw_key)
    selected_result = replace_selection(binary, tables.PC_1)
    for lf in tables.LEFT_MOVE:
        selected_result = left_move(selected_result, lf)
        result = replace_selection(selected_result, tables.PC_2)
        keys.append(result)
    return keys


def encrypt(cipher, raw_key):
    if len(cipher) != 8:
        raise ValueError("Cipher must be 8 bits")
    keys = generate_key(raw_key)
    binary = char2bin(cipher)
    IP_selected = replace_selection(binary, tables.IP)
    for i in range(0, 1):
        IP_selected = loop_step(IP_selected, keys[i])
    print IP_selected


encrypt('abcdefgh', '12345678')
