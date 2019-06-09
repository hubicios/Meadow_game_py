# ctr+alt+l to format code in file
from GUI import GUI
from Gui.GameStart import GameStart
from Gui.SizeSlider import SizeSlider
from World import World
from Game import Game
import Const as df
from tkinter import *


class Main:

    def __init__(self):
        self._width = 2
        self._height = 4


if __name__ == "__main__":
    main = Main()

    start_game = GameStart()
    if (start_game.get_result() is df.const.QUIT):
        sys.exit()
    else:
        width = df.const.MIN_BOARD_SIZE
        height = df.const.MIN_BOARD_SIZE
        if (start_game.get_result() is df.const.NEW_GAME):
            slider = SizeSlider()

            width = slider.get_width()
            height = slider.get_height()

        root = Tk()
        world = World(width, height)
        gui = GUI(root, width, height)
        game = Game(gui, world)
        if (start_game.get_result() is df.const.LOAD_GAME):
            game.load_game()

        gui.mainloop()
