from Products.game_item import GameItem


class Lead(GameItem):
    def open(self):
        print("Lead")