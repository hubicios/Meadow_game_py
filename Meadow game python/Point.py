from Direction import Direction
import Const as df
from math import sqrt


class Point:
    def __init__(self, x=0, y=0, direction=Direction.DIRECTION_NONE):
        self._x = x
        self._y = y
        if (direction is not Direction.DIRECTION_NONE.value):  # and direction is not Direction.DIRECTION_NONE):
            self.move(direction)
            # print(self)

    def __str__(self):
        return "(%d,%d)" % (self._x, self._y)

    def move(self, direction, n=1):
        if (direction == Direction.TOP):  # or direction == Direction.TOP.value):
            self._y = self._y - n

        elif (direction == Direction.RIGHT_TOP):  # or direction == Direction.RIGHT_TOP.value):
            self._x = self._x + n
            self._y = self._y - n

        elif (direction == Direction.RIGHT):  # or direction == Direction.RIGHT.value):
            self._x = self._x + n

        elif (direction == Direction.RIGHT_DOWN):  # or direction == Direction.RIGHT_DOWN.value):
            self._x = self._x + n
            self._y = self._y + n

        elif (direction == Direction.DOWN):  # or direction == Direction.DOWN.value):
            self._y = self._y + n

        elif (direction == Direction.LEFT_DOWN):  # or direction == Direction.LEFT_DOWN.value):
            self._x = self._x - n
            self._y = self._y + n

        elif (direction == Direction.LEFT):  # or direction == Direction.LEFT.value):
            self._x = self._x - n

        elif (direction == Direction.LEFT_TOP):  # or direction == Direction.LEFT_TOP.value):
            self._x = self._x - n
            self._y = self._y - n

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_xy(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def equals(self, x, y):
        return (self._x == x and self._y == y)

    def around_point(self, x_neighbour, y_neighbour, board_type):  # check if x_y_neighbour is around point x/y
        good = False
        if (abs(self._x - x_neighbour) <= 1 and abs(self._y - y_neighbour) <= 1):
            good = True

        if (board_type == df.const.HEXAGON):  # HEXAGON
            if (self._x % 2 == 1):  # without left-top and right-top
                if (self._y == y_neighbour + 1 and self._x != x_neighbour):
                    good = False

            else:  # x is even without left-down and right-down
                if (self._y == y_neighbour - 1 and self._x != x_neighbour):
                    good = False

        return good

    def equals_to(self, point):
        return self._x == point.get_x() and self._y == point.get_y()

    def direction_to_point(self, point):
        x = point.get_x()
        y = point.get_y()
        delta_x = abs(self._x - x)
        delta_y = abs(self._y - y)
        if (delta_x > delta_y and delta_x > 0):
            if (x > self._x):
                return Direction.RIGHT
            if (x < self._x):
                return Direction.LEFT
        elif (delta_y > 0):
            if (y > self._y):
                return Direction.DOWN
            if (y < self._y):
                return Direction.TOP
        return None

    def to_hex(self, mx, my, height):
        h = int(height)
        r = int(h / 2)
        R = int(h / sqrt(3))
        x = int(mx / (3 * R / 2))
        y = int((my - (x % 2) * r) / h)
        dx = int(mx - x * (3 * R / 2))
        dy = int(my - y * h)

        if (my - x % 2 * r < 0):
            self._x = -1  # prevent clicking in the open halfhexes at the top of the screen
            self._y = -1
            return

        # even columns
        if (x % 2 == 0):
            if (dy > r):  # bottom half of hexes
                if (dx * r / (R / 2) < dy - r):
                    x -= 1

            if (dy < r):  # top half of hexes
                if (((R / 2) - dx) * r / (R / 2) > dy):
                    x -= 1
                    y -= 1

        else:  # odd columns
            if (dy > h):  # bottom half of hexes
                if (dx * r / (R / 2) < dy - h):
                    x -= 1
                    y += 1

            if (dy < h):  # top half of hexes
                if (((R / 2) - dx) * r / (R / 2) > dy - r):
                    x -= 1

        self.set_xy(int(x), int(y))
