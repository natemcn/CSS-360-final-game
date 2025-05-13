from settings import *
import pygame
from map import *


def render_3d_view(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    ox, oy = player_pos

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(MAX_DEPTH):
            x = ox + depth * cos_a
            y = oy + depth * sin_a
            tile_x, tile_y = int(x // TILE) * TILE, int(y // TILE) * TILE

            if (tile_x, tile_y) in world_map:
                depth *= math.cos(player_angle - cur_angle)  # fix fish-eye
                proj_height = PROJ_COEFF / (depth + 0.0001)
                shade = 255 / (1 + depth * depth * 0.0001)
                color = (shade, shade, shade)

                pygame.draw.rect(sc, color,
                    (ray * SCALE, HEIGHT // 2 - proj_height // 2, SCALE, proj_height))
                break

        cur_angle += DELTA_ANGLE
