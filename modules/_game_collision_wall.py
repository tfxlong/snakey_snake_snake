import pygame
from pygame.locals import * # some globals being imported like KEYDOWN

def is_hit_wall_die(self, snake_x, snake_y, which_snake):
  if ((snake_x == -30 or snake_x == 900) or (snake_y == -30 or snake_y == 600)):
      # if (y1 >= y2) and (y1 < y2 + section_length):
      my_sound = pygame.mixer.Sound(self.wall_crash_sound)
      pygame.mixer.Sound.play(my_sound)

      if self.players == 2:   # this awards the other player points as this snake crashed
          if which_snake == 1: 
              if (self.snake_friend.y[0] == 600) and (self.snake_friend.orientation == "down"):
                  print("both crashed into walls at same time")
                  
              elif (self.snake_friend.y[0] == -30) and (self.snake_friend.orientation == "up"):
                  print("both crashed into walls at same time")
                  
              elif (self.snake_friend.x[0] == -30) and (self.snake_friend.orientation == "left"):
                  print("both crashed into walls at same time")
                  
              elif (self.snake_friend.y[0] == 900) and (self.snake_friend.orientation == "right"):
                  print("both crashed into walls at same time")
                  
              else: 
                  self.yummies_collisions_p2 += self.penalty_points 
  
      # Due to flow control, these conditions only need to be applied to player 1 (as it will run player 1 first)

          elif which_snake == 2:
              self.yummies_collisions += self.penalty_points
              print("P2 crashed")            

      raise "Hit Wall - Game Over"
  
  else:
      return False


def is_hit_wall_survive(self, snake_x, snake_y):
  if (snake_x == -30 and self.snake.orientation == "left"):
      self.snake.x[0] = 900 

  elif (snake_x == 900 and self.snake.orientation == "right"):
      self.snake.x[0] = -30
  
  elif (snake_y == -30 and self.snake.orientation == "up"):
      self.snake.y[0] = 600 
  
  elif (snake_y == 600 and self.snake.orientation == "down"):
      self.snake.y[0] = -30



def is_hit_wall_survive_friend(self, snake_x, snake_y):

  if (snake_x == -30 and self.snake_friend.orientation == "left"):
      self.snake_friend.x[0] = 900 

  elif (snake_x == 900 and self.snake_friend.orientation == "right"):
      self.snake_friend.x[0] = -30
  
  elif (snake_y == -30 and self.snake_friend.orientation == "up"):
      self.snake_friend.y[0] = 600 
  
  elif (snake_y == 600 and self.snake_friend.orientation == "down"):
      self.snake_friend.y[0] = -30