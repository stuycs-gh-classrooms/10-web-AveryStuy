#!/usr/bin/python
print('Content-type: text/html\n')

from random import random

r = random()

print('Here is your lucky number: ' + str(r))
