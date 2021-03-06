import pygame
from pygame import *


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

    def move(self, screen, rel):
        self.rect.move_ip(rel)
        self.rect.clamp_ip(screen.get_rect())
