import pygame
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT
from pieces import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16
        self.create_board()


    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT , SQUARE_WIDTH, SQUARE_HEIGHT))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 2:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row > 5:
                    self.board[row].append(Piece(row, col, BLACK))
                else:
                    self.board[row].append(0)
            else:
                self.board[row].append(0)
    def draw(self, win):
        self.draw_cubes(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

