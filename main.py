# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from game_map import GameMap

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Load sprites
    floor_sprite = pygame.image.load('sprites/walls_0042_Layer-43').convert_alpha()
    wall_sprite = pygame.image.load('sprites/walls_0042_Layer-43').convert_alpha()
    sprite_sheet = pygame.image.load('sprites/sprite_oldman.png').convert_alpha()

    # Create instances of the Player and GameMap
    player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), sprite_sheet)
    game_map = GameMap()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)
        screen.fill((0, 0, 0))
        game_map.draw(screen, floor_sprite, wall_sprite)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
