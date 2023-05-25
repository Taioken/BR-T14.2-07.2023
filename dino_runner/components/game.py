import pygame
import random

from dino_runner.components.cloud.imagecloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE,DEFAULT_TYPE,SCORE,HAMMER_TYPE
from dino_runner.utils.constants import Musica_Menu,Musica_gameplay,DEATH
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.music_score = SCORE
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()
        self.music_menu = Musica_Menu
        self.music_menu = Musica_gameplay
        self.image = DEATH
        self.playing = False
        self.executing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.record_score = 0
        self.trocar = 0
        
        self.score = 0
        self.death_count = -1
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                if self.trocar == 0:

                    pygame.mixer.music.play(-1)
                    self.display_menu()
                    
                else:
                    pygame.mixer.music.stop()
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
        self.power_up_manager.update(self)
        
    def update_score(self):
        
            self.score += 1
    
    def update_death(self):
        self.death_count +=1
        
    def update_speed(self):
        if self.score % 1000 == 0:
            self.music_score.play()
            self.game_speed += 10
        elif self.game_speed == 50:
            self.game_speed = 50
    
        
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
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()    
        
        pygame.display.flip()

    
    
    def display_text(self, text, x, y, font_size=22, color=(0,0,0)):
        font = pygame.font.Font(FONT_STYLE, font_size)
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(rendered_text, text_rect)
    
    
    def display_menu(self):
        pygame.mixer.music.play(-1)
        self.menu_events_handler()
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        self.display_text("Press any key to start", x_text_pos, y_text_pos)
        self.music_menu
      
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
        self.display_text("GAME OVER", x_text_pos, y_text_pos)
        self.display_text("Aperte C para continuar", x_text_pos, y_text_pos+80)
        self.display_text("Aperte R para Reiniciar", x_text_pos, y_text_pos+40)
        self.display_text(f"High Score: {self.record_score}", 800, 50)
        if self.record_score < self.score:
            self.record_score = self.score
        
        self.game_over_event_handler()

        pygame.display.flip()
        
    def game_over_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.mixer.music.play(-1)
                    self.menu_events_handler()
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
        
    def draw_power_up_time(self):
        contador = 3
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up Time:{time_to_show}s", True, (255,0,0))
                
                text_rect_powerup = text.get_rect()
                text_rect_powerup.center =(500,80)

                
                self.screen.blit(text, text_rect_powerup)
            
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE               
                
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
        