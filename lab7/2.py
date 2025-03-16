import pygame
import os

pygame.init()

playlist = []
music_folder = r"C:\Users\Алуа\Desktop\PP2\lab7\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Songs")
clock = pygame.time.Clock()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (600, 600))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 40)

playb = pygame.image.load("play.png")
pausb = pygame.image.load("pause.png")
nextb = pygame.image.load("next.png")
prevb = pygame.image.load("back.png")

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()
aplay = True

while True:
    screen.fill((255, 255, 255))
    screen.blit(background, (100, 50))
    screen.blit(bg, (150, 620))
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    text_rect = text2.get_rect(center=(screen_width // 2, 640))
    screen.blit(text2, text_rect)
    
    screen.blit(prevb, (273, 680))
    if aplay:
        screen.blit(pausb, (370, 685))
    else:
        screen.blit(playb, (370, 685))
    screen.blit(nextb, (460, 682))
    
    pygame.display.update()
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True
            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 370 <= x <= 440 and 685 <= y <= 755:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay
            elif 460 <= x <= 530 and 682 <= y <= 752:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True
            elif 273 <= x <= 348 and 680 <= y <= 755:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True
