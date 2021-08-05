

space = "　"
red = ['兵', '炮', '傌', '俥', '相', '仕', '帥']
num = [5, 2, 2, 2, 2, 2, 1] 
black = ['卒', '砲', '馬', '車', '象', '士', '將']
import random

class Chess():

    is_red_play = True
    
    error = ""
    board = []
    cover = []
    take = None

    winner = None

    def __init__(self) -> None:
        self.create_board()
        self.change_first()
        for i in range(30):
            self.random_index()
        self.create_cover()

    def create_board(self):
        new_board = []
        for i in range(32):
            new_board.append(space)
        self.board = new_board

    def change_first(self):
        # for i in range(7):
        #     self.board[i] = red[i]
        #     self.board[i+16] = black[i]
        index = 0
        for i in range(7):
            char_red = red[i]
            char_black = black[i]
            amount = num[i]
            for j in range(amount):
                # print(i, j, index)
                self.board[index] = char_red
                index += 1
                self.board[index] = char_black
                index += 1

    def random_index(self):
        a = random.randint(0, 31)
        b = random.randint(0, 31)
        temp = self.board[a]
        self.board[a] = self.board[b]
        self.board[b] = temp

    def create_cover(self):
        new_cover = []
        for i in range(32):
            new_cover.append(self.board[i] != space)
            # new_cover.append(False)
        self.cover = new_cover

    def click_board(self, index):

        self.error = ''

        if self.winner != None:
            self.error = '結束了'
            return
        
        if self.take == None:
            if self.board[index] == space:
                self.error = f'不能拿 {index}'
            elif self.cover[index]:
                self.cover[index] = False
                self.is_red_play = not self.is_red_play
            else:
                is_red, level = self.chess_info_number(index)
                if (self.is_red_play == is_red):
                    self.take = index
                else:
                    self.error = f'不能拿 顏色不對'
        else:
            if self.cover[index]:
                self.error = f'蓋住不能走 {index}'

            elif self.board[index] == space:
                if self.is_next(index, self.take):
                    self.move(index)
                else:
                    self.error = f'不能下在 {index}'
            else:
                # 判斷紅黑
                from_color_is_red, from_level = self.chess_info_number(self.take)
                to_color_is_red, to_level = self.chess_info_number(index)

                if (from_color_is_red == to_color_is_red):
                    self.error = f'有東西 {index}'
                else:
                    if (from_level == 0 and to_level == 6):
                        self.move(index)
                    elif (from_level < to_level) or (from_level == 6 and to_level == 0):
                        self.error = f'對方比較大 {index}'
                    else:
                        self.move(index)

        self.check_win()

    def move(self, index):
        self.board[index] = self.board[self.take]
        self.board[self.take] = space
        self.take = None
        self.is_red_play = not self.is_red_play

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

    def chess_info_number(self, index):
        return self.chess_info(self.board[index])

    def chess_info(self, char):
        is_red = char in red
        level = -1
        if is_red:
            level = red.index(char)
        else:
            level = black.index(char)
        return is_red, level

    def check_win(self):
        is_find_red = False
        is_find_black = False
        for char in self.board:
            if char != space:
                is_red, level = self.chess_info(char)
                if is_red:
                    is_find_red = True
                else:
                    is_find_black = True
        if not is_find_red:
            self.winner = '黑'
        
        if not is_find_black:
            self.winner = '紅'
