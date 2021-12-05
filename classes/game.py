import pygame
from pygame.locals import * # some globals being imported like KEYDOWN
import time
import random

from classes.yummies import *
from classes.yuckies import *
from classes.snake import *


class Game:
     
    def __init__(self):        

        pygame.init()
        pygame.display.set_caption("Snakey Snake Snake")

        pygame.mixer.init()
        self.play_background_music()

        self.players = 1

        self.surface = pygame.display.set_mode((900,600))  # initialises the window and parameters for it 
        self.render_background_plain()

        self.yuckies1 = Yuckies(self.surface)
        self.yuckies2 = Yuckies(self.surface)
        self.yuckies3 = Yuckies(self.surface)


        #################### IN GAME VARIABLES ###########################

        # self.players = 1
        self.difficulty_level = "Beginner" # (through walls, slow speed)
        self.game_speed = 0.5

        self.yummies_collisions = 0
        self.yummies_collisions_p2 = 0

        self.high_score = 0

        self.penalty_points = 10

        self.wall_crash_sound = "./sounds/audio1.wav"
        self.snake_crash_sound = "./sounds/audio1.wav"
        self.yummies_sound = "./sounds/audio1.wav"
        self.yuckies_sound = "./sounds/audio1.wav"


    def play_sound(self, sound):
        my_sound = pygame.mixer.Sound(sound)
        pygame.mixer.Sound.play(my_sound)


######### MAKE A YUMMY ###############

    def make_yummies(self):

        self.yummies = Yummies(self.surface) # arguments => they type of game_window
        self.yummies.draw()


########## MAKE A YUCKY ###################

# can leave this and implement as required for random effects (future feature)


######################## MAKE A SNAKE ##################

    def make_snake(self):

        if self.players == 1:
            self.snake = Snake(self.surface, 3, self.players, "only") # arguments => the type of game_window // number of snake sections
            self.snake.draw()

        elif self.players == 2:
            self.snake = Snake(self.surface, 3, self.players, "first") # arguments => the type of game_window // number of snake sections
            self.snake.draw()

            self.snake_friend = Snake(self.surface, 3, self.players, "second") # arguments => the type of game_window // number of snake sections
            self.snake_friend.draw()


####################### COLLISION PARAMETERS ########################################

    def is_collision(self, snake_x, snake_y, object_x, object_y):
        if (snake_x >= object_x) and (snake_x < object_x + section_length):
            if (snake_y >= object_y) and (snake_y < object_y + section_length):
                return True
        
        return False


################ GAME START, GAME OVER, DISPLAY SCORE SCREENS ##########################
  
    from _game_display_score import display_score
    from _game_start_menu import game_menu
    from _game_over_screen import show_game_over

#################################### GAME RESET ############################
    
    def reset(self):

        print(self.difficulty_level)

        self.yummies_collisions = 0

        if self.players == 2:
            self.yummies_collisions_p2 = 0

        if self.difficulty_level == "Beginner":
            self.game_speed = 0.3
        else: 
            self.game_speed = 0.1

        self.make_snake()  # need to re-create snake, otherwise it doesn't reset its position


#################################### BACKGROUND RENDER AND MUSIC/SOUND EFFECTS ############################

    def play_background_music(self):
        pygame.mixer.music.load("./sounds/rain.wav")
        pygame.mixer.music.play(-1)


    def render_background(self):
        background_image = pygame.image.load("./images/puddle.jpeg")
        self.surface.blit(background_image, (0,0, 500, 200))
        if self.difficulty_level=="Expert":
            colour = (255,0,0)
            pygame.draw.rect(self.surface, colour, pygame.Rect(0, 0, 900, 600), 2)

    def render_background_plain(self):
        self.surface.fill((15,74,74))


#################################### YUMMY COLLISION SOUND EFFECTS AND MOVE PARAMETERS ############################
   
    def ensure_yummy_not_on_yucky(self):

        possible_conflict = True
        while possible_conflict: # yummy and yucky on same spot
            self.yummies.move()
            if not ((self.yummies.x == self.yuckies1.x) and (self.yummies.y == self.yuckies1.y)):
                if not ((self.yummies.x == self.yuckies2.x) and (self.yummies.y == self.yuckies2.y)):
                    if not ((self.yummies.x == self.yuckies3.x) and (self.yummies.y == self.yuckies3.y)):
                        possible_conflict = False
                        # this avoids the possibility of a frog appearing at the same site as a toad


    def update_high_score(self):
        if self.yummies_collisions >= self.high_score:
            self.high_score = self.yummies_collisions
        if self.yummies_collisions_p2 >= self.high_score:
                self.high_score = self.yummies_collisions_p2
    

    def yummy_collision_adjunct(self, player):
        self.play_sound(self.yummies_sound)

        self.snake.increase_length() if (player == 'player_1') else self.snake_friend.increase_length()

        self.game_speed = self.game_speed * 0.9

        self.yuckies1.move()
        self.yuckies2.move()
        self.yuckies3.move()
        self.ensure_yummy_not_on_yucky()

        self.update_high_score()


#################################### YUCKY COLLISION SOUND EFFECTS, POINTS AND GAME OVER ############################

    def yucky_collision_adjunct(self, player_who_collided):
        self.play_sound(self.yuckies_sound)

        if self.players == 2:
            if player_who_collided == 'player_1':
                    self.yummies_collisions_p2 += self.penalty_points # penalty_points is a class variable with a value eg 10
            if player_who_collided == 'player_2':
                self.yummies_collisions += self.penalty_points

        raise "Game over"
    
#################################### REFRESH SCREEN - NEW FRAME POSTIONS - CHECK COLLISIONS ##################

    def refresh_screen(self):
        self.render_background()

        self.snake.update_frame() # this updates the co-ordinates AND includes the draw function
        if self.players == 2:
            self.snake_friend.update_frame() # this updates the co-ordinates AND includes the draw function

        self.yuckies1.draw()
        self.yuckies2.draw()
        self.yuckies3.draw()

        self.yummies.draw()
        
        self.display_score()

        pygame.display.flip()  

        self.check_snake_hitting_wall()
        self.check_if_snake_eat_snake()
        self.check_if_yummy_collision()

        #### YUCKIES COLLISION ####################################
        from _game_collision_yuckies import check_yuckies_collision
        check_yuckies_collision(self)


#################################### YUMMY COLLISION ####################################

    def check_if_yummy_collision(self):
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.yummies.x, self.yummies.y):
            self.yummy_collision_adjunct('player_1')
            self.yummies_collisions += 1

        elif self.players == 2:  # will only run if meets two conditions (1. first snake = no collision, 2. if there are two players)

            if self.is_collision(self.snake_friend.x[0], self.snake_friend.y[0], self.yummies.x, self.yummies.y):
                self.yummy_collision_adjunct('player_2')                    
                self.yummies_collisions_p2 += 1

#################################### WALL COLLISION ####################################

    from _game_collision_wall import is_hit_wall_die
    from _game_collision_wall import is_hit_wall_survive
    from _game_collision_wall import is_hit_wall_survive_friend

    def check_snake_hitting_wall(self):

        if self.difficulty_level == "Beginner":
            self.is_hit_wall_survive(self.snake.x[0], self.snake.y[0])

            if self.players == 2:
                self.is_hit_wall_survive_friend(self.snake_friend.x[0], self.snake_friend.y[0])

        else: # if 'Expert'
            self.is_hit_wall_die(self.snake.x[0], self.snake.y[0], 1)
            
            if self.players == 2:
                self.is_hit_wall_die(self.snake_friend.x[0], self.snake_friend.y[0], 2)

            
#################################### SNAKE EAT SELF ####################################
        
    from _game_snake_eat_snake import check_if_snake_eat_self
    from _game_snake_eat_snake import award_penalty_points_against
    from _game_snake_eat_snake import check_if_snake_eat_other_snake
    from _game_snake_eat_snake import check_if_snakes_headbutt

    def check_if_snake_eat_snake(self):

        if self.players == 1:
            self.check_if_snake_eat_self('player_1')

        elif self.players == 2:
            self.check_if_snake_eat_self('player_1')
            self.check_if_snake_eat_self('player_2')

            self.check_if_snake_eat_other_snake('player_1')
            self.check_if_snake_eat_other_snake('player_2')


            self.check_if_snakes_headbutt()


#################### ALLOWABLE SNAKE DIRECTION ########################

    def change_snake_direction(self, player, current_orientation, new_orientation):

        if player == 'player_1':
            selected_snake = self.snake
        else:
            selected_snake = self.snake_friend

        if selected_snake.orientation== current_orientation or ((selected_snake.x[0] == -30 or selected_snake.x[0] == 900) or (selected_snake.y[0] == -30 or selected_snake.y == 600)):
            True
        else:
            selected_snake.orientation= new_orientation

           
#################### GAME PLAY RUN LOOP ########################
    
    from _game_check_pygame_events import check_key_directions
    def run(self):

        intro_menu = True
        while intro_menu:             # This loop allows for game menu parameters to be set before playing
            self.game_menu()    
            intro_menu = False

        game_running = True
        pause_on_interchange = False

        self.make_snake()
        self.make_yummies()

        

        while game_running:

            for event in pygame.event.get(): 

                        # a pygame method that accepts a variety of user inputs
                
                if event.type == QUIT:
                    game_running = False              # will exit game
                
                elif event.type == KEYDOWN:             # KEYDOWN is from a global variable in the pygame.locals (key press)

                    if event.key == K_ESCAPE:         # Escape key works to exit now as well
                        game_running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause_on_interchange = False

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
                        if self.players == 2:

                            if event.key == ord('w'):
                                self.change_snake_direction('player_2', 'down', 'up')                
                            if event.key == ord('s'):
                                self.change_snake_direction('player_2', 'up', 'down')            
                            if event.key == ord('a'):
                                self.change_snake_direction('player_2', 'right', 'left')                
                            if event.key == ord('d'):
                                self.change_snake_direction('player_2', 'left', 'right')

                        
            
            #time.sleep(0.3)  #to slow it down
            time.sleep(self.game_speed)  #to slow it down
           

            try:
                if not pause_on_interchange:

                    self.refresh_screen()

            except Exception as e: # having the exception makes it very helpful for debugging
                print(e)
                
                self.show_game_over() # this is a message for game over with score
                pause_on_interchange = True
                self.reset()
                

####################################