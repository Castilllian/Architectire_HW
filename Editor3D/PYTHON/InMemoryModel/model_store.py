from InMemoryModel.i_model_change_observer import IModelChangeObserver
from InMemoryModel.i_model_changer import IModelChanger
from ModelElements.camera import Camera
from ModelElements.flash import Flash
from ModelElements.poligonal_model import PoligonalModel
from ModelElements.scene import Scene


class ModelStore(IModelChanger):
    def __init__(self, changeObservers: list[IModelChangeObserver]) -> None:
        self._changeObservers = changeObservers
        self.models: list[PoligonalModel] = [PoligonalModel([])]
        self.flashes: list[Flash] = [Flash()]
        self.cameras: list[Camera] = [Camera()]
        self.scenes: list[Scene] = [Scene(self.models, self.flashes, self.cameras)]

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender: IModelChanger) -> None:
        return super().notify_change(sender)
    