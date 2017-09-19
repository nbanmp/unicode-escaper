#!/usr/bin/python
# Author: Nathan
# Date Created: September 19, 2017

import sys

# Following function partly from https://stackoverflow.com/questions/5864279/converting-characters-to-their-python-escape-sequences
def escape(s):
    ch = (ord(c) for c in s)
    return ''.join(('\\u%04x' % c) for c in ch)

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " <file> <output file>"
    sys.exit()

with open(sys.argv[1], 'r') as in_file:
    with open(sys.argv[2], 'w') as out_file:
        out_file.write(escape(in_file.read()))
