import pygame

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.moves_list = []
        self.x = 0
        self.y = 0
        self.old_pos = self.calc_pos()

    def calc_pos(self):
        self.x = (self.col * SQUARE_WIDTH + SQUARE_WIDTH // 2) - 37
        self.y = (self.row * SQUARE_HEIGHT + SQUARE_HEIGHT // 2) - 40
        old_pos = (self.x, self.y)
        return old_pos

    def draw(self, win, col):
        chess_icon = pygame.image.load(f'./assets/Chess2/{col}_king.png').convert_alpha()
        win.blit(chess_icon, (self.x - 14, self.y - 20), )

    def get_loc(self):
        return self.row, self.col

    def get_moves(self):
        return self.moves_list

    def __repr__(self):
        return str(f'{self.__class__},{self.color},{self.row}, {self.col} ')
