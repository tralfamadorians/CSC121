'''12-2. Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen, then match the background color of the image to the back-
ground color of the screen or vice versa.'''

import pygame

class Cat:
    '''A class to manage the cat.'''

    def __init__(self, ai_game):
        '''Initialize the cat and set its starting position.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the cat image and get its rect.
        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()

        # Start each new cat at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self)
        '''Draw the cat at its current location.'''
        self.screen.blit(self.image, self.rect)

        