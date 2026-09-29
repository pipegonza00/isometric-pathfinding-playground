import pygame
import settings

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

        self.running = True

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt: float) -> None:
        pass

    def draw(self) -> None:
        pass

    def run(self) -> None:

        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
            

        pygame.quit()




