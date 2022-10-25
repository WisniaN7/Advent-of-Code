class Board:
    def __init__(self, numbers : list) -> None:
        if len(numbers) != 25:
            raise ValueError('Board must have 25 numbers')
        
        self.board = []
        self.bingo = False
        
        for i in range(5):
            self.board.append(numbers[i * 5 : i * 5 + 5])
            
    def mark_number(self, number : int) -> int:
        self.board = list(map(lambda row: list(map(lambda x: '-' if x == number else x, row)), self.board))
        
        if not self.bingo and self.check_bingo():
            self.bingo = True
            sum = 0
            
            for l in self.board:
                for el in l:
                    if type(el) is int:
                        sum += el
                        
            return sum * number
        else:
            return -1

    def check_bingo(self) -> bool:
        for i in range(5):
            if self.board[i].count('-') == 5:
                return True
            
            if list(map(lambda x: x[i], self.board)).count('-') == 5:
                return True
        
        return False
        
    def print(self) -> None:
        for row in self.board:
            print(row)
        
        print()

numbersDrawn = []
boards = []

with open(r'2021\Day 4\input.txt') as f:
    numbersDrawn = f.readline().rstrip().split(',')
    
    while board := f.read(76):
        l = []
        
        for i in range(1, len(board), 3):
            l.append(int(board[i:i + 3].rstrip()))
            
        boards.append(Board(l))
        
bingos = 0
        
while num := numbersDrawn.pop(0):
    for i, board in enumerate(boards):
        if board:
            answer = board.mark_number(int(num))
            
            if answer > 0:
                bingos += 1
                
                if bingos == len(boards) - 1:
                    print(answer)
                    exit()
                
                boards[i] = None