

##################################################################################################
# description:  strip versions from requirements.txt
# raw_url:      https://gist.githubusercontent.com/mrkafk/d4530a5dcd957a24a0a0/raw/e5a9f0165298688b0cb0713bd22e06c12fef1b95/strip_requirements_vers.py
# filename:     strip_requirements_vers.py


#!/usr/bin/env python

import sys

def find_requirements_file():
    try:
        fo = open('requirements.txt', 'rb')
    except OSError:
        print >>sys.stderr, 'File requirements.txt not found'
        sys.exit(1)
    return fo

def strip_vers(fo):
    lines = [line.split('=') for line in fo]
    return filter(None, [line[0] for line in lines])

def write_reqs_nover():
    fo = find_requirements_file()
    vers = strip_vers(fo)
    outfname = 'requirements_nover.txt'
    with open(outfname, 'wb') as fo:
        fo.write('\n'.join(vers))
    print >>sys.stderr, 'Wrote output to', outfname

if __name__ == '__main__':
    write_reqs_nover()



