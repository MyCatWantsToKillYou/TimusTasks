# task 1964
# Difficulty 117

import os
import sys

tbl = bytes.maketrans(bytearray(range(256)),
                      bytearray([ord(b'a') + b % 26 for b in range(256)]))
sys.stdout.buffer.write(os.urandom(1000000).translate(tbl))