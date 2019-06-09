from Plants.Plant import Plant
import Organism
import Point
import World
import Const as df


class Guarana(Plant):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.GUARANA_STRENGTH):
        super(Guarana, self).__init__(world,
                                      point,
                                      df.const.GUARANA_SIGN,
                                      df.const.GUARANA_COLOR,
                                      strength,
                                      df.const.GUARANA_SPREAD,
                                      age,
                                      id1)

    def collision(self, attacker):
        attacker.increase_strength(df.const.GUARANA_BONUS_GIVEN)  # increase strength by bonus (default 3)
        self.set_is_alive(False)
        self._world.add_turn_info(
            "%s strength is now %s. %s has been eaten\n" % (attacker, attacker.get_strength(), self))

    def spread(self):
        free_place = self._world.random_free_place(self)
        success = free_place is not None
        if (success and self._is_alive):
            self._world.add_organism(Guarana(self._world, free_place))
            self.spread_description()

    def __str__(self):
        return "Guarana"
