import pyxel

GAME_TITLE = "Pyxel Game" #仮タイトル

class OneKeyGame:
    def __init__(self):
        #初期化
        pyxel.init(160, 120, title=GAME_TITLE)

        #ゲームのリセット
        self.is_title = True
        self.reset_game()

        #アプリの実行を開始する
        pyxel.run(self.update, self.draw)

    #ゲームのリセット
    def reset_game(self):
        pass

    #アプリの更新
    def update(self):
        pass

    #アプリの描画
    def draw(self):
        pass

OneKeyGame()
