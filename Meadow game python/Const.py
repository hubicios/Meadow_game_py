from pconst import const

# human
const.HUMAN_COLOR_AVAILABLE = "RoyalBlue2"  # skill available
const.HUMAN_COLOR_ACTIVE = "blue"  # skill active
const.HUMAN_COLOR_INACTIVE = "blue4"  # skill cooldown
const.HUMAN_SIGN = 'H'
const.HUMAN_STRENGTH = 5
const.HUMAN_PRIORITY = 4
const.HUMAN_SKILL_TIME = 5
# wolf
const.WOLF_COLOR = "red"
const.WOLF_SIGN = 'W'
const.WOLF_STRENGTH = 9
const.WOLF_PRIORITY = 5
# sheep
const.SHEEP_COLOR = "snow"
const.SHEEP_SIGN = 'O'
const.SHEEP_STRENGTH = 4
const.SHEEP_PRIORITY = 4
# cyber sheep
const.CYBER_SHEEP_COLOR = "navajo white"
const.CYBER_SHEEP_SIGN = 'C'
const.CYBER_SHEEP_STRENGTH = 11
const.CYBER_SHEEP_PRIORITY = 4
# fox
const.FOX_COLOR = "DarkOrange1"
const.FOX_SIGN = 'L'
const.FOX_STRENGTH = 3
const.FOX_PRIORITY = 7
# tortoise
const.TORTOISE_COLOR = "SeaGreen3"
const.TORTOISE_SIGN = 'Z'
const.TORTOISE_STRENGTH = 2
const.TORTOISE_PRIORITY = 1
# antelope
const.ANTELOPE_COLOR = "saddle brown"
const.ANTELOPE_SIGN = 'A'
const.ANTELOPE_STRENGTH = 4
const.ANTELOPE_PRIORITY = 4
const.ANTELOPE_JUMP = 2
# grass
const.GRASS_COLOR = "lawn green"
const.GRASS_SIGN = 't'
const.GRASS_STRENGTH = 0
const.GRASS_SPREAD = 0.02
# dandelion
const.DANDELION_COLOR = "gold"
const.DANDELION_SIGN = 'm'
const.DANDELION_STRENGTH = 0
const.DANDELION_SPREAD = 0.02
const.DANDELION_SPREAD_TIMES = 3
# guarana
const.GUARANA_COLOR = "purple"
const.GUARANA_SIGN = 'g'
const.GUARANA_STRENGTH = 0
const.GUARANA_SPREAD = 0.02
const.GUARANA_BONUS_GIVEN = 3
# belladonna
const.BELLADONNA_COLOR = "maroon1"
const.BELLADONNA_SIGN = 'j'
const.BELLADONNA_STRENGTH = 99
const.BELLADONNA_SPREAD = 0.03
# sosnowski's hogweed
const.SOSNOWSKIS_HOGWEED_COLOR = "red3"
const.SOSNOWSKIS_HOGWEED_SIGN = 'b'
const.SOSNOWSKIS_HOGWEED_STRENGTH = 10
const.SOSNOWSKIS_HOGWEED_SPREAD = 0.01

const.ALL_SIGNS = [const.HUMAN_SIGN,
                   const.ANTELOPE_SIGN,
                   const.CYBER_SHEEP_SIGN,
                   const.FOX_SIGN,
                   const.SHEEP_SIGN,
                   const.TORTOISE_SIGN,
                   const.WOLF_SIGN,
                   const.BELLADONNA_SIGN,
                   const.DANDELION_SIGN,
                   const.GRASS_SIGN,
                   const.GUARANA_SIGN,
                   const.SOSNOWSKIS_HOGWEED_SIGN]

const.PLANT_SPREAD = 0.02

const.FERTILITY_AGE = 10  # min age to make organizm

const.MAX_BOARD_SIZE = 50
const.MIN_BOARD_SIZE = 10
const.RECTANGLE = 'R'
const.HEXAGON = 'H'
# const.POPULATION_DENSITY = 2 # 1-low 2-medium 3-high

const.WINDOW_WIDTH = 1280
const.WINDOW_HEIGHT = 1000
const.MENU_HEIGHT = 95
const.SPACING = 2
const.WINDOW_SIDE_BORDER = 8
const.WINDOW_TOP_BORDER = 31
const.DEFAULT_FIELD_COLOR = "gray50"
const.DEFAULT_FIELD_HEX_COLOR = (80, 80, 80, 200)
const.DEFAULT_BOARD_COLOR = (66, 66, 66, 255)
const.BUTTON_FOREGROUND = (0, 0, 0, 255)
const.BUTTON_BACKGROUND = (255, 255, 255, 255)
const.BORDERS = 5

const.QUIT = -1
const.NEW_GAME = 0
const.LOAD_GAME = 1
const.DEFAULT_COLOR = "gray35"

const.SAVE_FILE_NAME = "save\\save.txt"

const.CLEAR_LOG = True

const.HEX_TOP = 's'
const.HEX_RIGHT_TOP = 'd'
const.HEX_RIGHT_DOWN = 'c'
const.HEX_DOWN = 'x'
const.HEX_LEFT_DOWN = 'z'
const.HEX_LEFT_TOP = 'a'

const.RECT_TOP = "Up"
const.RECT_RIGHT = "Right"
const.RECT_DOWN = "Down"
const.RECT_LEFT = "Left"
