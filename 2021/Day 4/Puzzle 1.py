class Board:
    def __init__(self, numbers : list) -> None:
        if len(numbers) != 25:
            raise ValueError('Board must have 25 numbers')
        
        self.board = []
        
        for i in range(5):
            self.board.append(numbers[i * 5 : i * 5 + 5])

numbersDrawn = []

with open(r'2021\Day 4\input.txt') as f:
    numbersDrawn = f.readline().rstrip().split(',')
    
board = Board([i for i in range(25)])