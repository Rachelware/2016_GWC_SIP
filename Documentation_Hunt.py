"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [BLACK, GREEN, RED, BLUE]
def random_color():
	return random.coice(colors)
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

x_speed = 3
y_speed = 3

pygame.display.set_caption("Documentation Hunt")

class Circle():
	def __init__(self, mouse_position, Circle_size):
		self.mouse_position = mouse_position
		x_pos = mouse_position[0]
		y_pos = mouse_position[1]
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.Circle_size = Circle_size
	def draw(self):
		global screen
		global RED
		pygame.draw.circle(screen,RED, self.mouse_position,self.Circle_size)
	def move(self, x_pos, y_pos, y_speed, x_speed):
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.x_pos = x_pos								#make a list of positions?
		self.y_pos = y_pos
		
		if self.x_pos >= screen_width - self.Circle_size or self.x_pos < self.Circle_size:
			self.x_speed = x_speed * -1

		if self.y_pos >= screen_height - self.Circle_size or self.y_pos < self.Circle_size:
			self.y_speed = self.y_speed * -1

		self.x_pos += self.x_speed 
		self.y_pos += self.y_speed 

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


circle_list = []

screen.fill(WHITE)

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	pressed = pygame.mouse.get_pressed()
	if pressed[0] == 1:			  #checks if mouse click is happening
		print("Here!")
		screen.fill(WHITE)
		mouse_position = pygame.mouse.get_pos()			#takes position where mouse is pressed
		circle = Circle(mouse_position,20)					#makes circle object
		circle_list.append(circle)
		for circle in circle_list:
			circle.draw()								#draws circles
			circle.move(1,1,1,1)
	
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image
	

	# --- Drawing code should go here


	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60) 

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
