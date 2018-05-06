import logging
import utils.trpg as trpg

class OWWeapons():

    def __init__(self):
        pass


class OWWeaponFactory():

    GAME_DATA_DIR = ""

    def __init__(self):
        self.weapons = {}

    def load(self, file_name : str):


        weapon_data = trpg.RPGCSVFactory(name="Weapons", file_name=OWWeaponFactory.GAME_DATA_DIR + file_name)
        weapon_data.load