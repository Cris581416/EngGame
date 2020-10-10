import pygame
from pygame import *
from os import path
import sys
import player
from loops import *

pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.init()

print(sys.path)

height = int(1536/3)
width = int(3072/3)
fps = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption(u"Oedipus Project")
screen = pygame.display.set_mode(size=(width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (74, 20, 140)

# Files
image_dir = path.join(path.dirname(__file__), 'images')
text_dir = path.join(path.dirname(__file__), 'texts')
sound_dir = path.join(path.dirname(__file__), 'sounds')
bckgrnd_list = ["full_bg", "tile_ground", "title_bg"]
bckgrnd_dict = {}
for image in bckgrnd_list:
    i = image + '.png'
    bckgrnd_dict[image] = pygame.image.load(path.join(image_dir, i)).convert()
bckgrnd_dict["full_bg"] = pygame.transform.scale(bckgrnd_dict["full_bg"], (width, height))
bckgrnd_dict["title_bg"] = pygame.transform.scale(bckgrnd_dict["title_bg"], (width, height))
image_list = ["title"]
image_dict = {}
for image in image_list:
    i = image + '.png'
    image_dict[image] = pygame.image.load(path.join(image_dir, i)).convert()
image_dict["title"].set_colorkey(white)

# Fonts 
arial = pygame.font.match_font('arial')
jackeyfont = pygame.font.match_font('jackeyfont')

# Player
oedipus = player.Player(screen)

# Sprites
all_sprites = pygame.sprite.Group(oedipus)

looping = True
loops = {"Menu": True, "Plot Summary": False, "Character List": False, "Theme": False,
         "Kahlo": False, "Game": False}
maps = {"t": "Menu", "y": "Plot Summary", "u": "Character List", "i": "Theme", "o": "Kahlo",
        "p": "Game"}
quit_game = True
clock.tick(30)
while looping:
    while loops["Menu"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                loops["Menu"] = False

        title.run(screen, oedipus, bckgrnd_dict, image_dict, width, height)

        # all_sprites.draw(screen)

        pygame.display.flip()





    if quit_game:
        looping = False
        for key in loops:
            loops[key] = False
        pygame.quit()
