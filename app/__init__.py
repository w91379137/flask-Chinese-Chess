
from flask import Flask, render_template

from app.model.chess import Chess

game = Chess()

def create_app(test_config = None):
    app = Flask(__name__)

    
    # 首頁設定
    @app.route('/')
    @app.route('/index')
    def index():

        button_dict_list = []
        count = len(game.board)
        for index in range(count):
            x = index % 8
            y = (index - x) / 8
            dict = {
                "left": f"{ 50 * x + 100 }px",
                "top": f"{ 50 * y + 100}px",
                "symbol": game.board[index],
                "id": index,
            }
            button_dict_list.append(dict)

        return render_template('board.html', button_dict_list = button_dict_list)


    return app
