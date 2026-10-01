import pygame
import settings

class World:
    
    def __init__(self) -> None:

        self.tile_map = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

        self.map_height = len(self.tile_map)
        self.map_width = len(self.tile_map[0])

    def update(self) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:

        offset_x = (settings.SCREEN_W - (self.map_width * settings.TILE_SIZE)) / 2
        offset_y = (settings.SCREEN_H - (self.map_height * settings.TILE_SIZE)) / 2

        for i in range(self.map_height):
            for j in range(self.map_width):
                rect = pygame.Rect(settings.TILE_SIZE * j + offset_x, settings.TILE_SIZE * i + offset_y, settings.TILE_SIZE, settings.TILE_SIZE)

                if(i + j) % 2:
                    pygame.draw.rect(surface, settings.LIGHT_GRAY, rect)

                else:
                    pygame.draw.rect(surface, settings.DARK_GRAY, rect)
    