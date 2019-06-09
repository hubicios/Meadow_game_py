from Plants.Plant import Plant
import Organism
import Point
import World
import Const as df


class Belladonna(Plant):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.BELLADONNA_STRENGTH):
        super(Belladonna, self).__init__(world,
                                         point,
                                         df.const.BELLADONNA_SIGN,
                                         df.const.BELLADONNA_COLOR,
                                         strength,
                                         df.const.BELLADONNA_SPREAD,
                                         age,
                                         id1)

    def collision(self, attacker):
        self.deadly_plant_eaten(attacker)

    def spread(self):
        free_place = self._world.random_free_place(self)
        success = free_place is not None
        if (success and self._is_alive):
            self._world.add_organism(Belladonna(self._world, free_place))
            self.spread_description()

    def __str__(self):
        return "Belladonna"
