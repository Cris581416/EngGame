import pygame
from pygame import *
from pygame import surface
import random
from os import path
import sys
import player

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
bckgrnd_list = ["full_bg", "tile_ground"]
bckgrnd_dict = {}
for image in bckgrnd_list:
    i = image + '.png'
    bckgrnd_dict[image] = pygame.image.load(path.join(image_dir, i)).convert()
bckgrnd_dict["full_bg"] = pygame.transform.scale(bckgrnd_dict["full_bg"], (width, height))
image_list = ["title"]
image_dict = {}
for image in image_list:
    i = image + '.png'
    image_dict[image] = pygame.image.load(path.join(image_dir, i)).convert()
image_dict["title"].set_colorkey(white)

# Fonts 
arial = pygame.font.match_font('arial')
jackeyfont = pygame.font.match_font('jackeyfont')


class TextBox:
    def __init__(self, text, pos, rect_size, font, size, bg_color, text_color=(255, 255, 255)):
        self.fnt = pygame.font.Font(font, size)
        self.font_height = self.fnt.get_linesize()
        self.text = text.split(' ')  # Single words.
        self.rect = pygame.Rect(pos, rect_size)
        self.bg_color = bg_color
        self.text_color = text_color
        self.render_text_surfaces()
        self.images = []

    def render_text_surfaces(self):
        """Create a new text images list when the rect gets scaled."""
        self.images = []  # The text surfaces.
        line_width = 0
        line = []
        # Put the words one after the other into a list if they still
        # fit on the same line, otherwise render the line and append
        # the resulting surface to the self.images list.
        for word in self.text:
            line_width += self.fnt.size(word)[0]
            # Render a line if the line width is greater than the rect width.
            if line_width > self.rect.w:
                surf = self.fnt.render(''.join(line), True, self.text_color)
                self.images.append(surf)
                line = []
                line_width = self.fnt.size(word)[0]

            line.append(word)

        # Need to render the last line as well.
        surf = self.fnt.render(' '.join(line), True, self.text_color)
        self.images.append(surf)

    def draw(self, screen):
        """Draw the rect and the separate text images."""
        pygame.draw.rect(screen, self.bg_color, self.rect)

        for y, surf in enumerate(self.images):
            # Don't blit below the rect area.
            if y * self.font_height + self.font_height > self.rect.h:
                break
            screen.blit(surf, (self.rect.x, self.rect.y + y * self.font_height))

    def scale(self, rel):
        self.rect.w += rel[0]
        self.rect.h += rel[1]
        self.rect.w = max(self.rect.w, 30)  # 30 px is the minimum width.
        self.rect.h = max(self.rect.h, 30)
        self.render_text_surfaces()

    def move(self, rel):
        self.rect.move_ip(rel)
        self.rect.clamp_ip(screen.get_rect())


looping = True
loops = {"Menu": True, "Plot Summary": False, "Character List": False, "Theme": False,
         "Kahlo": False}
maps = {"t": "Menu", "y": "Plot Summary", "u": "Character List", "i": "Theme", "o": "Kahlo"}
quit_game = True
while looping:
    while loops["Menu"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                loops["Menu"] = False

        keys = pygame.key.get_pressed()

        screen.blit(bckgrnd_dict["full_bg"], (0, 0, width, height))
        screen.blit(image_dict["title"], (300, -100, 500, 500))

        pygame.display.flip()

    if quit_game:
        looping = False
        for key in loops:
            loops[key] = False
        pygame.quit()
