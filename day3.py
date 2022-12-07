import re

with open('day3.txt', 'r') as f:
    sum = 0

    i = 0
    for line in f:
        i += 1
        line = line.strip()
        half_size = len(line) // 2
        a, b = line[:half_size], line[half_size:]
        items = re.findall(f'[{a}]', b)

        for item in set(items):
            if item.isupper():
                sum += ord(item) - 38
            else:
                sum += ord(item) - 96

    print(sum)