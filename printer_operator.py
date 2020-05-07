#!/usr/bin/python3

import sys
import select

try:
    room_no = select.select([sys.stdin], [], [], 0)[0][0].read().strip()
except IndexError:
    print('No room number input found. Exiting...')
    sys.exit(1)

try:
    integerified = int(room_no)
except ValueError:
    print('Not an integer input. Exiting...')
    sys.exit(1)

if len(room_no) is not 3:
    print('Input must be a 3 digit number. Exiting...')
    sys.exit(1)

number_map = {'1':['*^','^^','^^'],
        '2':['*^','*^','^^'],
        '3':['**','^^','^^'],
        '4':['**','^*','^^'],
        '5':['*^','^*','^^'],
        '6':['**','*^','^^'],
        '7':['**','**','^^'],
        '8':['*^','**','^^'],
        '9':['^*','*^','^^'],
        '0':['^*','**','^^'],
        }

lines = [[],[],[]]

for ln in range(len(lines)):
    for digit in room_no:
        lines[ln].append(number_map[digit][ln])
    if ln % 2 !=0:
        lines[ln] = ''.join(lines[ln])[::-1]
    else:
        lines[ln] = ''.join(lines[ln])

print(''.join(lines))

