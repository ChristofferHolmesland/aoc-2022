import numpy as np

data = None

with open('day8.txt', 'r') as f:
    for i, line in enumerate(f):
        arr = np.array([[int(x) for x in line.strip()]])
        
        if i == 0:
            data = arr
        else:
            data = np.concatenate((data, arr), axis=0)

def ltr_visibility(row):
    tallest = -1

    out = np.zeros(shape=row.shape)

    for i, v in enumerate(row):
        if v > tallest:
            out[i] = 1

        if v > tallest:
            tallest = v
    
    return out

num_visible = np.count_nonzero(np.add.reduce([np.rot90(np.apply_along_axis(ltr_visibility, 1, np.rot90(data, k=i)), k=-i) for i in range(4)]))
print(num_visible)

