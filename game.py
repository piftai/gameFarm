import pygame


class Game:
    def __init__(self, SIZE_FIELD_HEIGHT, SIZE_FIELD_WIDTH):
        self.SIZE_FIELD_WIDTH = SIZE_FIELD_WIDTH
        self.SIZE_FIELD_HEIGHT = SIZE_FIELD_HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SIZE_FIELD_WIDTH, self.SIZE_FIELD_HEIGHT))
        pygame.display.set_caption("Farm")


    def run(self):
        run = True
        while run:
            self.clock.tick(60)
            self.screen.fill("grey100")
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()