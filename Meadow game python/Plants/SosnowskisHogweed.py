from Plants.Plant import Plant
import Organism
import Point
import World
import Const as df


class SosnowskisHogweed(Plant):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.SOSNOWSKIS_HOGWEED_STRENGTH):
        super(SosnowskisHogweed, self).__init__(world,
                                                point,
                                                df.const.SOSNOWSKIS_HOGWEED_SIGN,
                                                df.const.SOSNOWSKIS_HOGWEED_COLOR,
                                                strength,
                                                df.const.SOSNOWSKIS_HOGWEED_SPREAD,
                                                age,
                                                id1)

    def collision(self, attacker):
        self.set_is_alive(False)
        attacker.set_is_alive(False)
        self._world.add_turn_info("%s killed himself by eating %s\n" % (attacker, self))

    def action(self, spread=df.const.SOSNOWSKIS_HOGWEED_SPREAD):
        neighbours = self._world.neighbours(self)
        for nghbr in neighbours:
            if (nghbr.get_sign() != self.get_sign() and nghbr.get_sign() != df.const.CYBER_SHEEP_SIGN):
                nghbr.collision(self)
                #nghbr.set_is_alive(False)
                #self._world.add_turn_info("%s killed -> %s\n" % (self, nghbr))

        self._age += 1
        super(SosnowskisHogweed, self).action(spread)

    def spread(self):
        free_place = self._world.random_free_place(self)
        success = free_place is not None
        if (success and self._is_alive):
            self._world.add_organism(SosnowskisHogweed(self._world, free_place))
            self.spread_description()

    def collision(self, attacker):
        self.deadly_plant_eaten(attacker)

    def __str__(self):
        return "Sosnowski's Hogweed"
