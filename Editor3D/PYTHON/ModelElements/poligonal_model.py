from .poligon import Poligon
from .texture import Texture
from Stuff.point_3d import Point3D

class PoligonalModel:
    def __init__(self, texture):
        self.Poligons = []
        self.Texture = texture
        self.poligons.append(Poligon(Point3D()))
