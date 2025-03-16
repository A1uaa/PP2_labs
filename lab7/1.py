import pygame
from datetime import datetime

pygame.init()

background = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

WIDTH, HEIGHT = background.get_size()
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = datetime.now()
    minutes = current_time.minute
    seconds = current_time.second
    
    minute_angle = -6 * minutes
    second_angle = -6 * seconds
    
    rotated_minute = pygame.transform.rotate(min_hand, minute_angle)
    rotated_second = pygame.transform.rotate(sec_hand, second_angle)
    
    screen.blit(background, (0, 0))
    screen.blit(rotated_minute, rotated_minute.get_rect(center=CENTER).topleft)
    screen.blit(rotated_second, rotated_second.get_rect(center=CENTER).topleft)
    
    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
