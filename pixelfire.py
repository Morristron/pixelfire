import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Fire effect resolution (lower resolution for better performance)
fire_width, fire_height = 100, 75
pixel_size = screen_width // fire_width

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Fire Effect")

# Create a surface for the fire effect
fire_surface = pygame.Surface((fire_width, fire_height))

# Define the fire array
fire_array = [[0 for _ in range(fire_width)] for _ in range(fire_height)]

# List to track currently burning pixels
active_pixels = []

# Define a color palette for the fire effect
palette = [
    (0, 0, 0),
    (32, 8, 0),
    (64, 16, 0),
    (128, 32, 0),
    (192, 48, 0),
    (255, 64, 0),
    (255, 128, 0),
    (255, 192, 0),
    (255, 255, 0),
    (255, 255, 255)
]

# Update fire array
def update_fire():
    new_active_pixels = []
    for x, y in active_pixels:
        if y > 0:
            decay = random.randint(0, 2)
            new_value = fire_array[y][x] - decay
            if new_value < 0:
                new_value = 0
            fire_array[y - 1][x] = new_value
            if new_value > 0:
                new_active_pixels.append((x, y - 1))
        # Reset current pixel after processing
        fire_array[y][x] = 0

    # Generate new fire at the bottom
    for x in range(fire_width):
        new_value = random.randint(0, len(palette) - 1)
        fire_array[fire_height - 1][x] = new_value
        if new_value > 0:
            new_active_pixels.append((x, fire_height - 1))
    
    return new_active_pixels

# Render fire array to surface
def render_fire():
    for x in range(fire_width):
        for y in range(fire_height):
            color_index = fire_array[y][x]
            color = palette[color_index]
            pygame.draw.rect(fire_surface, color, (x, y, 1, 1))

# Main game loop
running = True
clock = pygame.time.Clock()

# Initialize active pixels with the bottom row
for x in range(fire_width):
    active_pixels.append((x, fire_height - 1))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    active_pixels = update_fire()
    render_fire()

    # Scale up the fire surface to fit the screen
    scaled_fire_surface = pygame.transform.scale(fire_surface, (screen_width, screen_height))
    screen.blit(scaled_fire_surface, (0, 0))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
