import logging
import model.objects as OWobjects

class OWMapObject():
    def __init__(self, name : str, x : int, y : int):
        self.name = name
        self.x = x
        self.y = y

class OWMap():

    FLOOR_LAYER = 0
    ENVIRONMENT_LAYER = 1

    def __init__(self, name: str, width : int = 10, height : int = 10):

        self.name = name
        self.width = width
        self.height = height

        self._layers = None

    def initialise(self):
        self._layers = []
        for i in range(2):
            self._layers.append([])


    def add_object(self, new_object : OWMapObject, layer_id : int = ENVIRONMENT_LAYER):

        self._layers[layer_id].append(new_object)

    def initialise_floor(self, floor_object_type : str):

        for y in range(self.height):
            for x in range(self.width):
                new_object = OWMapObject(floor_object_type, x, y)
                self.add_object(new_object, OWMap.FLOOR_LAYER)

    def print(self):
        if self._layers is None:
            raise Exception("No layers defined for map {0}".format(self.name))

    def __str__(self):
        return("Map:{0} ({1},{2})".format(self.name,self.width, self.height))


class OWMapFactory():

    def __init__(self):
        self._maps = None

    def initialise(self):
        self.load_maps()

    def load_maps(self):

        self._maps = {}

        new_map = OWMap("The Field", 20, 20)
        new_map.initialise()
        new_map.initialise_floor(OWobjects.GRASS)

        self._maps[new_map.name] = new_map

        new_map = OWMap("The Town", 20, 20)
        new_map.initialise()
        new_map.initialise_floor(OWobjects.BRICK)

        self._maps[new_map.name] = new_map

    def print(self):
        for map in self._maps.values():
            print(str(map))