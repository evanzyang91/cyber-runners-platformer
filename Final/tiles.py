import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, size, x, y):
        
        super().__init__()
        self.image = pygame.Surface((size, size))
        
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, xSpeed):
        self.rect.x += xSpeed

class StaticTile(Tile):

    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

