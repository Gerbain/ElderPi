import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Title")
    clock = pygame.time.Clock()

    # Load sprite sheets
    body_sheet = pygame.image.load('sprites/Heroes/Rogue/Idle_sheet.png').convert_alpha()
    hand_sheet = pygame.image.load('sprites/Weapons/Hands/Hands.png').convert_alpha()
    weapon_sheets = {
        'pistol': pygame.image.load('sprites/Weapons/Hands/Hands.png').convert_alpha(),
        # Add other weapons as needed
    }

    # Create Player instance
    player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), body_sheet, hand_sheet, weapon_sheets)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        screen.fill((0, 0, 0))  # Clear the screen with black (or any other background)

        player.render()  # Render the player
        screen.blit(player.image, player.rect.topleft)  # Draw the player on the screen

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the specified FPS

    pygame.quit()

if __name__ == '__main__':
    main()
