

space = "　"
red = ['兵', '俥']
black = ['卒', '車']

class Chess():
    
    error = ""
    board = []
    take = None

    def __init__(self) -> None:
        self.create_board()
        self.change_first()

    def create_board(self):
        new_board = []
        for i in range(32):
            new_board.append(space)
        self.board = new_board

    def change_first(self):
        self.board[0] = red[0]
        self.board[1] = red[1]
        self.board[2] = black[0]
        self.board[3] = black[1]

    def click_board(self, index):

        self.error = ''
        
        if self.take == None:
            if self.board[index] == space:
                self.error = f'不能拿 {index}'
            else:
                self.take = index
        else:
            if self.board[index] == space:

                if self.is_next(index, self.take):
                    self.board[index] = self.board[self.take]
                    self.board[self.take] = space
                    self.take = None
                else:
                    self.error = f'不能下在 {index}'
            else:
                # 判斷紅黑
                from_color_is_red, from_level = self.chess_info(self.board[self.take])
                to_color_is_red, to_level = self.chess_info(self.board[index])

                if (from_color_is_red == to_color_is_red):
                    self.error = f'有東西 {index}'
                else:
                    if (from_level < to_level):
                        self.error = f'對方比較大 {index}'
                    else:
                        self.board[index] = self.board[self.take]
                        self.board[self.take] = space
                        self.take = None

    def is_next(self, a, b):
        x_a, y_a = self.map(a)
        x_b, y_b = self.map(b)

        if (x_a == x_b):
            return abs(y_a - y_b) == 1

        if (y_a == y_b):
            return abs(x_a - x_b) == 1
        
        return False

    def map(self, index):
        x = index % 8
        y = (index - x) / 8
        return x, y

    def chess_info(self, char):
        is_red = char in red
        level = -1
        if is_red:
            level = red.index(char)
        else:
            level = black.index(char)
        return is_red, level
