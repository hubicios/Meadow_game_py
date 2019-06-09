from tkinter import *
from tkinter.ttk import Combobox


class RadioButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = None

        self.window_bar = Toplevel()
        self.window_bar.grab_set()
        self.screen_width = self.window_bar.winfo_screenwidth()  # width of the screen
        self.screen_height = self.window_bar.winfo_screenheight()  # height of the screen
        self.width = 300
        self.height = 100
        self.window_x = (self.screen_width / 2) - (self.width / 2)
        self.window_y = (self.screen_height / 2) - (self.height / 2)

        self.window_bar.geometry('%dx%d+%d+%d' % (self.width, self.height, self.window_x, self.window_y))
        self.window_bar.resizable(False, False)

        # Application Name
        self.window_bar.title("Field (%d,%d)" % (x + 1, y + 1))
        # Label Creation
        self.label = Label(self.window_bar, text="Choose an organism:", font=("Helvetica", 12))
        self.label.place(x=50, y=20)

        # Button Action
        # button Creation
        self.button = Button(self.window_bar, text="Add", relief=SOLID, background="white", borderwidth=1,
                             font=("Helvetica", 12))
        self.button.place(x=self.width - 90, y=35)
        # Combobox Creation
        self.number = StringVar()

        self.numberChosen = Combobox(self.window_bar, width=22, textvariable=self.number, state="readonly")
        # Adding Values
        self.numberChosen['values'] = (
            "Antelope", "Cyber sheep", "Fox", "Sheep", "Tortoise", "Wolf", "Belladonna", "Dandelion", "Grass",
            "Guarana", "Sosnowski's Hogweed")
        self.numberChosen.place(x=50, y=45)
        self.numberChosen.current()

    # def add_spawn_listener(self, spawn_listener):
    #    self.button.config(command=spawn_listener)

    def multiple_methods(*args, **kwargs):
        print(args[0])  # the first inner callback
        print(kwargs['opt1'])  # another inner callback

    def destroy(self):
        if (self.numberChosen.get() is not ""):
            # self.result(self.numberChosen.current()+1)
            print("chosen organism is : " + self.numberChosen.get())
            self.window_bar.grab_release()
            self.window_bar.destroy()

    # --------------------------------

    def get_result(self):
        return self.numberChosen.current() + 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def add_spawn_listener(self, spawn_listener):
        # self.button['command'] = lambda arg="live", kw="as the": spawn_listener(arg, opt1=kw)
        self.button.config(command=spawn_listener)
