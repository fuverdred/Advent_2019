with open('input_3.txt', 'r') as f:
    wire_1, wire_2 = f.readlines()

def manhatten_distance(x, y):
    return abs(x) + abs(y)

def extract_coords(wire):
    coords = []
    i, j = 0, 0 #  Start position
    directions = {'R': (0, 1),
                  'L': (0, -1),
                  'U': (1, 0),
                  'D': (-1, 0)}
    for path in wire.split(','):
        y, x = directions[path[0]]
        for _ in range(int(path[1:])):
            i += y
            j += x
            coords.append((i,j))
    return coords
        
wire_1_coords = extract_coords(wire_1[:-1]) #  take off the \n
wire_2_coords = extract_coords(wire_2[:-1])

crossing_points = list(set(wire_1_coords).intersection(set(wire_2_coords)))
crossing_points.sort(key=lambda x: manhatten_distance(*x))
