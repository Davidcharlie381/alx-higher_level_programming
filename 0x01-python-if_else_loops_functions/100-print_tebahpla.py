#!/usr/bin/python3
value = ''
for alphabet in range(122, 96, -1):
    if alphabet % 2 == 0:
        value = value + chr(alphabet)
    else:
        value = value + chr(alphabet - 32)
print('{}'.format(value), end='')
