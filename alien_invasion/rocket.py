'''12-4. Rocket: Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left, or right using the four arrow keys. Make sure the rocket never moves beyond any edge of the screen.'''

import pygame

class Rocket:
    '''A class to manage the rocket.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load(r'C:\Users\kellyincville\.vscode\CS121\CSC121\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the rocket's exact horizontal position.
        self.x = float(self.rect.x)

        # Store a float for the rocket's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flag; start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        '''Update the rocket's position based on the movement flag.'''
        # Update the rocket's x and y value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Draw the rocket at its current location.'''
        self.screen.blit(self.image, self.rect)

