from Plants.Plant import Plant
import Organism
import Point
import World
import Const as df


class Grass(Plant):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.GRASS_STRENGTH):
        super(Grass, self).__init__(world,
                                    point,
                                    df.const.GRASS_SIGN,
                                    df.const.GRASS_COLOR,
                                    strength,
                                    df.const.GRASS_SPREAD,
                                    age,
                                    id1)

    def spread(self):
        free_place = self._world.random_free_place(self)
        success = free_place is not None
        if (success and self._is_alive):
            self._world.add_organism(Grass(self._world, free_place))
            self.spread_description()

    def __str__(self):
        return "Grass"
