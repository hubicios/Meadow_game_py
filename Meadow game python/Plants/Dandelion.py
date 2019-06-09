from Plants.Plant import Plant
import Organism
import Point
import World
import Const as df


class Dandelion(Plant):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.DANDELION_STRENGTH):
        super(Dandelion, self).__init__(world,
                                        point,
                                        df.const.DANDELION_SIGN,
                                        df.const.DANDELION_COLOR,
                                        strength,
                                        df.const.DANDELION_SPREAD,
                                        age,
                                        id1)

    def action(self, spread=df.const.DANDELION_SPREAD):
        for i in range(df.const.DANDELION_SPREAD_TIMES):
            super(Dandelion, self).action(spread)

        self._age = self._age - df.const.DANDELION_SPREAD_TIMES + 1

    def spread(self):
        free_place = self._world.random_free_place(self)
        success = free_place is not None
        if (success and self._is_alive):
            self._world.add_organism(Dandelion(self._world, free_place))
            self.spread_description()

    def __str__(self):
        return "Dandelion"
