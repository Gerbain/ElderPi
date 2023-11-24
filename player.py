import pygame
from settings import TILE_SIZE, CHARACTER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, body_sheet, hand_sheet, weapon_sheets, frame_counts):
        super().__init__()
        self.body_animations = self.load_sprites(body_sheet, frame_counts)
        self.hand_animations = self.load_sprites(hand_sheet, frame_counts)
        # Assuming the same frame counts for body and hands; adjust if different
        self.weapon_animations = {weapon: self.load_sprites(sheet, frame_counts) for weapon, sheet in weapon_sheets.items()}
      
        self.current_weapon = 'pistol'  # Example weapon
        self.current_animation = 'idle'
        self.frame_index = 0

        self.image = None  # To be created in the render method
        self.rect = pygame.Rect(pos, (TILE_SIZE, TILE_SIZE))

    def load_sprites(self, sprite_sheet, frame_counts):
        animations = {}
        row = 0
        for anim, num_frames in frame_counts.items():
            animations[anim] = []
            for col in range(num_frames):
                frame = sprite_sheet.subsurface(pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                animations[anim].append(frame)
            row += 1  # Move to the next row for the next animation
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

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
            self.current_animation = 'walk'
        else:
            self.current_animation = 'idle'

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Update the frame index
        self.frame_index = (self.frame_index + 1) % len(self.body_animations[self.current_animation])


    def render(self):
        body_frame = self.body_animations[self.current_animation][self.frame_index]
        hand_frame = self.hand_animations[self.current_animation][self.frame_index]
        weapon_frame = self.weapon_animations[self.current_weapon][self.current_animation][self.frame_index]

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        self.image.blit(body_frame, (0, 0))
        self.image.blit(hand_frame, (0, 0))  # Adjust these coordinates if needed
        self.image.blit(weapon_frame, (0, 0))  # Adjust these coordinates if needed

