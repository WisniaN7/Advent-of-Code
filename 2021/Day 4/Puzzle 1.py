class Board:
    def __init__(self, numbers : list) -> None:
        if len(numbers) != 25:
            raise ValueError('Board must have 25 numbers')
        
        self.board = []
        
        for i in range(5):
            self.board.append(numbers[i * 5 : i * 5 + 5])
            
    def mark_number(self, number : int) -> int:
        self.board = list(map(lambda row: list(map(lambda x: -1 if x == number else x, row)), self.board))
        
        if self.check_bingo():
            sum = 0
            
            for l in self.board:
                for el in l:
                    if el > 0:
                        sum += el
                        
            return sum * number
        else:
            return -1

    def check_bingo(self) -> bool:
        for i in range(5):
            if self.board[i].count(-1) == 5:
                return True
            
            if list(map(lambda x: x[i], self.board)).count(-1) == 5:
                return True
        
        return False

numbersDrawn = []
boards = []

with open(r'2021\Day 4\input.txt') as f:
    numbersDrawn = f.readline().rstrip().split(',')

    while board := f.read(76):
        l = []
        
        for i in range(1, len(board), 3):
            l.append(int(board[i:i + 3].rstrip()))
            
        boards.append(Board(l))
        
while num := numbersDrawn.pop(0):
    for board in boards:
        answer = board.mark_number(int(num))
        
        if answer > 0:
            print(answer)
            exit()