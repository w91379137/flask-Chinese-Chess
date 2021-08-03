

space = "　"
x = "兵"

class Chess():
    
    board = []

    def __init__(self) -> None:
        self.create_board()

    def create_board(self):
        new_board = []
        for i in range(32):
            if i == 0:
                new_board.append(x)
            else:
                new_board.append(space)
        self.board = new_board
