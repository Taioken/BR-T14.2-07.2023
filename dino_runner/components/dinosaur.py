import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, SCREEN_WIDTH, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, DUCKING_SHIELD,JUMPING_SHIELD
from dino_runner.utils.constants import HAMMER_TYPE,RUNNING_HAMMER,JUMPING_HAMMER,DUCKING_HAMMER,PULO

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}

Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8
Move_Speed = 10
X_Pos = 10



class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[DEFAULT_TYPE][0]
        self.dino_rect = self.image.get_rect()
        self.has_power_up = False
        self.power_up_time_up = 0
        self.som_pulo = PULO
        self.som_pulo.set_volume(1)
        self.dino_rect.x = X_Pos
        self.dino_rect.y = Y_POS
        
        self.step_count = 0
        
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_front = False
        self.jump_vel = JUMP_VEL
        self.dino_back = False
    
    def update(self, user_input):
        

        
        if user_input[pygame.K_UP]:
            if self.dino_rect.y != Y_POS:
                pass
            else:
                self.dino_run = False
                self.dino_jump = True
                PULO.play()
                
        elif not self.dino_jump:
            self.dino_run = True
        
            
            
        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        if user_input[pygame.K_RIGHT]:
            self.dino_front = True
        if user_input[pygame.K_LEFT]:
            self.dino_back = True
        
        
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if self.step_count > 9:
            self.step_count = 0
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_count//5]
        self.dino_rect.y = Y_POS
        if self.dino_front:
            if self.dino_rect.x <= 1000:
                self.dino_rect.x += Move_Speed
                self.dino_front = False
        elif self.dino_back:
                if self.dino_rect.x >= 0:
                    self.dino_rect.x -= Move_Speed
                    self.dino_back = False    
            
            
        
        self.step_count+=1
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_count//5]
        self.dino_rect.y = Y_POS_DUCK
        if self.dino_front:
            if self.dino_rect.x <= 1005:
                self.dino_rect.x += Move_Speed
                self.dino_front = False
        elif self.dino_back:
            if self.dino_rect.x >= 0:
                self.dino_rect.x -= Move_Speed
                self.dino_back = False    
        
        self.step_count+=1
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            if self.dino_front:
                if self.dino_rect.x <= 1005:
                    self.dino_rect.x += Move_Speed
                    self.dino_front = False
            elif self.dino_back:
                if self.dino_rect.x >= 0:
                        self.dino_rect.x -= Move_Speed
                        self.dino_back = False
            self.jump_vel -= 0.8
        
            
        if self.jump_vel <- JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
    
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
        