# game_map.py
import pygame
from settings import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class GameMap:
    def __init__(self):
        self.tiles = self.generate_map()

    def generate_map(self):
        # Define the map layout
        # 1 represents wall, 0 represents floor
        game_map = [[1 if x == 0 or x == (SCREEN_WIDTH // TILE_SIZE) - 1 or y == 0 or y == (SCREEN_HEIGHT // TILE_SIZE) - 1 else 0 for x in range(SCREEN_WIDTH // TILE_SIZE)] for y in range(SCREEN_HEIGHT // TILE_SIZE)]
        return game_map

    def draw(self, screen, floor_sprite, wall_sprite):
        for row_index, row in enumerate(self.tiles):
            for col_index, tile in enumerate(row):
                if tile == 0:
                    screen.blit(floor_sprite, (col_index * TILE_SIZE, row_index * TILE_SIZE))
                elif tile == 1:
                    screen.blit(wall_sprite, (col_index * TILE_SIZE, row_index * TILE_SIZE))
