from Fabrics.item_fabric import ItemFabric
from Products.palladium import Palladium


class PalladiumGenerator(ItemFabric):
    def create_item(self):
        return Palladium()