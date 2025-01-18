import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    """
    Represents an asteroid in the game. Moves in a straight line at a constant speed.
    """
    containers = None  # This will be set to sprite groups in main.py

    def __init__(self, x, y, radius):
       
        super().__init__(x, y, radius)
        
        # Set a random velocity for the asteroid
        angle = random.uniform(0, 360)
        speed = random.uniform(50, 150)  # Random speed between 50 and 150 units/second
        self.velocity = pygame.Vector2(speed, 0).rotate(angle)

    def draw(self, screen):
        """
        Draw the asteroid as a circle.
        """
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        """
        Update the asteroid's position based on its velocity.
        """
        self.position += self.velocity * dt

    def split(self):
        # Kill this asteroid (it will be removed from groups)
        self.kill()

        # If the asteroid is too small, don't split it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Rotate the velocity vector to create two new velocities
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Compute new radii for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2 
