import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
					(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#create a play button
	play_button = Button(ai_settings, screen, "Play")
	
	#create a register to save the game stats
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#create a ship
	ship = Ship(ai_settings, screen)
	
	#create a alien
	#alien = Alien(ai_settings, screen)
	
	#background color
	bg_color = (230, 230, 230)
	
	#create a group to save the bullet
	bullets = Group()
	
	aliens = Group()
	
	#create a group for aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	while True:
		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets)
		if stats.game_active:
			ship.Update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
				bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		#print(len(bullets))
		gf.Update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
			play_button)

run_game()
