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
        if dir == "UP":
            self.pos.y -= 5 * dt
        elif dir == "DOWN":
            self.pos.y += 5 * dt
        elif dir == "LEFT":
            self.pos.x -= 5 * dt
        elif dir == "RIGHT":
            self.pos.x += 5 * dt

class Snake:
    snakeList = []

    def __init__(self, surface) -> None:
        self.snakeList.append(SnakeTile(pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)))

    def draw():
        pass


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    dir = "UP"
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        pygame.draw.rect(screen, "red", pygame.Rect(player_pos.x, player_pos.y, 35, 35))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()