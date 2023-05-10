import sys
import pygame
from pygame.sprite import Group
from game.settings import Settings
from game.game_stats import GameStats
from game.scoreboard import Scoreboard
from game.button import Button
from game.ship import Ship
import game.game_functions as gf

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.play_button = Button(self.settings, self.screen, "Play")
        self.stats = GameStats(self.settings)
        self.sb = Scoreboard(self.settings, self.screen, self.stats)
        self.ship = Ship(self.settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()
        gf.create_fleet(self.settings, self.screen, self.ship, self.aliens)
    def run_game(self):
        while True:
            gf.check_events(self.settings, self.screen, self.stats, self.sb, self.play_button, self.ship, self.aliens,
                            self.bullets)

            if self.stats.game_active:
                self.ship.update()
                gf.update_bullets(self.settings, self.screen, self.stats, self.sb, self.ship, self.aliens,
                                  self.bullets)
                gf.update_aliens(self.settings, self.stats, self.screen, self.sb, self.ship, self.aliens,
                                 self.bullets)

            gf.update_screen(self.settings, self.screen, self.stats, self.sb, self.ship, self.aliens, self.bullets,
                             self.play_button)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
