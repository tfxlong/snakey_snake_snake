import pygame
section_length = 30


class Snake:
    def __init__(self, game_window, snake_length, number_players, snake_identity):

        print("In Snake here is the Number players = " + str(number_players))

        self.length = snake_length

        self.game_window = game_window

        self.snake_identity = snake_identity
    
        self.body_h = pygame.image.load("images/snake_body_h.png").convert()
        self.body_v = pygame.image.load("images/snake_body_v.png").convert()

        self.head_up = pygame.image.load("images/snake_head_up.jpg").convert() 
        self.head_down = pygame.image.load("images/snake_head_down.jpg").convert() 
        self.head_left = pygame.image.load("images/snake_head_left.jpg").convert() 
        self.head_right = pygame.image.load("images/snake_head_right.jpg").convert() 

        # MOVE THESE TO INSTANTIATION ARGUMENTS SO THAT SNAKE 2 CAN HAVE OTHERS
        # MAYBE USE AN f STRING TO SET FOLDER LOCATION SNAKE_1, SNAKE_2
        
        if int(number_players) == 1: 
            self.x = [section_length] * self.length  # x = 90      x = [30, 30, 30]
            self.y = [section_length] * self.length  # y = 90      y = [30, 30, 30]
        
        elif int(number_players) == 2:

            if self.snake_identity == "first":
                self.x = [(section_length * 6)] * (self.length)  # x = 180      x = [30, 30, 30]
                self.y = [(section_length * 4)] * (self.length)  # y = 90      y = [30, 30, 30]

            else:
                self.x = [(section_length * 20)] * (self.length)  # x = 720     x = [30, 30, 30]
                self.y = [(section_length * 4)] * (self.length)  # y = 90      y = [30, 30, 30]

        self.orientation= 'down'        # to enable the automatic movement

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
 


    def draw(self):

        ####### HEAD SECTION ##############

        if self.orientation == "up":
            snake_head_image = self.head_up
        elif self.orientation == "down":
                snake_head_image = self.head_down
        elif self.orientation == "right":
                snake_head_image = self.head_right
        else: 
            snake_head_image = self.head_left

        #tail => if self.snake[0]
        self.game_window.blit(snake_head_image, (self.x[0], self.y[0]) )

        ####### BODY SECTION ##############
      
        for i in range(1, self.length):  #range 1 to (up-to-but-not-including) length of snake ([-1] is negligible value)

            if self.x[i] == self.x[i-1]:
                self.game_window.blit(self.body_v, (self.x[i], self.y[i]))

            else:
                self.game_window.blit(self.body_h, (self.x[i], self.y[i]))

        pygame.display.flip()



    def update_frame(self):

        for i in range( (self.length - 1), 0, -1):     #length of snake (minus 1),  iterate backwards up to but not including [0]/head

            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.orientation == 'up':
            self.y[0] -= section_length                  #head of snake is at index [0] of array

        elif self.orientation == 'down':
            self.y[0] += section_length

        elif self.orientation == 'right':
            self.x[0] += section_length

        elif self.orientation == 'left':
            self.x[0] -= section_length
            
        else:
            print("Something is wrong with snake frame update")
        
        self.draw()


    def check_collision(self):
        return # consider moving the collisions to apply to the snake itself, not be applicable to the game per se