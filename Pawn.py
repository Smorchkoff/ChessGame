import pygame
from pieces import Piece
from constants import white_locations, black_locations, BLACK, WHITE


class Pawn(Piece):
    def draw(self, win, col):
        chess_icon = pygame.image.load(f'images/Chess/{col}_pawn.png').convert_alpha()
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
            if (pos[0] - 1, pos[1] -1) in white_locations:
                moves_list.append((pos[0] - 1, pos[0] - 1))
        return moves_list

