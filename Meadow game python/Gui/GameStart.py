from tkinter import *
import Const as df


class GameStart(Frame):
    def __init__(self, width=300, height=140):
        self._result = df.const.QUIT
        self._master = Tk()
        Frame.__init__(self, self._master)
        blank_space = " "
        self._master.title(18 * blank_space + "Meadow Game")
        self._master.configure(background=df.const.DEFAULT_COLOR)
        screen_width = self._master.winfo_screenwidth()  # width of the screen
        screen_height = self._master.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # set the dimensions of the screen
        # and where it is placed
        self._master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self._master.resizable(False, False)

        self.label = Label(self._master, text="Start a new game or load one", font=("Helvetica", 12, "bold"),
                           background=df.const.DEFAULT_COLOR, foreground="white")
        self.label.place(x=35, y=30)
        self.new_game_button = Button(self._master, text="New game", relief=SOLID, background="white", borderwidth=1,
                                      font=("Helvetica", 12))
        self.new_game_button.place(x=50, y=60)
        # self.new_game_button.bind("<Button-1>", self.new_game_button_listener)
        self.new_game_button.config(command=self.new_game_button_listener)

        self.load_game_button = Button(self._master, text="Load game", relief=SOLID, background="white", borderwidth=1,
                                       font=("Helvetica", 12))
        self.load_game_button.place(x=160, y=60)
        # self.load_game_button.bind("<Button-1>", self.load_game_button_listener)
        self.load_game_button.config(command=self.load_game_button_listener)
        self._master.mainloop()

    def new_game_button_listener(self):
        self._result = df.const.NEW_GAME
        self._master.destroy()

    def load_game_button_listener(self):
        self._result = df.const.LOAD_GAME
        self._master.destroy()

    def get_result(self):
        return self._result
