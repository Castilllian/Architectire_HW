from random import randint
from Fabrics.bronze_generator import BronzeGenerator
from Fabrics.diamond_generator import DiamondGenerator
from Fabrics.gold_generator import GoldGenerator
from Fabrics.lead_generator import LeadGenerator
from Fabrics.palladium_generator import PalladiumGenerator
from Fabrics.platinum_generator import PlatinumGenerator
from Fabrics.silver_generator import SilverGenerator


if __name__ == '__main__':
    GoldGenerator().create_item().open()

    generators = [GoldGenerator(), BronzeGenerator(), DiamondGenerator(), 
                  LeadGenerator(),PalladiumGenerator(), PlatinumGenerator(), 
                  SilverGenerator()]
    for i in range(10):
        generators[randint(0, 5)].create_item().open()