import Direction
from Organism import Organism
from abc import abstractmethod
import random as rand
import Const as df
from Point import Point


class Plant(Organism):
    def __init__(self, world, point, sign, color, strength, spread, age, id1):
        super(Plant, self).__init__(world, point, sign, color, strength, 0, age, id1)
        self._spread = spread

    def get_spread(self):
        return self._spread

    def set_spread(self, spread):
        self._spread = spread

    def action(self, spread=None):
        if (spread is None):
            spread = self._spread
        base = 1000
        rand_num = rand.randint(0, base - 1)
        if (rand_num < spread * base and self._age >= df.const.FERTILITY_AGE):
            self.spread()
        self._age += 1

    def collision(self, attacker):
        if (self._strength < attacker.get_strength()):
            self.set_is_alive(False)
            self._world.add_turn_info("%s destroyed %s\n" % (attacker, self))
        else:
            attacker.set_is_alive(False)
            self._world.add_turn_info("%s has been destroyed by %s\n" % (attacker, self))

    def deadly_plant_eaten(self, attacker):
        self.set_is_alive(False)
        if (self._strength > attacker.get_strength()):
            attacker.set_is_alive(False)
            self._world.add_turn_info("%s skilled himself by eating %s\n" % (attacker, self))
        else:
            self._world.add_turn_info("%s has eaten %s but manage to survive\n" % (attacker, self))

    @abstractmethod
    def spread(self):
        return

    def spread_description(self):
        self._world.add_turn_info("New %s\n" % (self))

    def is_fight_off(self, attacker):
        return False

    @abstractmethod
    def __str__(self):
        return "Plant"
