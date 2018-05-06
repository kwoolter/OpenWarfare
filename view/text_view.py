import model

class OWObjectColours:

    BLACK = 0
    RED = 1
    BLUE = 4
    CYAN = 6
    GREEN = 2
    WHITE = 8
    GREY = 7

    @staticmethod
    def colour_codes(fg = BLACK, bg = WHITE):
        return "\x1B[" + str(fg+30) + ";" + str(bg+40) +"m"


class OWMapView():

    def __init__(self, game: model.OWGame):
        self.game = game

    def draw_map(self):
        current_map = self.game.current_map

        title = "  " + \
                OWObjectColours.colour_codes(OWObjectColours.RED, OWObjectColours.GREY) + \
                "{0:^" + str(current_map.width) + "}" + \
                OWObjectColours.colour_codes(OWObjectColours.BLACK, OWObjectColours.WHITE)

        print(title.format(current_map.name))

        map_array = current_map.layer_to_array()

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
            row = "  "
            for x in range(len(map_array[y])):
                if map_array[x][y] is not None:
                    row += "*"
                else:
                    row += "_"
            print(row)

        print(header2)
        print(header1)
