import pygame
from pygame.locals import * # some globals being imported like KEYDOWN



def game_menu(self):

  ##################### SECTION 1 / 3 ##########################

  pos_y = 70

  self.render_background_plain()
  font1 = pygame.font.Font('./fonts/28_days_later.ttf', 60)

  welcome = font1.render("WELCOME TO SNAKEY SNAKE SNAKE", True, (200, 200, 200))
  self.surface.blit(welcome, (12, pos_y))

  pygame.display.flip()

  font2 = pygame.font.Font('./fonts/28_days_later.ttf', 30)

  choose_players_line1 = font2.render("HERE ARE THE RULES", True, (200, 200, 200))
  self.surface.blit(choose_players_line1, (100, pos_y + 100))


  choose_players_line2 = font2.render("* Move snake to eat frogs", True, (200, 200, 200))
  self.surface.blit(choose_players_line2, (100, pos_y + 150))

  choose_players_line3 = font2.render("* Do not eat the cane toads or snake will die", True, (200, 200, 200))
  self.surface.blit(choose_players_line3, (100, pos_y + 200))

  choose_players_line4 = font2.render("* Beginners Can go through walls but not Experts", True, (200, 200, 200))
  self.surface.blit(choose_players_line4, (100, pos_y + 250))

  choose_players_line5 = font2.render("* USE UP DOWN LEFT RIGHT   &   w s a d   FOR PLAYER 2", True, (200, 200, 200))
  self.surface.blit(choose_players_line5, (100, pos_y + 300))

  choose_players_line6 = font2.render("* 10 Points ARE given to other player if you crash", True, (200, 200, 200))
  self.surface.blit(choose_players_line6, (100, pos_y + 350))

  choose_players_line7 = font2.render("* Game will speed up as more frogs are eaten", True, (200, 200, 200))
  self.surface.blit(choose_players_line7, (100, pos_y + 400))


  font3 = pygame.font.Font('./fonts/28_days_later.ttf', 25)
  exit_line = font3.render("PRESS Enter to continue  OR  esc to exit", True, (200, 200, 200))
  self.surface.blit(exit_line, (100, pos_y + 480))

  pygame.display.flip()

  adequate_answer = False
  while not adequate_answer:

      for event in pygame.event.get(): 
                          # a pygame method that accepts a variety of user inputs
                                                
          if event.type == QUIT:
              quit()            # will exit game
          
          elif event.type == KEYDOWN:             # KEYDOWN is from a global variable in the pygame.locals (key press)

              if event.key == K_ESCAPE:         # Escape key works to exit now as well
                  quit()

              if event.key == K_RETURN: 
                  adequate_answer = True



#################### SECTION 2 / 3 ################################

  pos_y = 100

  self.render_background_plain()
  font1 = pygame.font.Font('./fonts/28_days_later.ttf', 60)

  welcome = font1.render("WELCOME TO SNAKEY SNAKE SNAKE", True, (200, 200, 200))
  self.surface.blit(welcome, (12, pos_y))

  pygame.display.flip()

  font2 = pygame.font.Font('./fonts/28_days_later.ttf', 40)

  choose_players_line1 = font2.render("HOW MANY PLAYERS ", True, (200, 200, 200))
  self.surface.blit(choose_players_line1, (200, pos_y + 200))

  choose_players_line2 = font2.render("Press 1 or 2", True, (200, 200, 200))
  self.surface.blit(choose_players_line2, (200, pos_y + 250))

  font3 = pygame.font.Font('./fonts/28_days_later.ttf', 20)
  exit_line = font3.render("To exit press esc", True, (200, 200, 200))
  self.surface.blit(exit_line, (200, pos_y + 450))

  pygame.display.flip()

  adequate_answer = False
  while not adequate_answer:

      for event in pygame.event.get(): 
                          # a pygame method that accepts a variety of user inputs
                                                
          if event.type == QUIT:
              quit()            # will exit game
          
          elif event.type == KEYDOWN:             # KEYDOWN is from a global variable in the pygame.locals (key press)

              if event.key == K_ESCAPE:         # Escape key works to exit now as well
                  quit()

              if event.key == K_1:   
                  self.players = 1
                  adequate_answer = True


              if event.key == K_2:   
                  self.players = 2
                  adequate_answer = True
                

#################### SECTION 3 / 3 ################################

  self.render_background_plain()
  # self.surface.fill(background_colour)

  pos_y = 100

  font1 = pygame.font.Font('./fonts/28_days_later.ttf', 60)

  welcome = font1.render("WELCOME TO SNAKEY SNAKE SNAKE", True, (200, 200, 200))
  self.surface.blit(welcome, (12, pos_y))

  font2 = pygame.font.Font('./fonts/28_days_later.ttf', 40)

  choose_players_line1 = font2.render("WHAT DIFFICULTY LEVEL", True, (200, 200, 200))
  self.surface.blit(choose_players_line1, (200, pos_y + 200))

  font3 = pygame.font.Font('./fonts/28_days_later.ttf', 35)

  choose_players_line2 = font3.render("Press 1 for Beginner", True, (200, 200, 200))
  self.surface.blit(choose_players_line2, (200, pos_y + 275))

  choose_players_line3 = font3.render("Press 2 for Expert", True, (200, 200, 200))
  self.surface.blit(choose_players_line3, (200, pos_y + 325))

  font3 = pygame.font.Font('./fonts/28_days_later.ttf', 20)
  exit_line = font3.render("To exit press esc", True, (200, 200, 200))
  self.surface.blit(exit_line, (200, pos_y + 450))

  pygame.display.flip()

  adequate_answer = False
  while not adequate_answer:

      for event in pygame.event.get(): 
                          # a pygame method that accepts a variety of user inputs
                  
          if event.type == QUIT:
              quit()              # will exit game
          
          elif event.type == KEYDOWN:             # KEYDOWN is from a global variable in the pygame.locals (key press)

              if event.key == K_ESCAPE:         # Escape key works to exit now as well
                  quit()

              if event.key == K_1:                      
                  self.difficulty_level = "Beginner" # (through walls, slow speed)
                  self.game_speed = 0.3
                  adequate_answer = True                        

              if event.key == K_2:                            
                  self.difficulty_level = "Expert" # (through walls, slow speed)
                  self.game_speed = 0.1
                  adequate_answer = True