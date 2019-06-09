import math
import numpy as np

import Const as df
import Animals
import Plants
from Animals.Antelope import Antelope
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.CyberSheep import CyberSheep
from Animals.Wolf import Wolf
from Animals.Fox import Fox
from Animals.Tortoise import Tortoise

from Plants.SosnowskisHogweed import SosnowskisHogweed
from Plants.Guarana import Guarana
from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Belladonna import Belladonna

from Point import Point
from Direction import Direction
import random as rand


class World:
    def __init__(self, width, height, turn_counter=0, board_type=df.const.RECTANGLE):
        self._width = width
        self._height = height
        self._turn_counter = turn_counter
        self._board_type = board_type
        self._input = None
        self._to_draw = np.empty((height, width), dtype='O')
        self._turn_info = []
        self._organisms = []
        self._turn_description = []
        self.TurnInfoListener = None

    def get_input(self):
        return self._input

    def set_input(self, input1):
        self._input = input1

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_fields_color(self):
        return self._to_draw

    def set_field_color(self, point, color):
        x = point.get_x()
        y = point.get_y()
        if (x < self._width and y < self._height):
            self._to_draw[y][x] = color

    def set_default_colors(self):
        for x in range(self._width):
            for y in range(self._height):
                self._to_draw[y][x] = df.const.DEFAULT_FIELD_COLOR

    def change_board_type(self):  # TODO DEFAULT_RECTANGLE
        if (self._board_type == df.const.RECTANGLE):
            self._board_type = df.const.HEXAGON
        elif (self._board_type == df.const.HEXAGON):
            self._board_type = df.const.RECTANGLE

    def get_board_type(self):
        return self._board_type

    def set_board_type(self, board_type):
        self._board_type = board_type

    def init_world(self, exist=False):
        if (exist is False):
            self.generate_organisms()
            self.sort_organisms()
        self.draw_organisms()

    def make_turn(self):
        self.set_default_colors()
        self._turn_counter += 1
        self.sort_organisms()  # organisms are prepared for the beginning of the new
        for organism in self._organisms:
            organism.action()

        self.delete_organisms()
        self.draw_organisms()
        self.add_turn_info("Turn number %d\n" % (self._turn_counter))

        # self.show_organisms()

    def draw_organisms(self):
        self.set_default_colors()
        for organism in self._organisms:
            organism.draw()

    def sort_organisms(self):
        self._organisms.sort(key=lambda l: (l.get_priority(), l.get_age()), reverse=True)

    def generate_organisms(self):
        points = []
        for x in range(self._width):
            for y in range(self._height):
                points.append(Point(x, y))

        rand_num = rand.randint(0, len(points) - 1)
        self.generate_organism(points.pop(rand_num), df.const.ALL_SIGNS[0])
        ###########test
        '''rand_num = rand.randint(0, len(points) - 1)
        self.generate_organism(points.pop(rand_num), df.const.ALL_SIGNS[2])
        rand_num = rand.randint(0, len(points) - 1)
        self.generate_organism(points.pop(rand_num), df.const.ALL_SIGNS[11])
        '''
        ###########test

        if (self._width + self._height > 2):
            for i in range(int((self._width * self._height) / (len(df.const.ALL_SIGNS) * 3) + 1)):
                for j in range(1, len(df.const.ALL_SIGNS)):
                    rand_num = rand.randint(0, len(points) - 1)
                    self.generate_organism(points.pop(rand_num), df.const.ALL_SIGNS[j])

    def generate_organism(self, point: Point, species):
        if (species == df.const.ANTELOPE_SIGN):
            self._organisms.append(Antelope(self, point))

        elif (species == df.const.HUMAN_SIGN):
            self._organisms.append(Human(self, point))

        elif (species == df.const.GUARANA_SIGN):
            self._organisms.append(Guarana(self, point))

        elif (species == df.const.FOX_SIGN):
            self._organisms.append(Fox(self, point))

        elif (species == df.const.DANDELION_SIGN):
            self._organisms.append(Dandelion(self, point))

        elif (species == df.const.SHEEP_SIGN):
            self._organisms.append(Sheep(self, point))

        elif (species == df.const.CYBER_SHEEP_SIGN):
            self._organisms.append(CyberSheep(self, point))

        elif (species == df.const.GRASS_SIGN):
            self._organisms.append(Grass(self, point))

        elif (species == df.const.BELLADONNA_SIGN):
            self._organisms.append(Belladonna(self, point))

        elif (species == df.const.WOLF_SIGN):
            self._organisms.append(Wolf(self, point))

        elif (species == df.const.TORTOISE_SIGN):
            self._organisms.append(Tortoise(self, point))
        elif (species == df.const.SOSNOWSKIS_HOGWEED_SIGN):
            self._organisms.append(SosnowskisHogweed(self, point))

    def add_organism(self, organism):
        self._organisms.append(organism)

    def delete_organisms(self):
        self._organisms[:] = [org for org in self._organisms if org.get_is_alive()]


    def num_of_organisms(self):
        return len(self._organisms)

    def nearest_organism(self, point, sign):
        x = point.get_x()
        y = point.get_y()
        distance = None
        org_x = None
        org_y = None
        for org in self._organisms:
            if (org.get_sign() == sign):
                org_x_temp = org.get_point().get_x()
                org_y_temp = org.get_point().get_y()
                temp_distance = abs(x - org_x_temp) + abs(y - org_y_temp)
                if (distance is None or distance > temp_distance):
                    distance = temp_distance
                    org_x = org_x_temp
                    org_y = org_y_temp

        if (distance is not None):
            return Point(org_x, org_y)
        return None

    def neighbours(self, org):
        neighbours_organism = []
        for organism in self._organisms:
            x_neighbour = organism.get_point().get_x()
            y_neighbour = organism.get_point().get_y()
            if (organism.get_is_alive() and organism.get_id() != org.get_id() and org.get_point().around_point(
                    x_neighbour, y_neighbour, self._board_type)):
                neighbours_organism.append(organism)
        return neighbours_organism

    def neighbours_num(self, org):
        sum_of = 0
        for organism in self._organisms:
            x_neighbour = organism.get_point().get_x()
            y_neighbour = organism.get_point().get_y()
            if (organism.get_is_alive() and organism.get_id() != org.get_id() and org.get_point().around_point(
                    x_neighbour, y_neighbour, self._board_type)):
                sum_of += 1
        return sum_of

    def random_free_place(self, org, n=1):
        num = 8
        free = [True] * num
        x = org.get_point().get_x()
        y = org.get_point().get_y()
        q = 0
        # *********************
        if (y - n < 0):  # TOP
            free[q] = False
        else:
            free[q] = self.field_free(x, y - n)

        q += 1
        if (x + n >= self._width or y - n < 0 or (self._board_type == df.const.HEXAGON and x % 2 == 1)):  # RIGHT_TOP
            free[q] = False
        else:
            free[q] = self.field_free(x + n, y - n)

        q += 1
        if (x + n >= self._width):  # RIGHT
            free[q] = False
        else:
            free[q] = self.field_free(x + n, y)

        q += 1
        if (x + n >= self._width or y + n >= self._height or (
                self._board_type == df.const.HEXAGON or x % 2 == 0)):  # RIGHT_DOWN
            free[q] = False
        else:
            free[q] = self.field_free(x + n, y + n)

        q += 1
        if (y + n >= self._height):  # DOWN
            free[q] = False
        else:
            free[q] = self.field_free(x, y + n)

        q += 1
        if (x - n < 0 or y + n >= self._height or (self._board_type == df.const.HEXAGON or x % 2 == 0)):  # LEFT_DOWN
            free[q] = False
        else:
            free[q] = self.field_free(x - n, y + n)

        q += 1
        if (x - n < 0):  # LEFT
            free[q] = False
        else:
            free[q] = self.field_free(x - n, y)

        q += 1
        if (x - n < 0 or y - n < 0 or (self._board_type == df.const.HEXAGON or x % 2 == 1)):  # LEFT_TOP
            free[q] = False
        else:
            free[q] = self.field_free(x - n, y - n)

        # ***************************

        directions = []
        for i in range(num):
            if (free[i] is True):
                directions.append(i)
        if (not directions):
            return None
        if (directions):
            rand_num = rand.randint(0, len(directions) - 1)
            # print(directions[rand_num])
            return Point(x, y, Direction(directions.pop(rand_num)))

    def field_taken(self, point):
        x = point.get_x()
        y = point.get_y()

        for organism in self._organisms:
            if (organism.get_point().equals(x, y) and organism.get_is_alive()):
                return organism
        return None

    def field_free(self, x, y):
        for organism in self._organisms:
            if (organism.get_point().equals(x, y)):
                return False
        return True

    def add_turn_info_listener(self, TurnInfoListener):
        self.TurnInfoListener = TurnInfoListener

    def add_turn_info(self, text):
        self.TurnInfoListener(text)

    def show_organisms(self):
        print("########################")
        for org in self._organisms:
            print(org, org.get_id(), org.get_point())
        print("########################")

    def save_game(self):
        file = open(df.const.SAVE_FILE_NAME, "w+")
        file.write("%d %d %d %c\n" % (self._width, self._height, self._turn_counter, self._board_type))
        for org in self._organisms:
            file.write(org.save())
        file.close
        self.add_turn_info("Game has been saved successfully\n\n")

    def load_organism(self, line):
        text = line.split()
        age = int(text[3])
        id1 = int(text[4])
        strength = int(text[5])
        point = Point(int(text[1]), int(text[2]))
        species = text[0]

        if (species == df.const.ANTELOPE_SIGN):
            self._organisms.append(Antelope(self, point, age, id1, strength))

        elif (species == df.const.SOSNOWSKIS_HOGWEED_SIGN):
            self._organisms.append(SosnowskisHogweed(self, point, age, id1, strength))

        elif (species == df.const.HUMAN_SIGN):
            self._organisms.append(Human(self, point, age, id1, strength, int(text[6])))

        elif (species == df.const.GUARANA_SIGN):
            self._organisms.append(Guarana(self, point, age, id1, strength))

        elif (species == df.const.FOX_SIGN):
            self._organisms.append(Fox(self, point, age, id1, strength))

        elif (species == df.const.DANDELION_SIGN):
            self._organisms.append(Dandelion(self, point, age, id1, strength))

        elif (species == df.const.SHEEP_SIGN):
            self._organisms.append(Sheep(self, point, age, id1, strength))

        elif (species == df.const.CYBER_SHEEP_SIGN):
            self._organisms.append(CyberSheep(self, point, age, id1, strength))

        elif (species == df.const.GRASS_SIGN):
            self._organisms.append(Grass(self, point, age, id1, strength))

        elif (species == df.const.BELLADONNA_SIGN):
            self._organisms.append(Belladonna(self, point, age, id1, strength))

        elif (species == df.const.WOLF_SIGN):
            self._organisms.append(Wolf(self, point, age, id1, strength))

        elif (species == df.const.TORTOISE_SIGN):
            self._organisms.append(Tortoise(self, point, age, id1, strength))
