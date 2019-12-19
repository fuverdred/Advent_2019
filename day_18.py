import numpy as np

with open('inputs/input_18.txt', 'r') as f:
    maze = [i for i in f.readlines()]

test = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

test = [i for i in test.split('\n')]

directions = ((1,0), (0,1), (-1,0), (0,-1))

class Maze():
    def __init__(self, maze):
        self.maze = maze
        self.start = self.find_start()

    def find_start(self):
        for i, row in enumerate(self.maze):
            for j, char in enumerate(row):
                if char == '@':
                    return (i, j)

    def __repr__(self):
        return '\n'.join(self.maze)

    def unlock_door(self, coord):
        i,j = coord
        self.maze[i] = self.maze[i][:j]+'.'+self.maze[i][j+1:]

    def possible_paths(self):
        def recursive(maze, coord, depth=0):
            print(' '*depth, depth)
            visited.add(tuple(coord))
            char = maze[coord[0]][coord[1]]
            if char.isupper():
                doors.append((depth, tuple(coord), char))
                return # Can't pass?
            elif char.islower():
                keys.append((depth, tuple(coord), char))
            for direction in directions:
                poss = coord + direction
                char = maze[poss[0]][poss[1]]
                if char != '#' and tuple(poss) not in visited:
                    recursive(maze, poss, depth+1)
                        

        visited = set()
        keys = []
        doors = []
        recursive(self.maze, np.array(self.start))
        self.keys = keys
        self.doors = doors
                    
                    
                
    
maze = Maze(test)
maze.possible_paths()
