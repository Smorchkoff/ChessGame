import pygame
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT, BLACK_SQUARE, white_locations, \
    black_locations, WIN

piece_list = [Pawn, Rook, Knight, Bishop, Queen, King]
white_pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook,
                Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]
black_pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook,
                Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16

    @staticmethod
    def draw_cubes(win):
        win.fill(BLACK_SQUARE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
        for i in range(9):
            pygame.draw.line(win, 'black', (0, SQUARE_HEIGHT * i), (800, SQUARE_HEIGHT * i), 2)
            pygame.draw.line(win, 'black', (SQUARE_WIDTH * i, 0), (SQUARE_WIDTH * i, 600), 2)

    def create_board(self, win):
        self.draw_cubes(win)
        for i, piece in enumerate(white_pieces):
            self.board.append([])

            piece(white_locations[i][0], white_locations[i][1], WHITE).draw(win, WHITE)
            self.board[i].append(piece(white_locations[i][0], white_locations[i][1], WHITE))

        for i, piece in enumerate(black_pieces):
            piece(black_locations[i][0], black_locations[i][1], BLACK).draw(win, BLACK)
            self.board[i].append(piece(black_locations[i][0], black_locations[i][1], BLACK))

        # global color, piece
        # for row in range(ROWS):
        #     self.board.append([])
        #     for col in range(COLS):
        #         if row < 2:
        #             color = WHITE
        #         elif row > 5:
        #             color = BLACK
        #         else:
        #             self.board[row].append(0)
        #
        #         if row in (0, 7):
        #             try:
        #                 piece = Piece_dict[col]
        #             except KeyError as E:
        #                 print('ОШЕБКА')
        #             self.board[row].append(piece(row, col, color))
        #         elif row in (1, 6):
        #             self.board[row].append(Pawn(row, col ,color))
        #
        #     else:
        #         self.board[row].append(0)


