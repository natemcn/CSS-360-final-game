from settings import *
import pygame
import math
from map import *

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = player_speed

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def int_pos(self):
        return int(self.x), int(self.y)

    def movement(self):
        keys = pygame.key.get_pressed()

        # Calculate directional movement based on angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        dx, dy = 0, 0

        # Move forward
        if keys[pygame.K_w]:
            dx += cos_a * self.speed
            dy += sin_a * self.speed
        # Move backward
        if keys[pygame.K_s]:
            dx -= cos_a * self.speed
            dy -= sin_a * self.speed
        # Strafe left
        if keys[pygame.K_a]:
            dx += sin_a * self.speed
            dy -= cos_a * self.speed
        # Strafe right
        if keys[pygame.K_d]:
            dx -= sin_a * self.speed
            dy += cos_a * self.speed

        # Apply movement with collision detection
        self.check_collision(dx, dy)

    def check_collision(self, dx, dy):
        """Move player while checking for wall collisions."""
        next_x = self.x + dx
        next_y = self.y + dy

        if not self.wall_collision(next_x, self.y):
            self.x = next_x
        if not self.wall_collision(self.x, next_y):
            self.y = next_y

    def wall_collision(self, x, y):
        """Return True if (x, y) collides with a wall."""
        grid_x = int(x // TILE) * TILE
        grid_y = int(y // TILE) * TILE
        return (grid_x, grid_y) in world_map
