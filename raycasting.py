
#THIS IS ONLY FOR THE 2D MAP I USED TO TEST

import math
from settings import *
from map import *
from player import *

def ray_casting(player_pos, ray_angle, ray_length):
    """Casts a ray and checks for wall collisions."""
    ray_x, ray_y = player_pos
    ray_dx = math.cos(ray_angle)
    ray_dy = math.sin(ray_angle)

    # Step through the ray in small increments
    for t in range(ray_length):
        # Update ray position
        ray_x += ray_dx
        ray_y += ray_dy
        
        # Check if the ray is inside a wall
        grid_x = int(ray_x // TILE) * TILE
        grid_y = int(ray_y // TILE) * TILE
        
        if (grid_x, grid_y) in world_map:
            pass
            #return ray_x, ray_y  # Return the collision point

    # No collision, return the max distance point
    return player_pos[0] + ray_length * ray_dx, player_pos[1] + ray_length * ray_dy
