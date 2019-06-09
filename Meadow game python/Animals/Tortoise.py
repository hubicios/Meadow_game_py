from Animals.Animal import Animal
import Const as df
import random as rand


class Tortoise(Animal):
    def __init__(self, world, point, age=0, id1=0, strength=df.const.TORTOISE_STRENGTH):
        super(Tortoise, self).__init__(world,
                                       point,
                                       df.const.TORTOISE_SIGN,
                                       df.const.TORTOISE_COLOR,
                                       strength,
                                       df.const.TORTOISE_PRIORITY,
                                       age,
                                       id1)

    # override
    def breeding(self):
        free_place = self._world.random_free_place(self)
        if (free_place is not None):
            self.breeding_description()
            self._world.add_organism(Tortoise(self._world, free_place))

    # override
    def is_fight_off(self, attacker):
        return (attacker.get_strength() < self._strength)

    # override
    def __str__(self):
        return "Tortoise"

    # override
    def action(self):
        if (self._age == 0):
            self._age += 1
        else:
            rand_num = rand.randint(1, 4)
            if (rand_num == 1):  # 25% chances to move
                super().action()
            else:
                self._age += 1

    # override
    # def collision(self,attacker):
    #   super.collision(attacker)
