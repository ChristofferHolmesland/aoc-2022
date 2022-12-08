from collections import deque

text = ''
with open('day6.txt', 'r') as f:
    text = f.read().strip()

def task_one(text, num=4):
    chars = deque(text[:num], maxlen=num)

    if chars.count(chars[-1]) == 1:
        return 4

    for i in range(num, len(text)):
        chars.append(text[i])

        for j in range(num - 1, 0, -1):
            if chars.count(chars[j]) != 1:
                break
        else:
            return i + 1
    
    return -1

def runner():
    for x in range(1000):
        task_one(text)

runner()