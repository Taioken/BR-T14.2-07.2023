import random
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import CLOUD


class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.y_pos_cloud = random.randint(20,80)
        self.x_pos_cloud = SCREEN_WIDTH
        
    def update(self,game_speed):
        self.x_pos_cloud -= game_speed/2
        if self.x_pos_cloud < 0:
            self.x_pos_cloud = 1500
        
        
            
        
    def draw(self,screen):
        screen.blit(self.image, (self.x_pos_cloud,self.y_pos_cloud))
        
        
        
