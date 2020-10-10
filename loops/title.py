import pygame


def run(screen, p1, bk_dict, img_dict, w, h):
    keys = pygame.key.get_pressed()

    p1.update()

    screen.blit(bk_dict["title_bg"], (0, 0, w, h))
    screen.blit(img_dict["title"], (300, -100, 500, 500))

    pygame.draw.rect(screen, (255, 0, 0), p1.rect)

    pygame.display.flip()
