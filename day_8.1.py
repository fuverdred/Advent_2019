import numpy as np
import matplotlib.pyplot as plt
H, W = 6, 25
with open('inputs/input_8.txt', 'r') as f:
    d = f.read().strip('\n')
p1 = sorted([d[i*H*W:(i+1)*H*W] for i in range(int(len(d)/(H*W)))],
             key=lambda x: x.count('0'))
print('Part 1: ', p1[0].count('1') * p1[0].count('2'))
image = [[int(d[i*W+j::H*W].strip('2')[0]) for j in range(W)] for i in range(H)]
plt.imshow(np.array(image), cmap='gray')
plt.show()
