import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

class Level():
    # setting up the map with the data entered in settings.py
    def __init__(self, level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)

        # This will allow the map to move with player
        self.world_shift = 0


    # This is allowing me to make a grid.  by using my For loop I can loop through my Level array and add my Tile Class blocks to each space that contains a 'X' and a player to the place that has a 'P'
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            # print(row)
            # print(row_index)
            for column_index, column in enumerate(row):
                # print(f'{row_index},{column_index}:{column}')
                if column == 'X':
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    # This will stop my player from moving through a block when its hit
    def horizontal_move_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    # Same for this one
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    # This is what allows for my screen to move.  When the screen moves the players speed actually stops and the screen moves which gives it the effect that the whole thing is moving
    def scroll_x(self):
        player = self.player.sprite  
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.horizontal_move_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.scroll_x()