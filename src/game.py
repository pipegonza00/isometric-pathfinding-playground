import pygame
import settings

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H))
        self.clock = pygame.time.Clock()

        self.running = True

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass

    def run(self) -> None:

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()




