from abc import ABC, abstractmethod


class Organism(ABC):
    num_of = 0

    def __init__(self, world, point, sign, color, strength, priority, age=0, id1=num_of):
        self._world = world
        self._point = point
        self._color = color
        self._sign = sign
        self._strength = strength
        self._priority = priority
        self._age = age
        self._is_alive = True
        self._id = id1

        if (id1 > Organism.num_of):
            Organism.num_of = id1

        Organism.num_of += 1
        self._id = Organism.num_of

    def get_strength(self):
        return self._strength

    def set_strength(self, strength):
        self._strength = strength

    def increase_strength(self, add):
        self._strength += add

    def get_priority(self):
        return self._priority

    def get_sign(self):
        return self._sign

    def get_color(self):
        return self._color

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def increase_age(self):
        self._age += 1

    def get_id(self):
        return self._id

    def set_id(self, id1):
        self._id = id1

    def get_is_alive(self):
        return self._is_alive

    def set_is_alive(self, is_alive):
        self._is_alive = is_alive
        if (self._is_alive is False):
            self._point.set_xy(-1, -1)

    def get_point(self):
        return self._point

    def save(self):
        return "%c %d %d %d %d %d\n" % (
            self._sign, self._point.get_x(), self._point.get_y(), self._age, self._id, self._strength)

    # public abstract String toString()
    @abstractmethod
    def action(self):
        return

    @abstractmethod
    def collision(self, attacker):
        return

    @abstractmethod
    def is_fight_off(self, attacker):  # checks if attack was countered
        return

    def draw(self, color=None):
        if (color is None):
            color = self._color
        if (self._is_alive is True):
            self._world.set_field_color(self._point, color)
