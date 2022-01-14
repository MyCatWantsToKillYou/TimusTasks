# task 1964
# Difficulty 117


import os
import sys

# make translation table from 0..255 to 97..122
tbl = bytes.maketrans(bytearray(range(256)),
                      bytearray([ord(b'a') + b % 26 for b in range(256)]))
# generate random bytes and translate them to lowercase ascii
sys.stdout.buffer.write(os.urandom(1000000).translate(tbl))