import logging
import os
import random
import model.character as OWcharacter
import model.weapons as OWweapons
import model.maps as OWMaps
import utils.trpg as trpg

class OWGame():

    GAME_DATA_DIR = os.path.dirname(__file__) + "\\data\\"

    def __init__(self):
        self.characters = []
        self._weapons = None
        self._maps = None

    def initialise(self):
        print("Initialising Game...")

        self.load_weapons("weapons.csv")
        self.load_characters()
        self.load_maps()

    def load_characters(self):

        print("Loading characters...")

        names = ["Jack", "Keith", "Rosie", "Honey", "Dave", "Bill"]
        for i in range(4):
            name = random.choice(names)
            new_char = OWcharacter.OWCharacter(name)
            self.characters.append(new_char)
            names.remove(name)

    def load_weapons(self, file_name):

        print("Loading weapons...")

        self._weapons = {}

        weapon_data = trpg.RPGCSVFactory(name="Weapons", file_name=OWGame.GAME_DATA_DIR + file_name)
        weapon_data.load()
        weapons = weapon_data.get_rpg_object_names()

        for weapon in weapons:

            attributes = weapon_data.get_attributes_by_name(weapon)
            print("Attributes for weapon {0}:".format(weapon))
            for attribute, value in attributes.items():
                print("\t{0}={1}".format(attribute, value))

            stats = weapon_data.get_stats_by_name(weapon)

            for stat in stats:
                print("\t{0}={1}".format(stat.name, stat.value))

    def load_maps(self):
        print("Loading maps...")
        self._maps = OWMaps.OWMapFactory()
        self._maps.initialise()

    def print(self):
        print("Printing Game...")
        print("Characters")
        for character in self.characters:
            print(character)

        print("Maps")
        self._maps.print()