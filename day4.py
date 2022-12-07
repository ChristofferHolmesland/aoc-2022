import re

with open('day4.txt', 'r') as f:
    s1, s2 = 0, 0

    for line in f:
        [x1, x2], [y1, y2] = [[int(t) for t in p.split('-')] for p in line.split(',')]
        x = int(re.sub('1[0]*1', '1' * (x2-x1+1), bin(((2**x2)|(2**x1)) >> 1)), 2)
        y = int(re.sub('1[0]*1', '1' * (y2-y1+1), bin(((2**y2)|(2**y1)) >> 1)), 2)
        s1 += x & y in (x, y)
        s2 += (x & y) > 0

    print(s1, s2)
