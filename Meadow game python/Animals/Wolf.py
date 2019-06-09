from Animals.Animal import Animal
import Const as df


class Wolf(Animal):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.WOLF_STRENGTH):
        super(Wolf, self).__init__(world,
                                   point,
                                   df.const.WOLF_SIGN,
                                   df.const.WOLF_COLOR,
                                   strength,
                                   df.const.WOLF_PRIORITY,
                                   age,
                                   id1)

    # override
    def breeding(self):
        free_place = self._world.random_free_place(self)
        if (free_place is not None):  # and self._world.field_taken(free_place) is False):
            self.breeding_description()
            self._world.add_organism(Wolf(self._world, free_place))

    # override
    def __str__(self):
        return "Wolf"

    def draw(self, color=None):
        if (color is None):
            color = self._color
        super().draw(color)
