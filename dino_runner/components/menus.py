import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH,FONT_STYLE


class MENUS:
    
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