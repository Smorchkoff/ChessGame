import pygame

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_WIDTH * self.col + SQUARE_WIDTH // 2
        self.y = SQUARE_HEIGHT * self.row + SQUARE_HEIGHT // 2

    def draw(self, win):
        chess_icon = pygame.image.load(f'images/Chess/{self.color}_king.png').convert_alpha()
        win.blit(chess_icon, (self.x - 14, self.y - 20), )

    def __repr__(self):
        return str(self.color, self.col, self.row)
