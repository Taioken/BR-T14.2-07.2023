import random
from dino_runner.components.obstacles.obstacles import Obstacle

class BigCactus (Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 310  