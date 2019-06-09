from Animals.Animal import Animal
import Const as df
from Point import Point
import random as rand


class Fox(Animal):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.FOX_STRENGTH):
        super(Fox, self).__init__(world,
                                  point,
                                  df.const.FOX_SIGN,
                                  df.const.FOX_COLOR,
                                  strength,
                                  df.const.FOX_PRIORITY,
                                  age,
                                  id1)

    def __str__(self):
        return "Fox"

    def action(self):
        #if (self._age == 0):
        #    self._age += 1
        #elif (self._is_alive):
        self._age += 1
        all_dir = super(Fox, self).all_directions()

        do_while = True
        while True:
            rand_num = rand.randint(0, len(all_dir) - 1)
            direction = all_dir.pop(rand_num)
            point = Point(self._point.get_x(), self._point.get_y(), direction)
            field_taken = self._world.field_taken(point)

            # searches for free spot (if nothing is free, stays in the same filed)
            do_while = (not all_dir and field_taken is not None and field_taken.get_strength() > self._strength)

            if (do_while is False):
                break

        if (self.attack(field_taken)):
            self._point.move(direction)

    def breeding(self):
        free_place = self._world.random_free_place(self)
        if (free_place is not None):
            self.breeding_description()
            self._world.add_organism(Fox(self._world, free_place))

    def draw(self, color=None):
        if (color is None):
            color = self._color
        super().draw(color)
