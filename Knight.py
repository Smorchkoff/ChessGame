import pygame
from pieces import Piece
from constants import WHITE, black_locations, white_locations,piece_size


class Knight(Piece):
    def draw(self, win, col):
        chess_icon = pygame.image.load(f'images/Chess2/{col}_knight.png').convert_alpha()
        chess_icon = pygame.transform.smoothscale(chess_icon, piece_size)
        win.blit(chess_icon, (self.x, self.y), )

    def move(self, pos):
        moves_list = []
        if self.color == WHITE:
            enemies_list = black_locations
            friends_list = white_locations
        else:
            enemies_list = white_locations
            friends_list = black_locations

        moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(len(moves)):
            move = (pos[0] + moves[i][0], pos[1] + moves[i][1])
            if move not in friends_list and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                moves_list.append(move)
        return moves_list
