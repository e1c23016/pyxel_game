import pyxel

GAME_TITLE = "Pyxel Game" #仮タイトル

class OneKeyGame:
    def __init__(self):
        #初期化
        pyxel.init(160, 120, title=GAME_TITLE)

        #リソースファイルの読み込み
        pyxel.load("pyxel_game.pyxres")

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

    def draw_test(self):
        pyxel.blt(
            80,
            80,
            0,
            0,
            0,
            16,
            16,
            0
        )
        pyxel.blt(
            80,
            80,
            0,
            16,
            0,
            48,
            48,
            0
        )

    #アプリの描画
    def draw(self):
        self.draw_test()

OneKeyGame()
