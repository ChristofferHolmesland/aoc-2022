import re

def task_one():
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

def task_two():
    with open('day3.txt', 'r') as f:
        sum = 0
        group = []

        for i, line in enumerate(f):
            group.append(set(line.strip()))

            if (i + 1) % 3 == 0:
                item = list(group[0].intersection(group[1]).intersection(group[2]))[0]

                if item.isupper():
                    sum += ord(item) - 38
                else:
                    sum += ord(item) - 96
                
                group.clear()
        
        print(sum)


task_two()