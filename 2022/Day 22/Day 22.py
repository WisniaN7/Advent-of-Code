import re
from enum import Enum

def convert(c):
    if c  == ' ':
        return None
    elif c == '#':
        return False
    elif c == '.':
        return True

class DIR(Enum):
    R = 0
    D = 1
    L = 2
    U = 3
    
    def __iter__(self):
        if (self == DIR.U):
            yield 0
            yield -1
        elif (self == DIR.R):
            yield 1
            yield 0
        elif (self == DIR.D):
            yield 0
            yield 1
        elif (self == DIR.L):
            yield -1
            yield 0
        else:
            raise ValueError('Invalid direction:', self.name)
        
    def opposite(self):
        return DIR((self.value + 2) % 4) 
    
    def next(self):
        return DIR((self.value + 1) % 4) 
    
    def prev(self):
        return DIR((self.value - 1) % 4) 
        
board = []
instructions = []

with open(r'2022\Day 22\test.txt') as f:
    while (line := f.readline()) != '\n':
        board.append(line[:-1])
        
    instructions = f.readline().strip()
    
instructions = re.split(r'([RL])', instructions)
board = [list(map(convert, row)) for row in board]

pos = [board[0].index(True), 0]
facing = DIR.R

for instruction in instructions:
    if instruction.isnumeric():
        for _ in range(int(instruction)):
            if facing == DIR.R:
                if pos[0] + 1 == len(board[pos[1]]) or board[pos[1]][pos[0] + 1] is None:
                    prevPos = pos.copy()
                    pos = [board[pos[1]].index(True), pos[1]]
                    
                    if board[pos[1]][pos[0]] == False:
                        pos = prevPos
                        break
                elif board[pos[1]][pos[0] + 1] == False:
                    break
                else:
                    pos[0] += 1
            elif facing == DIR.L:
                if pos[0] - 1 < 0 or board[pos[1]][pos[0] - 1] is None:
                    prevPos = pos.copy()
                    
                    temp = board[pos[1]][::-1].index(True)
                    pos = [len(board[pos[1]]) - temp - 1, pos[1]]
                    
                    if board[pos[1]][pos[0]] == False:
                        pos = prevPos
                        break
                elif board[pos[1]][pos[0] - 1] == False:
                    break
                else:
                    pos[0] -= 1
            elif facing == DIR.D:
                if pos[1] + 1 == len(board) or board[pos[1] + 1][pos[0]] is None:
                    prevPos = pos.copy()
                    
                    for r in range(len(board)):
                        if board[r][pos[0]] is not None:
                            pos = [pos[0], r]
                            break

                    if board[pos[1]][pos[0]] == False:
                        pos = prevPos
                        break
                elif board[pos[1] + 1][pos[0]] == False:
                    break
                else:
                    pos[1] += 1
            elif facing == DIR.U:
                if pos[1] - 1 < 0 or board[pos[1] - 1][pos[0]] is None:
                    prevPos = pos.copy()
                    
                    for r in range(len(board) - 1, -1, -1):
                        if board[r][pos[0]] is not None:
                            pos = [pos[0], r]
                            break

                    if board[pos[1]][pos[0]] == False:
                        pos = prevPos
                        break
                elif board[pos[1] - 1][pos[0]] == False:
                    break
                else:
                    pos[1] -= 1
    elif instruction == 'R':
        facing = facing.next()
    elif instruction == 'L':
        facing = facing.prev()
    else:
        raise ValueError('Invalid instruction:', instruction)

print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facing.value)