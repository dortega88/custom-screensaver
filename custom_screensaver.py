import pygame
import os
import random

# Function to get list of image file paths from a folder.
def get_image_files(folder):
	extensions = ['.jpg', '.jpeg', '.png', '.gif']
	return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in extensions]

# Function to resize the image while maintaining aspect ratio.
def resize_image(image, target_width, target_height):
	width, height = image.get_size()
	aspect_ratio = float(width) / float(height)
	new_width, new_height = target_width, target_height

	if width > height:
		new_height = int(target_width / aspect_ratio)
	else:
		new_width = int(target_height * aspect_ratio)
	
	return pygame.transform.scale(image, (new_width, new_height))

# Init pygame
pygame.init()

# Screen dimensions
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Create a screen surface
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

# Set window title
pygame.display.set_caption("Custom Screensaver")

# Set the folder containing images.
image_folder = "/home/pi/shared"

# Load image file paths.
image_files = get_image_files(image_folder)

# Main loop
running = True
while running:
	# Shuffle image file paths.
	random.shuffle(image_files)

	# Loop through the image files.
	for image_file in image_files:
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False
				break

		if not running:
			break

		# Load the image
		image = pygame.image.load(image_file)

		# Resize the image while maintaining aspect ratio
		image = resize_image(image, WIDTH, HEIGHT)

		# Fill the screen with black to 'clear' the previous image.
		screen.fill((0, 0, 0))

		# Center the img on the screen.
		image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

		# Display the image.
		screen.blit(image, image_rect)
		pygame.display.flip()

		# Display the image for a specified duration (in milliseconds)
		pygame.time.delay(5000)

		# Handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False
				break

# Cleanup and exit
pygame.quit()

