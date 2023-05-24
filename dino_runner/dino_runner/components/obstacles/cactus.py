import random
from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)
