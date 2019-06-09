from Animals.Animal import Animal
import Const as df
from Animals.Sheep import Sheep
from Point import Point


class CyberSheep(Sheep):

    def __init__(self, world, point, age=0, id1=0, strength=df.const.CYBER_SHEEP_STRENGTH,
                 priority=df.const.CYBER_SHEEP_PRIORITY):
        super(CyberSheep, self).__init__(world,
                                         point,
                                         age,
                                         id1,
                                         strength,
                                         priority,
                                         df.const.CYBER_SHEEP_SIGN,
                                         df.const.CYBER_SHEEP_COLOR)
        self._nothing_to_eat = False #True if every sosnowski's hogweed had been eaten

    # override
    def breeding(self):
        free_place = self._world.random_free_place(self)
        if (free_place is not None):
            self.breeding_description()
            self._world.add_organism(CyberSheep(self._world, free_place))

    # override
    def action(self):

        org_point = self._world.nearest_organism(self.get_point(), df.const.SOSNOWSKIS_HOGWEED_SIGN)
        if (org_point is None):
            super(CyberSheep, self).action()
        else:
            #if (self._age == 0):
            #   self._age += 1
            #elif (self._is_alive):
            self._age += 1

            direction = self._point.direction_to_point(org_point)
            point = Point(self._point.get_x(), self._point.get_y(), direction)
            field_taken = self._world.field_taken(point)
            #if (field_taken is not None and field_taken.get_sign() == df.const.SOSNOWSKIS_HOGWEED_SIGN):
            if (field_taken is None):
                self._nothing_to_eat = True
            if (self.attack(field_taken)):
                self._point.move(direction)

    # override
    def __str__(self):
        return "Cyber Sheep"

    def draw(self, color=None):
        if (color is None):
            color = self._color

        super(Animal, self).draw(color)
