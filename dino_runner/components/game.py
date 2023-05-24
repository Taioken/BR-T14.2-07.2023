import pygame
import random

from dino_runner.components.cloud.imagecloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        
        self.playing = False
        self.executing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.record_score = 0
        self.trocar = 0
        
        self.score = 0
        self.death_count = -1
        self.life_counter = 3
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                if self.trocar == 0:
                    #self.menu_game_over()
                    self.display_menu()
                    
                else:
                    
                    self.menu_game_over()


 
            
                
        
        pygame.quit()    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)
        
    def update_score(self):
        if self.score > 1000:
            self.score += 5
        else:
            self.score += 1
        
    
    def update_death(self):
        self.death_count +=1
        
    def update_speed(self):
        if self.score % 1000 == 0:
            self.game_speed += 10
        elif self.score % 3000 == 0:
            self.game_speed += 5
    
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_death_count()
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.speed_draw()
        
        pygame.display.flip()

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        
        self.screen.blit(text, text_rect)
        
        self.menu_events_handler()
        pygame.display.flip()
    
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def menu_game_over(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        
        user_input = pygame.key.get_pressed
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("GAME OVER", True, (0,0,0))

        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        textcontinue = font.render("Aperte C para continua", True, (0,0,0))
        textrestart = font.render("Aperte R para Reiniciar", True, (0,0,0))
        textrecord = font.render(f"High Score: {self.record_score}",True,(0,0,0))
        self.screen.blit(text, text_rect)
        self.screen.blit(textrestart,(480,400))
        self.screen.blit(textcontinue,(480,340))
        self.screen.blit(textrecord,(800,50))
        if self.record_score < self.score:
            self.record_score = self.score
        
        self.game_over_event_handler()

        pygame.display.flip()
        self.screen.blit(textrestart,(0,800))
        
    def game_over_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.run()
                
                elif event.key == pygame.K_r:
                    self.death_count = -1
                    self.display_menu()
                    self.trocar = 0
    
    def speed_draw(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_speed = font.render(f"Speed: {self.game_speed}KM/h", True, (0,0,0))
        text_rect_speed = text_speed.get_rect()
        text_rect_speed.center = (0,50)
        
        self.screen.blit(text_speed,text_rect_speed)  
        
                        
                
    def draw_death_count(self):
         font = pygame.font.Font(FONT_STYLE,22)
         text_death = font.render(f"Death Count: {self.death_count}", True, (0,0,0))
         text_rect_death = text_death.get_rect()
         text_rect_death.center = (500,50)
         
         self.screen.blit(text_death,text_rect_death)        
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text_score = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect_score = text_score.get_rect()
        text_rect_score.center = (1000,50)
        
        self.screen.blit(text_score, text_rect_score)
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        if self.death_count <= 0:
            self.update_death()
        elif self.death_count > 0:
            self.update_death()
        if self.trocar <= 0:
            self.trocar +=1
        elif self.trocar > 0:
            pass
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
        