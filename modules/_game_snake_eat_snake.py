import pygame
from pygame.locals import * # some globals being imported like KEYDOWN



def award_penalty_points_against(self, player):
    if player == 'player_1':
        self.yummies_collisions_p2 += self.penalty_points
    elif player == 'player_2':
        self.yummies_collisions += self.penalty_points


def check_if_snake_eat_self(self, player):
    selected_snake = (self.snake if (player == 'player_1') else self.snake_friend)
    
    for i in range(3,selected_snake.length): #3 for third body part, range up to but not including
        if self.is_collision(selected_snake.x[0], selected_snake.y[0], selected_snake.x[i], selected_snake.y[i]):
            self.play_sound(self.snake_crash_sound)

            if self.player == 2:
                self.award_penalty_points_against(player)

            raise "Game over"


def check_if_snake_eat_other_snake(self, player):
    selected_snake = (self.snake if (player == 'player_1') else self.snake_friend)
    eaten_snake = (self.snake_friend if (player == 'player_1') else self.snake)

    for i in range(1,eaten_snake.length): # range up to but not including
        if self.is_collision(selected_snake.x[0], selected_snake.y[0], eaten_snake.x[i], eaten_snake.y[i]):
            self.play_sound(self.snake_crash_sound)
            self.award_penalty_points_against(player)
            raise "Game over"
            

def check_if_snakes_headbutt(self):
    if self.is_collision(self.snake_friend.x[0], self.snake_friend.y[0], self.snake.x[0], self.snake.y[0]):
        self.play_sound(self.snake_crash_sound)
        raise "Game over"



def check_if_snake_eat_snake(self):

    if self.players == 1:
        self.check_if_snake_eat_self('player_1')

    elif self.players == 2:
        self.check_if_snake_eat_self('player_1')
        self.check_if_snake_eat_self('player_2')

        self.check_if_snake_eat_other_snake('player_1')
        self.check_if_snake_eat_other_snake('player_2')


        self.check_if_snakes_headbutt()