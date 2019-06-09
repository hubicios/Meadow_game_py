from Animals.Animal import Animal
import Const as df


class Sheep(Animal):

    def __init__(self, world, point, age=0, id1=0, strength=df.const.SHEEP_STRENGTH, priority=df.const.SHEEP_PRIORITY,
                 sign=df.const.SHEEP_SIGN, color=df.const.SHEEP_COLOR):
        super(Sheep, self).__init__(world,
                                    point,
                                    sign,
                                    color,
                                    strength,
                                    priority,
                                    age,
                                    id1)

    # override
    def breeding(self):

        free_place = self._world.random_free_place(self)
        if (free_place is not None):  # and self._world.field_taken(free_place) is False):
            self.breeding_description()
            self._world.add_organism(Sheep(self._world, free_place))

    # override
    def __str__(self):
        return "Sheep"

    def draw(self, color=None):
        if (color is None):
            color = self._color
        super().draw(color)
