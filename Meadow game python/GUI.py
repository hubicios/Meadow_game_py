from tkinter import *
from tkinter.scrolledtext import ScrolledText
from math import sqrt
import numpy as np
import pconst as df
from Gui.Hex import Hex


class GUI(Frame):

    def __init__(self, master=None, width=1, height=1):
        Frame.__init__(self, master)
        # self.master=master
        # ---------------------------------------------------------window title
        master.title("Meadow game")
        # master.configure(background='gray35')
        self._board_type = df.const.RECTANGLE
        self._width_border = 0
        self._height_border = 0

        # self.hex_grid=None
        # ---------------------------------------------------------window center/size

        # get screen width and height
        screen_width = master.winfo_screenwidth()  # width of the screen
        screen_height = master.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (screen_width / 2) - (df.const.WINDOW_WIDTH / 2)
        y = (screen_height / 2) - (df.const.WINDOW_HEIGHT / 2)

        # set the dimensions of the screen
        # and where it is placed
        master.geometry('%dx%d+%d+%d' % (df.const.WINDOW_WIDTH, df.const.WINDOW_HEIGHT, x, y))
        master.resizable(False, False)
        # ---------------------------------------------------------buttons

        button_font = ("Helvetica", 14)
        self.next_turn_button = Button(master, text="Next turn", width=10, height=1,
                                       background="pale green", borderwidth=1, relief=SOLID,
                                       font=button_font)
        self.next_turn_button.place(x=100, y=df.const.WINDOW_HEIGHT - 65)
        # set enter as next turn button action
        master.bind('<Return>', (lambda e, b=self.next_turn_button: b.invoke()))  # b is your button

        self.save_game_button = Button(master, text="Save game", width=10, height=1
                                       , background="white", borderwidth=1, relief=SOLID,
                                       font=button_font)
        self.save_game_button.place(x=225, y=df.const.WINDOW_HEIGHT - 65)

        self.load_game_button = Button(master, text="Load game", width=10, height=1
                                       , background="white", borderwidth=1, relief=SOLID,
                                       font=button_font)
        self.load_game_button.place(x=350, y=df.const.WINDOW_HEIGHT - 65)
        self.change_board_type_button = Button(master, text="Board type", width=10, height=1
                                               , background="white", borderwidth=1,
                                               relief=SOLID, font=button_font)

        self.change_board_type_button.place(x=475, y=df.const.WINDOW_HEIGHT - 65)
        self.txt = ScrolledText(master, undo=True, width=60, height=4, font=("Helvetica", 10), background='gray60',
                                relief=SOLID)
        self.txt.place(x=650, y=df.const.WINDOW_HEIGHT - 85)

        self.insert_log("Just a text Widget\nin two lines\n")
        self.clear_log()

        # ---------------------------------------------------------rectangles
        self._fields = np.empty((height, width), dtype='O')
        self.pack(fill=BOTH, expand=YES)
        self._width_num = width  # x
        self._height_num = height  # y
        self._canvas = Canvas(self, background='gray35')
        self.hex_grid = Hex(0, self._canvas)
        self.draw_rectangles()
        # self.draw_hexagons()


    def insert_log(self, text):
        self.txt.config(state=NORMAL)
        self.txt.insert('1.0', text)
        self.txt.config(state=DISABLED)
        self.txt.see('1.0')

    def clear_log(self):
        self.txt.config(state=NORMAL)
        self.txt.delete('1.0', END)
        self.txt.config(state=DISABLED)

    def draw_rectangles(self):

        field_width = df.const.WINDOW_WIDTH / self._width_num
        field_height = (df.const.WINDOW_HEIGHT - df.const.MENU_HEIGHT) / self._height_num
        for i in range(self._width_num):
            for j in range(self._height_num):
                self._canvas.delete(self._fields[j][i])
                self._fields[j][i] = self._canvas.create_rectangle(field_width * i, field_height * j,
                                                                   field_width * (i + 1),
                                                                   field_height * (j + 1),
                                                                   fill=df.const.DEFAULT_FIELD_COLOR)
        self._canvas.focus_set()
        self._canvas.pack(fill=BOTH, expand=YES)

    def draw_hexagons(self, hex_height):
        self.hex_grid.set_height(hex_height)
        for i in range(self._width_num):
            for j in range(self._height_num):
                self._canvas.delete(self._fields[j][i])
                self._fields[j][i] = self._canvas.create_polygon(self.hex_grid.draw_hex(i, j), outline="gray15",
                                                                 fill=df.const.DEFAULT_FIELD_COLOR)

        self._canvas.focus_set()
        self._canvas.pack(fill=BOTH, expand=YES)

    def get_board_type(self):
        return self._board_type

    def get_width(self):
        return self._width_num

    def get_height(self):
        return self._height_num

    def get_width_border(self):
        return self._width_border

    def get_height_border(self):
        return self._height_border

    def get_hex_height(self):
        return self.hex_grid.get_hex_height()

    def change_board_type(self):
        if (self._board_type == df.const.RECTANGLE):
            self._board_type = df.const.HEXAGON
        else:  # HEXAGON
            self._board_type = df.const.RECTANGLE

    def draw_board(self):
        if (self._board_type == df.const.RECTANGLE):
            self.draw_board_rect()
        else:  # HEXAGON
            self.draw_board_hex()

    def repaint(self):
        row = df.const.WINDOW_WIDTH  # width of the  panel
        col = df.const.WINDOW_HEIGHT - df.const.MENU_HEIGHT  # height of the panel
        if (self._board_type == df.const.RECTANGLE):
            field_width = row / self._width_num
            field_height = col / self._height_num
            self._width_border = (row - field_width * self._width_num) / 2
            self._height_border = (col - field_height * self._height_num) / 2
            self.draw_rectangles()
        else:  # HEXAGON
            hex_height = int(2 * min((col / (2.0 * self._height_num + 1)),
                                     (row * sqrt(3) / (3 * self._width_num + self._width_num % 2))))
            hex_height -= hex_height % 2

            self._height_border = int((2 * col - hex_height * (2 * self._height_num + 1)) / 4)
            self._width_border = int((2 * row - hex_height * (3 * self._width_num + self._width_num % 2) / sqrt(3)) / 4)

            self.hex_grid.set_borders(self._height_border, self._width_border)
            self.draw_hexagons(hex_height)

            ###################################################################

    def clear_fields(self):
        for i in range(self._width_num):
            for j in range(self._height_num):
                # self._fields[j][i] = df.const.DEFAULT_FIELD_COLOR
                self._canvas.itemconfig(self._fields[j][i], fill=df.const.DEFAULT_FIELD_COLOR)
        if (df.const.CLEAR_LOG is True):
            self.clear_log()

    def set_fields(self, colors):
        for i in range(self._width_num):
            for j in range(self._height_num):
                # self._fields[j][i] = colors[j][i]
                self._canvas.itemconfig(self._fields[j][i], fill=colors[j][i])

    def set_field(self, x, y, color):
        self._canvas.itemconfig(self._fields[y][x], fill=color)

    def reload(self, width, height, board_type):
        for i in range(self._width_num):
            for j in range(self._height_num):
                self._canvas.delete(self._fields[j][i])
        self._board_type = board_type
        self._width_num = width
        self._height_num = height
        self._fields = np.empty((height, width), dtype='O')

    # ----------------------------------------------------------------------------listeners
    def add_next_turn_listener(self, next_turn_listener):
        self.next_turn_button.config(command=next_turn_listener)

    def add_save_game_listener(self, save_game_listener):
        self.save_game_button.config(command=save_game_listener)

    def add_load_game_listener(self, load_game_listener):
        self.load_game_button.config(command=load_game_listener)

    def add_change_board_type_listener(self, change_board_type_listener):
        self.change_board_type_button.config(command=change_board_type_listener)

    def add_field_pressed_listener(self, field_pressed_listener):
        self._canvas.bind("<Button-1>", field_pressed_listener)

    def add_key_pressed_listener(self, key_pressed_listener):
        self._canvas.bind("<Key>", key_pressed_listener)

    ########################################
