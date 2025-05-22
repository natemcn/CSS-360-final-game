import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=__, health=___): #finalize values
        super().__init__()
        #Finish screen drawing implementation with sprites

        self.speed = speed
        self.health = health

        self.wander_timer = 0
        self.wander_interval = 1000  
        self.direction_vector = pygame.math.Vector2(0, 0)

    def update(self, player_pos):
        now = pygame.time.get_ticks()
        if now - self.wander_timer > self.wander_interval:
            self.set_random_direction()
            self.wander_timer = now

        self.wander(wall) #update enemy state

        if self.distance_to(player_pos) < ___: #finish this
            self.chase(player_pos, wall_group)
        else:
            self.wander(wall_group)


#STATE FUNCTIONS
    def set_random_direction(self):
        angle = random.uniform(0, 2 * math.pi)
        self.direction_vector = pygame.math.Vector2(math.cos(angle), math.sin(angle)).normalize()

    def wander(self, wall):
        #
        self.rect.x += self.direction_vector.x * self.speed
        self.rect.y += self.direction_vector.y * self.speed

        if pygame.sprite.spritecollideany(self, wall_group): #if collosion detected
            #need sprite implementation

            self.rect.topleft = old_pos
            self.set_random_direction()

    def chase(self, player_pos, speed, wall):
        self.speed *= 1.65 #LOS increase
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery

        distance = math.hypot(dy, dx)
    

    def attack(self, player):
        if self.distance_to(player.rect.topleft) < ___: #finish this
            player.health -= __ #finish this
            self.speed = 0
            self.wander_timer = pygame.time.get_ticks() + 1000


    def distance_to(self, pos):
        return math.hypot(self.rect.centerx - pos[0], self.rect.centery - pos[1])
