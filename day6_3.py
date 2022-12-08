text = None
with open('day6.txt', 'r') as f:
    text = [ord(c) for c in f.read().strip()]

def task_one(text):
    c = text[:4]

    if c[0] not in c[1:] and c[1] not in c[2:] and c[2] not in c[3:]:
        return 4

    for i in range(4, len(text)):
        c[0], c[1], c[2], c[3] = c[1], c[2], c[3], text[i]

        if c[0] not in c[1:] and c[1] not in c[2:] and c[2] not in c[3:]:
            return i + 1
    
    return -1

def runner():
    for x in range(1000):
        task_one(text)

runner()