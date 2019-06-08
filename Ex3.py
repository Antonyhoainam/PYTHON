import numpy as np
sampl = np.random.uniform(low=-10, high=10, size=(80)).reshape(10,8)
l = np.shape(sampl)
n = float(input('nhap vao so tu nhien: '))
minn = abs(sampl[0][0] - n)
for x in range(0, l[0]):
    for y in range(0, l[1]):
        temp = sampl[x][y]
        hieu = abs(temp - n)
        if hieu < minn:
            minn = hieu
            tam = temp
        else:
            continue
print(tam)