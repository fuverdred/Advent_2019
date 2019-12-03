with open('input_3.txt', 'r') as f:
    wire_1, wire_2 = f.readlines()

def manhatten_distance(x, y):
    return abs(x) + abs(y)

def extract_coords(wire):
    coords = []
    latency = 0
    i, j = 0, 0 #  Start position
    directions = {'R': (0, 1),
                  'L': (0, -1),
                  'U': (1, 0),
                  'D': (-1, 0)}
    for path in wire.split(','):
        y, x = directions[path[0]]
        for _ in range(int(path[1:])):
            latency += 1
            i += y
            j += x
            coords.append((i,j, latency))
    return coords

wire_1_test = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire_2_test = 'U62,R66,U55,R34,D71,R55,D58,R83'

if __name__ == '__main__':   
    wire_1_coords = extract_coords(wire_1[:-1]) #  take off the \n
    wire_2_coords = extract_coords(wire_2[:-1])

    #Part 1
    crossing_points = list({(x,y) for x,y,_ in wire_1_coords}.intersection(
        {(x,y) for x,y,_ in wire_2_coords}))
    crossing_points.sort(key=lambda x: manhatten_distance(*x))
    print(f'Part 1 distance: {manhatten_distance(*crossing_points[0])}')

    #Part 2
    latencies = []
    for x, y in crossing_points:
        for i, j, latency in wire_1_coords:
            if x==i and y==j:
                latency_1 = latency
                break
        for i, j, latency in wire_2_coords:
            if x==i and y==j:
                latency_2 = latency
                break
        latencies.append(latency_1 + latency_2)
    latencies.sort()
    print(f'Part 2 minimum latency: {latencies[0]}')
