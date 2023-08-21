import pygame
from pieces import Piece
from constants import WHITE, piece_size


class King(Piece):
    def draw(self, win, col):
        chess_icon = pygame.image.load(f'./assets/Chess2/{col}_king.png').convert_alpha()
        chess_icon = pygame.transform.smoothscale(chess_icon, piece_size)
        win.blit(chess_icon, (self.x, self.y ), )

    def move(self, pos, brd):
        if self.color == WHITE:
            enemies_list = brd.black_locations
            friends_list = brd.white_locations
        else:
            enemies_list = brd.white_locations
            friends_list = brd.black_locations

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1,1), (1, -1), (-1, -1), (-1, 1)]
        for i in range(len(moves)):
            move = (pos[0] + moves[i][0], pos[1] + moves[i][1])
            if move not in friends_list and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                self.moves_list.append(move)
        return self.moves_list



