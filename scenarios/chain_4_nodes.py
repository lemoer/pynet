#!/usr/bin/env python3
import sys
sys.path.append(".")
from pynet import *

a = Node()
for i in range(3):
    b = Node()
    connect(a, b)
    a = b

start()
finish()
