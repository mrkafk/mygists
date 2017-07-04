

##################################################################################################
# description:  python: excepthook with pm postmortem pdb python
# raw_url:      https://gist.githubusercontent.com/mrkafk/b21131df0c54236088b4/raw/bb51b5ce1afa52ab2481a570df4916ec454bc2b2/gistfile1.py
# filename:     gistfile1.py




#!/usr/bin/python

import sys
import traceback
import pdb

def excepthook(typ, value, tb):
    traceback.print_exception(typ, value, tb)
    pdb.pm()

sys.excepthook = excepthook

x = 3.0
y = 0.0
print x/y
def div(a, b):
    return a / b
print div(x,y)



