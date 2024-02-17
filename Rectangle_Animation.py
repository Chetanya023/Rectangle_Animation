import pygame
import sys

pygame.init()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectangle Animation")

rect_width, rect_height = 100, 50
rect_color = (0, 255, 0)
rect_x, rect_y = width // 2 - rect_width // 2, height // 2 - rect_height // 2

vertical_rect_width, vertical_rect_height = 50, 100
vertical_rect_color = (255, 0, 0)
vertical_rect_x, vertical_rect_y = width // 4 - vertical_rect_width // 2, height // 2 - vertical_rect_height // 2

horizontal_rect_width, horizontal_rect_height = 80, 40
horizontal_rect_color = (0, 0, 255)
horizontal_rect_x, horizontal_rect_y = width // 1.5 - horizontal_rect_width // 2, height // 2 - horizontal_rect_height // 2

fps = 30
clock = pygame.time.Clock()
speed = 3
size_change_factor = 0.25
increasing = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect_y += speed
    rect_x += speed

    vertical_rect_y += speed        
    horizontal_rect_x += speed  

    if rect_y > height:
        rect_y = -rect_height
    if rect_x > width:
        rect_x = -rect_width

    if vertical_rect_y > height:
        vertical_rect_y = -vertical_rect_height
    if horizontal_rect_x > width:
        horizontal_rect_x = -horizontal_rect_width

    if increasing:
        rect_width *= 1 + size_change_factor
        rect_height *= 1 + size_change_factor

        vertical_rect_width *= 1 + size_change_factor
        vertical_rect_height *= 1 + size_change_factor

        horizontal_rect_width *= 1 + size_change_factor
        horizontal_rect_height *= 1 + size_change_factor

        if rect_width > 1.25 * 100:
            increasing = False
    else:
        rect_width /= 1 + size_change_factor
        rect_height /= 1 + size_change_factor

        vertical_rect_width /= 1 + size_change_factor
        vertical_rect_height /= 1 + size_change_factor

        horizontal_rect_width /= 1 + size_change_factor
        horizontal_rect_height /= 1 + size_change_factor

        if rect_width < 100:
            increasing = True

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(screen, vertical_rect_color, (vertical_rect_x, vertical_rect_y, vertical_rect_width, vertical_rect_height))
    pygame.draw.rect(screen, horizontal_rect_color, (horizontal_rect_x, horizontal_rect_y, horizontal_rect_width, horizontal_rect_height))

    pygame.display.flip()

    clock.tick(fps)
