import pygame
import settings

from world import World

class Game:
    """
    Main application controller

    It handles the main game loop, process de input events, updates the application 
    states, and renders all the objects.
    """

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H))
        self.clock = pygame.time.Clock()

        self.world = World()

        self.running = True

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt: float) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill((0,0,0))
        self.world.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:

        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
            self.draw()

        pygame.quit()




