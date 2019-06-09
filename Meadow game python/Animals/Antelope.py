from Animals.Animal import Animal
import Const as df
from Point import Point
import random as rand


class Antelope(Animal):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.ANTELOPE_STRENGTH):
        super(Antelope, self).__init__(world,
                                       point,
                                       df.const.ANTELOPE_SIGN,
                                       df.const.ANTELOPE_COLOR,
                                       strength,
                                       df.const.ANTELOPE_PRIORITY,
                                       age,
                                       id1)

    def __str__(self):
        return "Antelope"

    def draw(self, color=None):
        if (color is None):
            color = self._color
        super().draw(color)

    def action(self):
        #if (self._age == 0):
        #    self._age += 1
        #elif (self._is_alive):
        self._age += 1
        direction = self.random_direction(df.const.ANTELOPE_JUMP)
        point = Point(self._point.get_x(), self._point.get_y(), direction)
        field_taken = self._world.field_taken(point)

        if (self.attack(field_taken)):
            self._point.move(direction, df.const.ANTELOPE_JUMP)

    def breeding(self):
        free_place = self._world.random_free_place(self)
        if (free_place is not None):
            self.breeding_description()
            self._world.add_organism(Antelope(self._world, free_place))

    def collision(self, attacker):
        random_num = rand.randint(0, 1)
        if (random_num == 0):  # antelope stays #50% chances

            if (self._strength < attacker.get_strength()):
                self.set_is_alive(False)
                self._world.add_turn_info("%s killed -> %s\n" % (attacker, self))
            else:
                attacker.set_is_alive(False)
                self._world.add_turn_info("%s <- has been killed by %s\n" % (attacker, self))

        else:  # runs to nearest field

            free_place = self._world.random_free_place(self)
            if (free_place is not None):
                self._point.set_xy(free_place.get_x(), free_place.get_y())
                self._world.add_turn_info("%s has escaped from %s\n" % (self, attacker))

            else:
                super(Antelope, self).collision(attacker)
                # not a single field was free
