import pygame
from pieces import Piece
from constants import  BLACK, WHITE, piece_size


class Rook(Piece):
    def draw(self, win, col):
        chess_icon = pygame.image.load(f'./assets/Chess2/{col}_rook.png').convert_alpha()
        chess_icon = pygame.transform.smoothscale(chess_icon, piece_size)
        win.blit(chess_icon, (self.x, self.y))

    def move(self, pos, brd):
        if self.color == WHITE:
            enemies_list = brd.black_locations
            friends_list = brd.white_locations
        else:
            enemies_list = brd.white_locations
            friends_list = brd.black_locations

        for i in range(4):
            path = True
            chain = 1
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = 1
                y = 0
            elif i == 3:
                x = -1
                y = 0
            while path:
                if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                        0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                    self.moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                    if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return self.moves_list
