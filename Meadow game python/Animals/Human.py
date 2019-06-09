import Const as df
import World
from Animals.Animal import Animal
from Point import Point
from Direction import Direction


class Human(Animal):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.HUMAN_STRENGTH, skill_cooldown=0):
        super(Animal, self).__init__(world, point, df.const.HUMAN_SIGN, df.const.HUMAN_COLOR_AVAILABLE, strength,
                                     df.const.HUMAN_PRIORITY, age, id1)

        self._color_active = df.const.HUMAN_COLOR_ACTIVE
        self._color_inactive = df.const.HUMAN_COLOR_INACTIVE
        self._skill_cooldown = skill_cooldown  # how long till skill will be available (0,5)
        self._input = None

    def breeding(self):
        pass

    def is_fight_off(self, attacker):
        return (self._skill_cooldown > df.const.HUMAN_SKILL_TIME)

    def action(self):
        if (self._skill_cooldown > 0):
            self._skill_cooldown -= 1

        #if (self._age == 0):
        #    self._age += 1
        #elif (self._is_alive):
        self._age += 1

        self._input = self.user_input()
        if (self._input is not None):
            if (self._input == 'q' and self._skill_cooldown == 0):
                self._skill_cooldown = df.const.HUMAN_SKILL_TIME * 2
            else:
                point = Point(self._point.get_x(), self._point.get_y(), self._input)
                field_taken = self._world.field_taken(point)

                if (self.attack(field_taken)):
                    self._point.move(self._input)

    def user_input(self, n=1):
        event = self._world.get_input()
        if (event is None):
            return self._input
        elif (event.char == event.keysym):
            event = event.char.lower()
        elif (len(event.char) == 1):
            return self._input
        else:
            event = event.keysym

        if (event == 'q'):
            if (self._skill_cooldown == 0):
                self._world.add_turn_info(
                    "Alzur's shield has been activated for %d turns\n" % (df.const.HUMAN_SKILL_TIME))
                return 'q'
            elif (self._skill_cooldown > df.const.HUMAN_SKILL_TIME):
                self._world.add_turn_info("Alzur's shield is still active for %d turns\n" % (
                        self._skill_cooldown - df.const.HUMAN_SKILL_TIME))
            else:
                self._world.add_turn_info(
                    "You have to wait %d turns to activate Alzur's shield\n" % (self._skill_cooldown))

        else:
            if (event == df.const.HEX_TOP or event == df.const.RECT_TOP):  # TOP
                if (self._point.get_y() - n >= 0):  # TOP
                    return Direction.TOP

            elif (event == df.const.HEX_DOWN or event == df.const.RECT_DOWN):  # DOWN
                if (self._point.get_y() + n < self._world.get_height()):  # DOWN
                    return Direction.DOWN

            if (self._world.get_board_type() == df.const.RECTANGLE):  # RECTANGLE

                if (event == df.const.RECT_LEFT and self._point.get_x() - n >= 0):  # LEFT
                    return Direction.LEFT
                elif (event == df.const.RECT_RIGHT and self._point.get_x() + n < self._world.get_width()):  # RIGHT
                    return Direction.RIGHT
            else:  # HEXAGON
                if (self._point.get_x() % 2 == 1):  # odd
                    if (event == df.const.HEX_LEFT_TOP):  # LEFT
                        return Direction.LEFT
                    elif (event == df.const.HEX_RIGHT_TOP):  # RIGHT
                        return Direction.RIGHT
                    elif (event == df.const.HEX_LEFT_DOWN):  # LEFT DOWN
                        return Direction.LEFT_DOWN
                    elif (event == df.const.HEX_RIGHT_DOWN):  # RIGHT DOWN
                        return Direction.RIGHT_DOWN
                else:  # even
                    if (event == df.const.HEX_LEFT_TOP):  # TOP LEFT
                        return Direction.LEFT_TOP
                    elif (event == df.const.HEX_RIGHT_TOP):  # TOP RIGHT
                        return Direction.RIGHT_TOP
                    elif (event == df.const.HEX_LEFT_DOWN):  # LEFT
                        return Direction.LEFT
                    elif (event == df.const.HEX_RIGHT_DOWN):  # RIGHT
                        return Direction.RIGHT


    def __str__(self):
        return "Human"

    def draw(self, color=None):
        if (color is None):
            if (self._skill_cooldown == 0):
                color = self._color  # availabe
            elif (self._skill_cooldown > df.const.HUMAN_SKILL_TIME):
                color = self._color_active  # active
            else:
                color = self._color_inactive

        super(Animal, self).draw(color)  # cooldown

    def save(self):
        return "%c %d %d %d %d %d %d\n" % (
            self._sign, self._point.get_x(), self._point.get_y(), self._age, self._id, self._strength,
            self._skill_cooldown)

