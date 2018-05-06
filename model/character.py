import logging

class OWCharacter():
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return "Name:{0}".format(self.name)