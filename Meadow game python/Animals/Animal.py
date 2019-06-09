from Direction import Direction
from Organism import Organism
from abc import abstractmethod
import random as rand
import Const as df
from Point import Point


class Animal(Organism):
    def __init__(self, world, point, sign, color, strength, priority, age, id1):
        super(Animal, self).__init__(world, point, sign, color, strength, priority, age, id1)

    def action(self):  # override
        #if (self._age == 0):
        #    self._age += 1
        #elif (self._is_alive):
        self._age += 1
        direction = self.random_direction()
        point = Point(self._point.get_x(), self._point.get_y(), direction)
        field_taken = self._world.field_taken(point)
        if (self.attack(field_taken)):
            self._point.move(direction)

    def collision(self, attacker):  # override
        if (self._strength < attacker.get_strength()):
            self.set_is_alive(False)
            self._world.add_turn_info("%s %s %s\n" % (attacker, "killed ->", self))
        else:
            attacker.set_is_alive(False)
            self._world.add_turn_info("%s %s %s\n" % (attacker, "<- has been killed by", self))

    @abstractmethod
    def breeding(self):
        return

    def breeding_description(self):
        self._world.add_turn_info("New %s has been born\n" % (self))

    def random_direction(self, n=1):
        direction_available = self.all_directions(n)
        if (len(direction_available) > 0):
            random_num = rand.randint(0, len(direction_available) - 1)
            return direction_available[random_num]
        else:
            return Direction.DIRECTION_NONE

    def all_directions(self, n=1):
        x = self._point.get_x()
        y = self._point.get_y()
        direction_available = []
        if (x + n < self._world.get_width()):  # RIGHT

            direction_available.append(Direction.RIGHT)
            if (self._world.get_board_type() == df.const.HEXAGON):
                if (y - n >= 0 and x % 2 == 0):  # RIGHT_TOP

                    direction_available.append(Direction.RIGHT_TOP)

                if (y + n < self._world.get_height() and x % 2 == 1):  # RIGHT_DOWN

                    direction_available.append(Direction.RIGHT_DOWN)

        if (x - n >= 0):  # LEFT

            direction_available.append(Direction.LEFT)
            if (self._world.get_board_type() == df.const.HEXAGON):
                if (y - n >= 0 and x % 2 == 0):  # LEFT_TOP

                    direction_available.append(Direction.LEFT_TOP)

                if (y + n < self._world.get_height() and x % 2 == 1):  # LEFT_DOWN

                    direction_available.append(Direction.LEFT_DOWN)

        if (y - n >= 0):  # TOP

            direction_available.append(Direction.TOP)

        if (y + n < self._world.get_height()):  # DOWN

            direction_available.append(Direction.DOWN)

        return direction_available

    def is_fight_off(self, attacker):
        return False

    def attack(self, defender):
        make_move = True

        if (defender is not None):
            if (defender.get_sign() == self.get_sign()):

                make_move = False
                if (self._age >= df.const.FERTILITY_AGE and defender.get_age() >= df.const.FERTILITY_AGE
                        and self._id is not defender.get_id()):
                    # print(self, self._id, "meets", defender, defender.get_id())
                    self.breeding()

            elif (defender.is_fight_off(self) is True):
                self._world.add_turn_info("%s has fight off %s\n" % (defender, self))
                make_move = False
            else:
                defender.collision(self)
                if (self._is_alive is False):
                    make_move = False
        return make_move

    def draw(self, color=None):
        if (color is None):
            color = self._color
        super().draw(color)
