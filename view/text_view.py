import model

class OWObjectColours:

    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    GREY = 7
    WHITE = 8

    BRIGHT_RED = RED + 60
    BRIGHT_GREEN = GREEN +60
    BRIGHT_YELLOW = YELLOW + 60
    BRIGHT_BLUE = BLUE + 60
    BRIGHT_MAGENTA = MAGENTA + 60
    BIGHT_CYAN = CYAN + 60
    BRIGHT_GREY = GREY + 60
    BRIGHT_WHITE = WHITE + 60

    @staticmethod
    def colour_codes(fg = BLACK, bg = WHITE):
        return "\x1B[" + str(fg+30) + ";" + str(bg+40) +"m"

class OWObjectGraphics:

    object_to_char = {

        model.PLAYER : "&",
        model.HOUSE : "#",
        model.TREE : "T"

    }

    object_to_colour = {

        model.GRASS : OWObjectColours.GREEN,
        model.BRICK : OWObjectColours.RED,
        model.WATER : OWObjectColours.BLUE,

        model.PLAYER : OWObjectColours.BLACK,
        model.TREE : OWObjectColours.BRIGHT_RED,
        model.HOUSE : OWObjectColours.BRIGHT_GREY,

    }

class OWMapView():



    def __init__(self, game: model.OWGame):
        self.game = game

    def draw_map(self):
        current_map = self.game.current_map

        title = "  " + \
                OWObjectColours.colour_codes(OWObjectColours.BRIGHT_RED, OWObjectColours.GREY) + \
                "{0:^" + str(current_map.width) + "}" + \
                OWObjectColours.colour_codes(OWObjectColours.BLACK, OWObjectColours.WHITE)

        print(title.format(current_map.name))

        map_array = current_map.layer_to_array()
        map_floor = current_map.layer_to_array(model.OWMap.FLOOR_LAYER)

        header1 = OWObjectColours.colour_codes(bg=OWObjectColours.WHITE) + "  "+ OWObjectColours.colour_codes(bg=OWObjectColours.CYAN)
        header2 = header1

        for x in range(current_map.width):
            if x % 10 == 0:
                header1 += str(x // 10)
            else:
                header1 += " "
            header2 += str(x % 10)

        header1 += OWObjectColours.colour_codes(bg=OWObjectColours.WHITE)
        header2 += OWObjectColours.colour_codes(bg=OWObjectColours.WHITE)

        print(header1)
        print(header2)

        for y in range(len(map_array)):

            row = OWObjectColours.colour_codes(fg=OWObjectColours.BLACK, bg=OWObjectColours.GREY)
            if y % 10 == 0:
                row += str(y // 10)
            else:
                row += " "
            row += str(y % 10)

            for x in range(len(map_array[y])):
                obj = map_array[x][y]
                base = map_floor[x][y]
                if obj is not None:
                    if obj.name in OWObjectGraphics.object_to_char.keys():

                        row += OWObjectColours.colour_codes(fg=OWObjectGraphics.object_to_colour[obj.name],
                                                            bg=OWObjectGraphics.object_to_colour[base.name])

                        row += OWObjectGraphics.object_to_char[obj.name]
                    else:
                        row += OWObjectColours.colour_codes(bg=OWObjectGraphics.object_to_colour[base.name])
                        row += "?"
                else:
                    row += OWObjectColours.colour_codes(bg=OWObjectGraphics.object_to_colour[base.name])
                    row += " "


            row += OWObjectColours.colour_codes(fg=OWObjectColours.BLACK, bg=OWObjectColours.GREY)
            row += str(y % 10)
            if y % 10 == 0:
                row += str(y // 10)
            else:
                row += " "
            row +=  OWObjectColours.colour_codes(bg=OWObjectColours.WHITE)

            print(row)

        print(header2)
        print(header1)
