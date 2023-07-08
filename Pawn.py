import pygame
from pieces import Piece
from constants import white_locations, black_locations, BLACK, WHITE, piece_size


class Pawn(Piece):

    def draw(self, win, col):
        pygame.init()
        chess_icon = pygame.image.load(f'assets/Chess2/{col}_pawn.png').convert_alpha()
        chess_icon = pygame.transform.smoothscale(chess_icon, piece_size)
        # for i in range(10):

        win.blit(chess_icon, (self.x, self.y))

    def move(self, pos):
        moves_list = []
        if self.color == WHITE:
            if (pos[0], pos[1] + 1) not in white_locations and \
                    (pos[0], pos[1] + 1) not in black_locations and pos[1] < 7:
                moves_list.append((pos[0], pos[1] + 1))
            if (pos[0], pos[1] + 2) not in white_locations and \
                    (pos[0], pos[1] + 2) not in black_locations and pos[1] == 1:
                moves_list.append((pos[0], pos[1] + 2))
            if (pos[0] + 1, pos[1] + 1) in black_locations:
                moves_list.append((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] + 1) in black_locations:
                moves_list.append((pos[0] - 1, pos[1] + 1))
        else:
            if (pos[0], pos[1] - 1) not in white_locations and \
                    (pos[0], pos[1] - 1) not in black_locations and pos[0] > 0:
                moves_list.append((pos[0], pos[1] - 1))
            if (pos[0], pos[1] - 2) not in white_locations and \
                    (pos[0], pos[1] - 2) not in black_locations and pos[1] == 6:
                moves_list.append((pos[0], pos[1] - 2))
            if (pos[0] + 1, pos[1] - 1) in white_locations:
                moves_list.append((pos[0] + 1, pos[1] - 1))
            if (pos[0] - 1, pos[1] - 1) in white_locations:
                moves_list.append((pos[0] - 1, pos[0] - 1))
        return moves_list
