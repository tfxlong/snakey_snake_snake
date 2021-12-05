import pygame
from pygame.locals import * # some globals being imported like KEYDOWN


#################################### YUCKY COLLISION CHECK ############################

def check_yuckies_collision(self):

  if self.is_collision(self.snake.x[0], self.snake.y[0], self.yuckies1.x, self.yuckies1.y):
      self.yucky_collision_adjunct('player_1')

  elif self.is_collision(self.snake.x[0], self.snake.y[0], self.yuckies2.x, self.yuckies2.y):
      self.yucky_collision_adjunct('player_1')

  elif self.is_collision(self.snake.x[0], self.snake.y[0], self.yuckies3.x, self.yuckies3.y):
      self.yucky_collision_adjunct('player_1')


  if self.players == 2: # check the other conditional yucky_collision only if there are two players

      if self.is_collision(self.snake_friend.x[0], self.snake_friend.y[0], self.yuckies1.x, self.yuckies1.y):
          self.yucky_collision_adjunct('player_2')

      elif self.is_collision(self.snake_friend.x[0], self.snake_friend.y[0], self.yuckies2.x, self.yuckies2.y):
          self.yucky_collision_adjunct('player_2')

      elif self.is_collision(self.snake_friend.x[0], self.snake_friend.y[0], self.yuckies3.x, self.yuckies3.y):
          self.yucky_collision_adjunct('player_2')

