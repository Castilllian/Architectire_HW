from Fabrics.item_fabric import ItemFabric
from Products.lead import Lead


class LeadGenerator(ItemFabric):
    def create_item(self):
        return Lead()