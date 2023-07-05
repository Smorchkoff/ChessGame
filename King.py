import pygame
from pieces import Piece
from constants import WHITE, black_locations, white_locations


class King(Piece):
    def draw(self, win):
        chess_icon = pygame.image.load(f'images/Chess/{self.color}_king.png').convert_alpha()
        win.blit(chess_icon, (self.x - 14, self.y - 20), )

    def move(self, pos):
        moves_list = []
        if self.color == WHITE:
            enemies_list = black_locations
            friends_list = white_locations
        else:
            enemies_list = white_locations
            friends_list = black_locations

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1,1), (1, -1), (-1, -1), (-1, 1)]
        for i in range(len(moves)):
            move = (pos[0] + moves[i][0], pos[1] + moves[i][1])
            if move not in friends_list and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                moves_list.append(move)
        return moves_list

