import pygame
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT, BLACK_SQUARE

Piece_dict = {
    0: Rook,
    7: Rook,
    1: Knight,
    6: Knight,
    2: Bishop,
    5: Bishop,
    3: King,
    4: Queen
}


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16
        self.create_board()

    def draw_cubes(self, win):
        win.fill(BLACK_SQUARE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
        for i in range(9):
            pygame.draw.line(win, 'black', (0, SQUARE_HEIGHT * i), (800, SQUARE_HEIGHT * i), 2)
            pygame.draw.line(win, 'black', (SQUARE_WIDTH * i, 0), (SQUARE_WIDTH * i, 600), 2)


    def create_board(self):
        global color, piece
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 2:
                    color = WHITE
                elif row > 5:
                    color = BLACK
                else:
                    self.board[row].append(0)

                if row in (0, 7):
                    try:
                        piece = Piece_dict[col]
                    except KeyError as E:
                        print('ОШЕБКА')
                    self.board[row].append(piece(row, col, color))
                elif row in (1, 6):
                    self.board[row].append(Pawn(row, col ,color))
                #     if col in (0, 7):
                #         self.board[row].append(Rook(row, col, color))
                #
                #     self.board[row].append(Knight(row, col, color))
                #
                #     self.board[row].append(Bishop(row, col, color))
                #
                #     self.board[row].append(King(row, col, color))
                #
                #     self.board[row].append(Queen(row, col, color))
                # elif row == 2 or row == 6:
                #     self.board[row].append(Pawn(row, col, color))
            else:
                self.board[row].append(0)

    def draw(self, win):
        self.draw_cubes(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)



