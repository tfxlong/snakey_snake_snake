
import pygame
from pygame.locals import * # some globals being imported like blit


def display_score(self):       

    font = pygame.font.Font('./fonts/28_days_later.ttf', 30)        

    high_score = font.render(f"High Score  {self.high_score}", True, (232, 84, 136))
    self.surface.blit(high_score, (700,10))

    if self.players == 1:

        player_score = font.render(f"Score  {self.yummies_collisions}", True, (232, 84, 136))
        self.surface.blit(player_score, (20, 10))

    else:

        player_score = font.render(f"P1 Score  {self.yummies_collisions}", True, (232, 84, 136))
        self.surface.blit(player_score, (20, 10))

        player_score = font.render(f"P2 Score  {self.yummies_collisions_p2}", True, (232, 84, 136))
        self.surface.blit(player_score, (20, 60))