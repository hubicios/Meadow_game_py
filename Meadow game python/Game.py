import Const as df
from Gui.RadioButton import RadioButton
from Point import Point
from World import World


class Game():
    def __init__(self, gui, world):
        self._gui = gui
        self._world = world
        self.add_listeners()
        self._world.init_world()
        self.prepare_view()

    def add_listeners(self):
        self._gui.add_next_turn_listener(self.NextTurnListener)
        self._gui.add_change_board_type_listener(self.ChangeBoardTypeListener)
        self._gui.add_save_game_listener(self.SaveGameListener)
        self._gui.add_load_game_listener(self.LoadGameListener)
        self._gui.add_field_pressed_listener(self.FieldPressedListener)
        self._gui.add_key_pressed_listener(self.KeyPressedListener)
        self._world.add_turn_info_listener(self.TurnInfoListener)

    def prepare_view(self):
        self._gui.set_fields(self._world.get_fields_color())

    def NextTurnListener(self):
        self._gui.clear_log()
        self._world.make_turn()
        self._gui.set_fields(self._world.get_fields_color())

    def SaveGameListener(self):
        self._world.save_game()
        # print("Save game")

    def LoadGameListener(self):
        self.load_game()
        # print("Load game")

    def ChangeBoardTypeListener(self):
        self._world.change_board_type()
        self._gui.change_board_type()
        self._gui.repaint()
        self._gui.set_fields(self._world.get_fields_color())
        # print("Change board type")

    def SpawnListener(self):
        x = self._combo_box.get_x()
        y = self._combo_box.get_y()
        index = self._combo_box.get_result()
        point = Point(x, y)

        if (index is not None):
            self._world.generate_organism(point, df.const.ALL_SIGNS[index])
            self._world.draw_organisms()
            self.prepare_view()
            print("organisms is spawning", repr(index))
        else:
            print("organisms failed while spawning", repr(index))
        self._combo_box.destroy()

    def FieldPressedListener(self, event):
        mouse_x = event.x - self._gui.get_width_border()
        mouse_y = event.y - self._gui.get_height_border()
        good = False
        if (self._world.get_board_type() == df.const.RECTANGLE):
            x = self.in_box_x(mouse_x)
            y = self.in_box_y(mouse_y)
            if (0 <= x < self._world.get_width() and 0 <= y < self._world.get_height()):
                good = True

        else:  # HEXAGON
            point = Point()
            point.to_hex(mouse_x, mouse_y, self._gui.get_hex_height())
            x = point.get_x()
            y = point.get_y()
            if (0 <= x < self._world.get_width() and 0 <= y < self._world.get_height()):
                good = True
        if (good is True and self._world.field_free(x, y)):
            print("Clicked at", x + 1, y + 1)
            self._combo_box = RadioButton(x, y)
            self._combo_box.add_spawn_listener(self.SpawnListener)

    def KeyPressedListener(self, event):
        if (event.char is not '\r'):
            self._world.set_input(event)

    def TurnInfoListener(self, text):
        self._gui.insert_log(text)

    def in_box_x(self, mouse_x):
        field_width = (df.const.WINDOW_WIDTH) / self._gui.get_width()
        xmod = mouse_x / field_width
        if (xmod < 0 or xmod >= self._world.get_width()):
            xmod = -1

        return int(xmod)

    def in_box_y(self, mouse_y):
        field_height = (df.const.WINDOW_HEIGHT - df.const.MENU_HEIGHT) / self._gui.get_height()
        ymod = mouse_y / field_height
        if (ymod < 0 or ymod >= self._world.get_height()):
            ymod = -1

        return int(ymod)

    def load_game(self):
        file = open(df.const.SAVE_FILE_NAME, "r")
        if (file.mode == 'r'):
            line = file.readlines()
            text = line[0].split()
            width = int(text[0])
            height = int(text[1])
            turn_count = int(text[2])
            board_type = text[3]
            self._world = World(width, height, turn_count, board_type)
            self._world.add_turn_info_listener(self.TurnInfoListener)
            iterline = iter(line)
            next(iterline)
            for x in iterline:
                self._world.load_organism(x)

            file.close()
            self._world.draw_organisms()
            self._gui.reload(width, height, board_type)
            self._gui.repaint()
            self.prepare_view()
            self._gui.clear_log()
            self._world.add_turn_info("Game has been loaded successfully")
            self._world.set_board_type(board_type)
