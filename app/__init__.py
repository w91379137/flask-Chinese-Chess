
from flask import Flask, render_template

def create_app(test_config = None):
    app = Flask(__name__)

    
    # 首頁設定
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('board.html')


    return app
