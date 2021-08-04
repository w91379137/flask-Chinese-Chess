

space = "　"
x = "兵"
class Chess():
    
    error = ""
    board = []
    take = None

    def __init__(self) -> None:
        self.create_board()

    def create_board(self):
        new_board = []
        for i in range(32):
            if i == 0 or i == 4:
                new_board.append(x)
            else:
                new_board.append(space)
        self.board = new_board

    def click_board(self, index):

        self.error = ''
        
        if self.take == None:
            if self.board[index] == space:
                self.error = f'不能拿 {index}'
            else:
                self.take = index
        else:
            if self.board[index] == space:
                self.board[index] = self.board[self.take]
                self.board[self.take] = space
                self.take = None
            else:
                self.error = f'有東西 {index}'
