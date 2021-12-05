############# WILL NEED TO REFACTOR TO INCLUDE THE ord('x') COMMANDS AS BEING ACCESSIBLE


import pygame
from pygame.locals import * # some globals being imported like KEYDOWN


def check_key_directions(self, event, pause_on_interchange, players):


            if not pause_on_interchange:
         
                #event keys have additional protections, to stop snake from accidentally reversing on itself, and when transitioning through border side

                if event.key == K_UP:
                    self.change_snake_direction('player_1', 'down', 'up')
        
                if event.key == K_DOWN:
                    self.change_snake_direction('player_1', 'up', 'down')

                if event.key == K_LEFT:
                    self.change_snake_direction('player_1', 'right', 'left')

                if event.key == K_RIGHT:
                    self.change_snake_direction('player_1', 'left', 'right')

                ########## PLAYER 2 CONTROLS ########################

                if players == 2:

                    if event.key == ord('w'):
                        self.change_snake_direction('player_2', 'down', 'up')
        
                    if event.key == ord('s'):
                        self.change_snake_direction('player_2', 'up', 'down')

                    if event.key == ord('a'):
                        self.change_snake_direction('player_2', 'right', 'left')
        
                    if event.key == ord('d'):
                        self.change_snake_direction('player_2', 'left', 'right')