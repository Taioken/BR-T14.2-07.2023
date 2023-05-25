import random
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER

class hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER)
        self.duration = random.randint(3,6)