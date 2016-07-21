import pygame
import random

pygame.init()

from city_scroll import Scroller

WHITE = (255, 255, 255)
RED = (255, 0, 0)


screen_width=(800)
screen_height=(600)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Runner Game")



done = False

clock = pygame.time.Clock()

#classes

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bird.png")
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(60,60))
		
	def draw(self,pos):
		global screen
		screen.blit(self.image,pos)
		self.rect.move(pos)
	def update(self):
		g

#player sprite stuff
bird = RunnerSprite()
all_sprites_list = pygame.sprite.Group()
good_sprites = pygame.sprite.Group()
all_sprites_list.add(bird)
bird.draw((screen_width-100,100))




#scroller stuff

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)


back_scroller = Scroller(screen, screen_width, 100, screen_height-100, BACK_SCROLLER_COLOR, 1)
middle_scroller = Scroller(screen, screen_width, 300, screen_height-70, MIDDLE_SCROLLER_COLOR, 2)
front_scroller = Scroller(screen, screen_width, 500, screen_height-20, FRONT_SCROLLER_COLOR, 3)

back_scroller.add_buildings()
middle_scroller.add_buildings()
front_scroller.add_buildings()
a=0

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	if a%30==0:
		back_scroller.add_building(-100)
	if a%20==0:
		middle_scroller.add_building(-100)
	if a%10==0:
		front_scroller.add_building(-100)
	a+=1
	
	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(WHITE)

	# --- Drawing code should go here
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	eagle.draw((pygame.mouse.get_pos()[0]-30,pygame.mouse.get_pos()[1]-30))
	
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE