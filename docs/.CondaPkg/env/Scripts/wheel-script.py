#!/bin/sh
'''exec' "D:\CXC\Uni Stuttgart\24S\EGG\project\B2B\UnfoldDecode.jl\docs\.CondaPkg\env\python.exe" "$0" "$@" #'''
# -*- coding: utf-8 -*-
import re
import sys

from wheel.cli import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
