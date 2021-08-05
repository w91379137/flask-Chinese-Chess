
from flask import Flask, request, render_template

from app.model.chess import Chess

game = Chess()

def create_app(test_config = None):
    app = Flask(__name__)
    
    # 首頁設定
    @app.route('/', methods=('GET', 'POST'))
    @app.route('/index', methods=('GET', 'POST'))
    def index():

        value = request.form.get('button')
        if value is not None:
            game.click_board(int(value))

        button_dict_list = []
        count = len(game.board)
        for index in range(count):
            x = index % 8
            y = (index - x) / 8
            symbol = game.board[index]
            if game.cover[index]:
                symbol = "█"
            dict = {
                "left": f"{ 50 * x + 100 }px",
                "top": f"{ 50 * y + 100}px",
                "symbol": symbol,
                "id": index,
            }
            button_dict_list.append(dict)

        return render_template('board.html', button_dict_list = button_dict_list, game = game)


    return app
