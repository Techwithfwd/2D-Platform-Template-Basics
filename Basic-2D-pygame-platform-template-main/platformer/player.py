import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.Surface((32,60))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = position)

        # Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.gravity_value = 0.8
        self.jump_speed = -16
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1 
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def gravity(self):
        self.direction.y += self.gravity_value
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.gravity()
