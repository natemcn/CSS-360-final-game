import pygame
from settings import *
from player import Player
import math
from map import *
from raycasting import *
from renderer import *


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)



clock = pygame.time.Clock()
player = Player()
ray_length = 1000


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
    
    sc.fill(BLACK)
    
    
    #FOR 2D MAP
    for x, y in world_map:
        pass
        #pygame.draw.rect(sc, CADBLUE, (x,y,TILE,TILE),2)
    
   

 
    player.wall_collision(player.x,player.y)
    
    
    player.movement()
    
  
 
    
    #FOR 2D
    #pygame.draw.circle(sc,MGREEN,player.pos,12)
    #follows mouse
    #Mouse_x, Mouse_y = pygame.mouse.get_pos()
    #player_pos = (player.x,player.y)
    
    
    #3D rendering
    mx = pygame.mouse.get_rel()[0]
    player.angle += mx * 0.003  # tweak sensitivity here
    player.angle %= 2 * math.pi  # keep angle bounded

    pygame.mouse.set_pos(WIDTH // 2, HEIGHT // 2)
    pygame.mouse.get_rel()  
    #reset mouse to avoid getting stuck on side
 
     # draw scene
    sc.fill((0, 0, 0))  # clear screen
    render_3d_view(sc, player.pos, player.angle)
   
    


    #FOR 2D raycast
    """
    for i in range(NUM_RAYS):
        # Calculate angle for each ray
        base_angle = math.atan2(Mouse_y - player.y, Mouse_x - player.x)
        
        # Create some variation in the rays' angles
        angle_variation = (i - NUM_RAYS / 2) * (math.pi / NUM_RAYS)
        ray_angle = base_angle + angle_variation / math.pi
        
        # Cast the ray and get the collision point or max distance point
        ray_end_x, ray_end_y = ray_casting(player_pos, ray_angle, 500)
        
        # Draw the ray (stop at collision if detected)
        pygame.draw.line(sc, MGREEN, player.pos, (ray_end_x, ray_end_y))
    """


    """"
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    FOV working
    for i in range(NUM_RAYS):
        # Calculate angle for each ray
        angle = math.atan2(Mouse_y - player.y, Mouse_x - player.x)
        
        # Create some variation in the rays' angles
        angle_variation = (i - NUM_RAYS / 2) * (math.pi / NUM_RAYS)
        ray_angle = angle + angle_variation / math.pi
        
        ray_end_x = player.x + ray_length * math.cos(ray_angle)
        ray_end_y = player.y + ray_length * math.sin(ray_angle)


        
        
        # Calculate the end point of the ray
        
        pygame.draw.line(sc, MGREEN, player.pos, (ray_end_x,ray_end_y))
  
    """



    """"

    1 ray working
    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    angle = math.atan2(Mouse_y - player.y, Mouse_x - player.x)
    ray_end_x = player.x + ray_length * math.cos(angle)
    ray_end_y = player.y + ray_length * math.sin(angle)
    

    pygame.draw.line(sc, MGREEN, player.pos, (ray_end_x,ray_end_y))
      """  
    
   


    pygame.display.flip()
    clock.tick(FPS)


