section_length = 30
import random
import pygame
import time

class Yummies:

    def __init__(self, game_window):
        
        self.yummies_image = pygame.image.load("images/frog_faceS.png").convert()
        self.game_window = game_window

        self.x = random.randint(1,29)*section_length # x co-ordinate will be anywhere from 30 - 870
        self.y = random.randint(1,19)*section_length # y co-ordinate will be anywhere from 30 - 570


        # print(Yummies.yummies_count)

    def move(self):
        self.x = random.randint(0,29)*section_length
        self.y = random.randint(0,19)*section_length


    def draw(self):   

        # if Yummies.yummies_count % 10 != 0:
        self.game_window.blit(self.yummies_image, (self.x, self.y))
        pygame.display.flip()



