from ModelElements.camera import Camera
from ModelElements.flash import Flash
from ModelElements.poligonal_model import PoligonalModel
from typing import List, TypeVar
from abc import ABC


T = TypeVar('T', bound='PoligonalModel')


class Scene(ABC):
    def __init__(
        self, models: List[T], flashes: List[Flash], cameras: List[Camera]
    ) -> None:
        self.id: int = 0
        self.models: List[T] = models
        self.flashes: List[Flash] = flashes

    def method1(self, obj: T) -> T:
        return obj

    def method2(self, obj1: T, obj2: T) -> T:
        return obj1