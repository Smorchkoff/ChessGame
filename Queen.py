import pygame
from pieces import Piece
from constants import WHITE, black_locations, white_locations


class Queen(Piece):
    def draw(self, win, col):
        chess_icon = pygame.image.load(f'images/Chess/{col}_queen.png').convert_alpha()
        win.blit(chess_icon, (self.x, self.y ), )

    def move(self, pos):
        global x, y
        moves_list = []

        if self.color == WHITE:
            enemies_list = black_locations
            friends_list = white_locations
        else:
            enemies_list = white_locations
            friends_list = black_locations

        for i in range(8):  # up-right, up-left, down-right, down-left, right, left, down, up
            path = True
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            elif i == 3:
                x = -1
                y = 1
            elif i == 4:
                x = 1
                y = 0
            elif i == 5:
                x = -1
                y = 0
            elif i == 6:
                x = 0
                y = 1
            elif i == 7:
                x = 0
                y = -1

            while path:
                if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                        0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                    moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                    if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list


