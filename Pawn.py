import pygame
from pieces import Piece
from constants import BLACK, WHITE, piece_size


class Pawn(Piece):

    def draw(self, win, col):
        pygame.init()
        chess_icon = pygame.image.load(f'./assets/Chess2/{col}_pawn.png').convert_alpha()
        chess_icon = pygame.transform.smoothscale(chess_icon, piece_size)
        # for i in range(10):

        win.blit(chess_icon, (self.x, self.y))

    def move(self, pos, brd):

        if self.color == WHITE:
            if (pos[0], pos[1] + 1) not in brd.white_locations and \
                    (pos[0], pos[1] + 1) not in brd.black_locations and pos[1] < 7:
                self.moves_list.append((pos[0], pos[1] + 1))
            if (pos[0], pos[1] + 2) not in brd.white_locations and \
                    (pos[0], pos[1] + 2) not in brd.black_locations and pos[1] == 1:
                self.moves_list.append((pos[0], pos[1] + 2))
            if (pos[0] + 1, pos[1] + 1) in brd.black_locations:
                self.moves_list.append((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] + 1) in brd.black_locations:
                self.moves_list.append((pos[0] - 1, pos[1] + 1))
        else:
            if (pos[0], pos[1] - 1) not in brd.white_locations and \
                    (pos[0], pos[1] - 1) not in brd.black_locations and pos[0] > 0:
                self. moves_list.append((pos[0], pos[1] - 1))
            if (pos[0], pos[1] - 2) not in brd.white_locations and \
                    (pos[0], pos[1] - 2) not in brd.black_locations and pos[1] == 6:
                self.moves_list.append((pos[0], pos[1] - 2))
            if (pos[0] + 1, pos[1] - 1) in brd.white_locations:
                self.moves_list.append((pos[0] + 1, pos[1] - 1))
            if (pos[0] - 1, pos[1] - 1) in brd.white_locations:
                self.moves_list.append((pos[0] - 1, pos[1] - 1))
        return self.moves_list


