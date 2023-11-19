from abc import ABC


class Scene(ABC):
    def __init__(self, id, models, flashes, cameras):
        self.ID = id
        if len(models) > 0:
            self.Models = models
        else:
            raise Exception("Only one model must be")
        self.Flashes = flashes
        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Only one camera must be")
        