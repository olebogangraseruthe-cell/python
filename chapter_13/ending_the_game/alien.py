import pygame

from pathlib import Path
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        # Initialize the parent Sprite class.
        # This allows aliens to work with Pygame sprite groups.
        super().__init__()

        # Store references to the game's screen and settings.
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Build the path to the alien image relative to this file.
        # The image is stored inside the images folder.
        image_path = Path(__file__).parent / 'images' / 'alien.bmp'
        self.image = pygame.image.load(str(image_path))

        # Create a rectangle that represents the image's size
        # and position. Pygame uses this rectangle for positioning
        # and collision detection.
        self.rect = self.image.get_rect()

        # Position the alien near the top-left corner.
        # One alien-width of space is left from the left edge.
        self.rect.x = self.rect.width

        # One alien-height of space is left from the top edge.
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position as a float.
        # This supports movement at fractional speeds.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""

        # Get a rectangle representing the screen boundaries.
        screen_rect = self.screen.get_rect()

        # Return True if the alien reaches the right edge
        # or the left edge. Otherwise, return False.
        return (
            self.rect.right >= screen_rect.right
            or self.rect.left <= 0
        )

    def update(self):
        """Move the alien right or left."""

        # Move the alien horizontally.
        # alien_speed controls the speed, while fleet_direction
        # determines whether the fleet moves right or left.
        self.x += (
            self.settings.alien_speed
            * self.settings.fleet_direction
        )

        # Update the rectangle so the alien is drawn
        # at its new horizontal position.
        self.rect.x = self.x