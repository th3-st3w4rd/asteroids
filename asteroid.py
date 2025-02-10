from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="white",
            radius=self.radius,
            center=(self.position.x, self.position.y),
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
