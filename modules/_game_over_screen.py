import pygame
from pygame.locals import * # some globals being imported like KEYDOWN

def show_game_over(self):

  if self.high_score < self.yummies_collisions:   # will compare player 2 score only if required
      self.high_score = self.yummies_collisions

  y_axis = 100
  
  self.render_background_plain()

  if self.players == 1:

      font1 = pygame.font.Font('./fonts/28_days_later.ttf', 80)

      line1 = font1.render(f"** GAME OVER **", True, (200, 200, 200))
      self.surface.blit(line1, (80, y_axis,))

      font2 = pygame.font.Font('./fonts/28_days_later.ttf', 40)

      line2 = font2.render(f"Your Score    {self.yummies_collisions}", True, (255, 255, 255))
      self.surface.blit(line2, (200, y_axis+150))

      line3 = font2.render(f"High Score    {self.high_score}", True, (255, 255, 255))
      self.surface.blit(line3, (200, y_axis+200))

      line4 = font2.render("To play again press ENTER", True, (255, 255, 255))
      self.surface.blit(line4, (200, y_axis+300))

      line5 = font2.render("To exit press Esc", True, (255, 255, 255))
      self.surface.blit(line5, (200, y_axis+350))

  elif self.players == 2:

      if self.high_score < self.yummies_collisions_p2: # already compared the player 1 score
          self.high_score = self.yummies_collisions_p2
      
      font1 = pygame.font.Font('./fonts/28_days_later.ttf', 80)

      line1 = font1.render(f"** GAME OVER **", True, (200, 200, 200))
      self.surface.blit(line1, (80, y_axis,))

      font2 = pygame.font.Font('./fonts/28_days_later.ttf', 60)

      if self.yummies_collisions > self.yummies_collisions_p2:

          line2 = font2.render(f"Player 1 wins   {self.yummies_collisions} vs {self.yummies_collisions_p2}", True, (255, 255, 255))
          self.surface.blit(line2, (150, y_axis+140))

      elif self.yummies_collisions < self.yummies_collisions_p2:

          line2 = font2.render(f"Player 2 wins  -  {self.yummies_collisions_p2} vs {self.yummies_collisions}", True, (255, 255, 255))
          self.surface.blit(line2, (150, y_axis+140))

      elif self.yummies_collisions == self.yummies_collisions_p2:

          line2 = font2.render(f"It is a draw    {self.yummies_collisions_p2} vs {self.yummies_collisions}", True, (255, 255, 255))
          self.surface.blit(line2, (160, y_axis+140))


      font3 = pygame.font.Font('./fonts/28_days_later.ttf', 40)

      line3 = font3.render(f"High Score    {self.high_score}", True, (255, 255, 255))
      self.surface.blit(line3, (200, y_axis+260))

      line4 = font3.render("To play again press ENTER", True, (255, 255, 255))
      self.surface.blit(line4, (200, y_axis+360))

      line5 = font3.render("To exit press Esc", True, (255, 255, 255))
      self.surface.blit(line5, (200, y_axis+400))

  pygame.display.flip()
  pygame.mixer.music.pause()