import random
import pygame

from dino_runner.components.obstacles.bigcactus import BigCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import SMALL_CACTUS , BIRD, LARGE_CACTUS, GAMEOVER




class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0,2)]))
            
            elif random.randint(0,2) == 1:
                self.obstacles.append(BigCactus(LARGE_CACTUS[random.randint(0,2)]))
                
            elif random.randint(0,2)== 2:
                self.obstacles.append(Bird(BIRD))
                
            
        
        
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                
                pygame.time.delay(500)
                game.playing = False

        
    def draw(self,screen):
        
        for obstacle in self.obstacles:   
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()
            
            
  