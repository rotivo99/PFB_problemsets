#!/usr/bin/env python3

import sys

x = sys.argv[1]
y = sys.argv[2]

cmp = (x>y)-(x<y)
print(cmp)
