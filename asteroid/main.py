# import pygame
# from constants import *
# from player import Player

# def main():
#     # Initialize pygame
#     pygame.init()

#     # Set up the screen
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Player Game")

#     # Create a clock object and initialize delta time
#     clock = pygame.time.Clock()
#     dt = 0  # Delta time in seconds

#     # Create two groups: updatable and drawable
#     updatables = pygame.sprite.Group()
#     drawables = pygame.sprite.Group()

#     # Instantiate the player and add it to both groups
#     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     updatables.add(player)
#     drawables.add(player)

#     # Game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return  # Exit the game loop if the user closes the window

#         # Update and draw all objects
#         for sprite in updatables:
#             sprite.update(dt)

#         # Fill the screen with a solid black color
#         screen.fill((0, 0, 0))

#         for sprite in drawables:
#             sprite.draw(screen)

#         # Refresh the screen
#         pygame.display.flip()

#         # Limit the frame rate to 60 FPS and calculate delta time
#         dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

# if __name__ == "__main__":
#     main()


import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Game")

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # New group for shots

    # Assign group containers
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)  # Add Shot to groups

    # Create the asteroid field
    asteroid_field = AsteroidField()

    # Instantiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Clock and delta time
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    font = pygame.font.Font(None, 36)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the user closes the window

        # Update all updatable objects
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):  # Use the collision method we added to CircleShape
                    asteroid.kill()  # Remove asteroid from groups
                    shot.kill()  # Remove shot from groups
                    print("Asteroid destroyed!")
                    score += 5  # Increment score for destroying an asteroid
                    asteroid.split()

        for asteroid in asteroids:
            if player.collide(asteroid):  # If the player collides with an asteroid
                print("Game over!")
                pygame.quit()  # End the game
                return  # Exit the game loop
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        # Refresh the screen
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
