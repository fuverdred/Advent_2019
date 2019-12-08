import numpy as np
import matplotlib.pyplot as plt

with open('inputs/input_8.txt', 'r') as f:
    data = f.read().strip('\n')

WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT
LAYERS = int(len(data)/(HEIGHT * WIDTH))

layers = []
for i in range(LAYERS):
    layers.append(data[i*LAYER_SIZE:(i+1)*LAYER_SIZE])

counts = sorted([[layer.count(c) for c in ('012')] for layer in layers])
print(f'Part 1 result: {counts[0][1]*counts[0][2]}')

picture = ''
for pixel in range(LAYER_SIZE):
    for layer in layers:
        if layer[pixel] != '2':
            picture += layer[pixel]
            break
img = np.array([int(i) for i in picture]).reshape((HEIGHT, WIDTH))

plt.imshow(img, cmap='gray')
plt.show()
