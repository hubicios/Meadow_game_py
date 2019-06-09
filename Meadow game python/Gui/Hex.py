from math import sqrt


class Hex:

    def __init__(self, height, canvas, height_border=0, width_border=0):
        self._height_border = height_border
        self._width_border = width_border
        self._h = height
        self._r = int(height / 2)
        self._R = int(height / sqrt(3))
        self._canvas = canvas

    def set_borders(self, height_border=0, width_border=0):
        self._height_border = height_border
        self._width_border = width_border

    def set_height(self, height):
        self._h = height  # h = basic dimension: height (distance between two adj centresr aka size)
        self._r = int(height / 2)  # r = radius of inscribed circle
        self._R = int(height / sqrt(3))  # s = (h/2)/cos(30)= (h/2) / (sqrt(3)/2) = h / sqrt(3)

    def get_hex_height(self):
        return self._h

    def hex(self, x0, y0):
        y = y0 + self._height_border
        x = x0 + self._width_border

        if (self._R == 0 or self._h == 0):
            return None

        array = [
            x + self._R / 2,
            y,
            x + self._R * 3 / 2,
            y,
            x + self._R * 2,
            y + self._r,
            x + self._R * 3 / 2,
            y + 2 * self._r,
            x + self._R / 2,
            y + 2 * self._r,
            x,
            y + self._r]
        return array

    def draw_hex(self, i, j):
        x = i * (self._R * 3 / 2)
        y = j * self._h + (i % 2) * self._h / 2
        return self.hex(x, y)
