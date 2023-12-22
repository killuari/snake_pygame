# Example file showing a circle moving on screen
import pygame

class SnakeTile:
    pos = pygame.Vector2(0, 0)
    size = 35
    color = 'green'

    def __init__(self, pos: pygame.Vector2) -> None:
        self.pos = pos

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

    def move(self, dir, dt):
        # print(f"self.pos = {self.pos} (Before Move)")
        if dir == "UP":
            self.pos.y -= self.size *dt
        elif dir == "DOWN":
            self.pos.y += self.size *dt
        elif dir == "LEFT":
            self.pos.x -= self.size *dt
        elif dir == "RIGHT":
            self.pos.x += self.size *dt
        # print(f"self.pos = {self.pos} (After Move)")

    def getPos(self):
        return self.pos
    
    def setPos(self, pos):
        self.pos = pos

class Snake:
    snakeList = []
    surface = 0
    size = 0

    def __init__(self, surface) -> None:
        self.snakeList.append(SnakeTile(pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)))
        self.surface = surface
        self.size = self.snakeList[-1].size

    def draw(self):
        for tile in self.getSnakeList():
            tile.draw(self.surface)

    def move(self, dir, dt):
        pos = self.snakeList[0].pos.copy()
        self.snakeList[0].move(dir, dt)
        for tile in self.snakeList[1:]:
            p = tile.getPos()
            tile.setPos(tile.getPos().move_towards(pos, self.size * dt))
            pos = p

    def addTile(self):
        self.snakeList.append(SnakeTile(pygame.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)))

    def getSnakeList(self):
        return self.snakeList


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    dir = "UP"

    snake = Snake(screen)

    while running:

        # limits FPS to 60
        dt = clock.tick(60) / 100

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    snake.addTile()
                if event.key == pygame.K_w:
                    dir = "UP"
                if event.key == pygame.K_s:
                    dir = "DOWN"
                if event.key == pygame.K_a:
                    dir = "LEFT"
                if event.key == pygame.K_d:
                    dir = "RIGHT"


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        snake.move(dir, dt)
        snake.draw()

        # flip() the display to put your work on screen
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()