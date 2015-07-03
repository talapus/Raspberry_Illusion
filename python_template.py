#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

"""

import sys
from faker import Faker

# constants

gen = Faker()

# exception classes
# interface functions
# classes
# internal functions & classes

def main():
    print gen.paragraph()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
