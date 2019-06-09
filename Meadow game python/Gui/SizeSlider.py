import Const as df
from tkinter import *


class SizeSlider():
    def __init__(self):
        def show_values():
            self._width_result = board_width.get()
            self._height_result = board_height.get()
            master.destroy()

        width = 600
        height = 200
        master = Tk()
        master.title("Board size")
        master.configure(background=df.const.DEFAULT_COLOR)
        screen_width = master.winfo_screenwidth()  # width of the screen
        screen_height = master.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # set the dimensions of the screen
        # and where it is placed
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        master.resizable(False, False)

        board_width = Scale(master, relief=SOLID, highlightbackground=df.const.DEFAULT_COLOR,
                            background=df.const.DEFAULT_COLOR, foreground="white", borderwidth=0,
                            from_=df.const.MIN_BOARD_SIZE, to=df.const.MAX_BOARD_SIZE, orient=HORIZONTAL,
                            tickinterval=1,
                            length=600, label="Board width:")
        board_width.set(30)
        board_width.pack()
        board_height = Scale(master, relief=SOLID, background=df.const.DEFAULT_COLOR,
                             highlightbackground=df.const.DEFAULT_COLOR, foreground="white", borderwidth=0,
                             from_=df.const.MIN_BOARD_SIZE, to=df.const.MAX_BOARD_SIZE, orient=HORIZONTAL,
                             tickinterval=1,
                             length=600, label="Board height:")
        board_height.set(20)
        board_height.pack()

        Button(master, text='Set', command=show_values, relief=SOLID, background="white", borderwidth=1,
               font=("Helvetica", 12)).pack()
        self._width_result = board_width.get()
        self._height_result = board_height.get()
        master.mainloop()

    def get_width(self):
        return self._width_result

    def get_height(self):
        return self._height_result
