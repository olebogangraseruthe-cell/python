import sys
from time import sleep

import pygame

# Import the classes needed to run the game.
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        # Initialize Pygame so its features are ready to use.
        pygame.init()

        # Create a clock to control the game's frame rate.
        self.clock = pygame.time.Clock()

        # Load the game settings from the Settings class.
        self.settings = Settings()

        # Create the game window using the width and height
        # defined in settings.py.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Set the title displayed at the top of the game window.
        pygame.display.set_caption("Alien Invasion")

        # Create an object to track statistics, such as ships remaining.
        self.stats = GameStats(self)

        # Create the player's ship.
        self.ship = Ship(self)

        # Create a sprite group to store all active bullets.
        self.bullets = pygame.sprite.Group()

        # Create a sprite group to store all active aliens.
        self.aliens = pygame.sprite.Group()

        # Create the initial fleet of aliens.
        self._create_fleet()

        # Set the game to an active state so gameplay can begin.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""

        # Keep the game running until the player exits.
        while True:

            # Check for keyboard input and other events.
            self._check_events()

            # Update game objects only while the game is active.
            if self.game_active:
                # Update the ship's position.
                self.ship.update()

                # Move bullets and check for bullet-alien collisions.
                self._update_bullets()

                # Move aliens and check for collisions with the ship.
                self._update_aliens()

            # Draw all visible game objects on the screen.
            self._update_screen()

            # Limit the game to approximately 60 frames per second.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # Get all events waiting to be processed by Pygame.
        for event in pygame.event.get():

            # Close the game when the window's close button is clicked.
            if event.type == pygame.QUIT:
                sys.exit()

            # Respond when a keyboard key is pressed down.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # Respond when a keyboard key is released.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        # Start moving the ship to the right.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        # Start moving the ship to the left.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Exit the game when the Q key is pressed.
        elif event.key == pygame.K_q:
            sys.exit()

        # Fire a bullet when the spacebar is pressed.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        # Stop moving right when the right arrow is released.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        # Stop moving left when the left arrow is released.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        # Only fire a bullet if the number of active bullets
        # is below the maximum allowed in settings.py.
        if len(self.bullets) < self.settings.bullets_allowed:

            # Create a new bullet at the ship's current position.
            new_bullet = Bullet(self)

            # Add the bullet to the sprite group so it can be updated
            # and drawn by the game.
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Call the update() method of every bullet in the group.
        # Each bullet moves upwards.
        self.bullets.update()

        # Loop through a copy of the bullet group so bullets can
        # safely be removed from the original group.
        for bullet in self.bullets.copy():

            # Remove a bullet when its bottom edge reaches the top
            # of the screen or moves beyond it.
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check whether any bullets have collided with aliens.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""

        # Detect collisions between bullets and aliens.
        # The third argument, True, removes a colliding bullet.
        # The fourth argument, True, removes a colliding alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        # If no aliens remain, the player has destroyed the fleet.
        if not self.aliens:

            # Remove any remaining bullets from the screen.
            self.bullets.empty()

            # Create a new fleet for the next round.
            self._create_fleet()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        # Check whether the player has any ships remaining.
        if self.stats.ships_left > 0:

            # Reduce the number of remaining ships by one.
            self.stats.ships_left -= 1

            # Remove all bullets from the current round.
            self.bullets.empty()

            # Remove all aliens from the current fleet.
            self.aliens.empty()

            # Create a fresh fleet of aliens.
            self._create_fleet()

            # Return the player's ship to the bottom-middle
            # of the screen.
            self.ship.center_ship()

            # Pause briefly before the game continues.
            sleep(0.5)

        else:
            # No ships remain, so stop active gameplay.
            self.game_active = False

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""

        # Check whether any alien has reached a screen edge.
        # If so, the fleet must change direction and move down.
        self._check_fleet_edges()

        # Call update() on every alien in the sprite group.
        self.aliens.update()

        # Check whether an alien has collided with the player's ship.
        # spritecollideany() returns an alien if a collision occurs.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check whether any alien has reached the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""

        # Loop through every alien currently in the fleet.
        for alien in self.aliens.sprites():

            # Check whether the alien's bottom edge has reached
            # or passed the bottom of the screen.
            if alien.rect.bottom >= self.settings.screen_height:

                # Treat an alien reaching the bottom like a ship hit.
                self._ship_hit()

                # Stop checking because a ship hit has been handled.
                break

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create a temporary alien to determine the size of an alien.
        # Its dimensions are used to calculate the fleet spacing.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Start the first alien one alien-width from the left edge
        # and one alien-height from the top.
        current_x, current_y = alien_width, alien_height

        # Keep creating rows while there is enough vertical space.
        # The extra three alien-heights leave space at the bottom.
        while current_y < (
            self.settings.screen_height - 3 * alien_height
        ):

            # Add aliens across the current row while there is
            # enough horizontal space.
            while current_x < (
                self.settings.screen_width - 2 * alien_width
            ):

                # Create an alien at the current coordinates.
                self._create_alien(current_x, current_y)

                # Move to the next position, leaving one alien-width
                # of space between adjacent aliens.
                current_x += 2 * alien_width

            # The current row is complete.
            # Start again at the left side for the next row.
            current_x = alien_width

            # Move down to the next row, leaving one alien-height
            # of space between rows.
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""

        # Create a new Alien object.
        new_alien = Alien(self)

        # Set the alien's exact horizontal position.
        new_alien.x = x_position

        # Set the rectangle's horizontal position.
        new_alien.rect.x = x_position

        # Set the rectangle's vertical position.
        new_alien.rect.y = y_position

        # Add the alien to the fleet so it can be updated and drawn.
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""

        # Check every alien to see whether it has reached an edge.
        for alien in self.aliens.sprites():

            # check_edges() returns True if the alien reaches
            # either the left or right edge of the screen.
            if alien.check_edges():

                # Drop the entire fleet and reverse its direction.
                self._change_fleet_direction()

                # Stop checking because the fleet has already changed.
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction."""

        # Move every alien down by the configured number of pixels.
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        # Reverse the horizontal direction of the fleet.
        # Multiplying 1 by -1 gives -1, and vice versa.
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Clear the previous frame by filling the screen
        # with the configured background colour.
        self.screen.fill(self.settings.bg_color)

        # Draw every active bullet.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the player's ship at its current position.
        self.ship.blitme()

        # Draw all aliens in the fleet.
        self.aliens.draw(self.screen)

        # Display the completed frame.
        # This updates the window so the player can see the changes.
        pygame.display.flip()


# Run the game only when this file is executed directly.
# This prevents the game from starting automatically if the file
# is imported into another Python file.
if __name__ == '__main__':

    # Create an instance of the AlienInvasion class.
    ai = AlienInvasion()

    # Start the main game loop.
    ai.run_game()
