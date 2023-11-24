# player.py
import pygame
from settings import TILE_SIZE, CHARACTER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_sheet):
        super().__init__()
        self.sprites = self.load_sprites(sprite_sheet)
        self.current_sprite = self.sprites['idle'][0]
        self.rect = self.current_sprite.get_rect(center=pos)
        self.speed = CHARACTER_SPEED
        self.direction = pygame.math.Vector2(0, 0)

    def load_sprites(self, sprite_sheet):
        animations = {
            'idle': [],
            'walk': []
        }
        col_offset = 1  # Offset due to the first column being blank

        for row, anim in enumerate(animations.keys()):
            for col in range(4):  # Assuming 4 frames per animation
                frame = sprite_sheet.subsurface(pygame.Rect((col + col_offset) * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                animations[anim].append(frame)

        return animations

    def update(self, keys):
        self.direction.x, self.direction.y = 0, 0  # Reset movement direction

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1

        # Normalize direction vector to ensure consistent speed diagonally
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Update position
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Update animation
        # Add logic here to switch between 'idle' and 'walk' animations based on movement

    def draw(self, screen):
        screen.blit(self.current_sprite, self.rect.topleft)
