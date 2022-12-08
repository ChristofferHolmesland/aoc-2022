import pathlib

f = pathlib.Path("day6.txt").read_text()

def task_one(text):
    for idx, _ in enumerate(f):
        if len(set(f[idx : idx + 4])) == 4:
            return idx + 4

def runner():
    for x in range(1000):
        task_one(f)

runner()