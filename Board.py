import logging
from pygame_widgets.button import Button
import pygame
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT, \
    WIN, WIDTH, HEIGHT, info_rect_height, info_rect_width, black_texture, white_texture, font, \
    font_text, status_text, big_font, small_black_images, small_white_images, wood_bg, \
    set_button, menu_font, big_menu_font
from pprint import pprint

piece_list = [Pawn, Rook, Knight, Bishop, Queen, King]

piece_dict = {
    '♚': King,
    '♜': Rook,
    '♝': Bishop,
    '♟': Pawn,
    '♛': Queen,
    '♞': Knight
}
play_btn = None
quit_btn = None


class Board:
    piece_list = piece_list

    def __init__(self):
        self.gamemode = 0
        self.board_pos = []
        self.selected_piece = None
        self.board = []
        self.set_normal_board()
        self.winner = ''
        self.turn_step = 0
        self.white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

        self.black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        self.white_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook,
                             Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]
        self.black_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook,
                             Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]

    def set_default_values(self):
        self.board_pos = []
        self.selected_piece = None
        self.set_normal_board()
        self.winner = ''
        self.turn_step = 0
        self.white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

        self.black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        self.white_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook,
                             Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]
        self.black_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook,
                             Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]

    def set_normal_board(self):
        self.board = [['.' for i in range(8)] for i in range(8)]
        self.board[0][0] = 'w♜'
        self.board[0][1] = 'w♞'
        self.board[0][2] = 'w♝'
        self.board[0][3] = 'w♛'
        self.board[0][4] = 'w♚'
        self.board[0][5] = 'w♝'
        self.board[0][6] = 'w♞'
        self.board[0][7] = 'w♜'

        for col in range(0, 8):
            self.board[1][col] = 'w♟'
            self.board[6][col] = 'b♟'

        self.board[7][0] = 'b♜'
        self.board[7][1] = 'b♞'
        self.board[7][2] = 'b♝'
        self.board[7][3] = 'b♛'
        self.board[7][4] = 'b♚'
        self.board[7][5] = 'b♝'
        self.board[7][6] = 'b♞'
        self.board[7][7] = 'b♜'

    @staticmethod
    def draw_cubes():
        WIN.blit(white_texture, (0, 0))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                WIN.blit(black_texture, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT))
        for i in range(9):
            pygame.draw.line(WIN, 'black', (0, SQUARE_HEIGHT * i), (880, SQUARE_HEIGHT * i), 2)
            pygame.draw.line(WIN, 'black', (SQUARE_WIDTH * i, 0), (SQUARE_WIDTH * i, 650), 2)

    def create_board(self):
        self.draw_cubes()
        WIN.blit(big_font.render(status_text[self.turn_step], True, 'black'), (190, 650))

        pygame.draw.rect(WIN, 'black', [0, 650, WIDTH + info_rect_width, 50], 3)
        WIN.blit(font_text.render(f'Белых осталось: {len(self.white_pieces)}', True, 'Black'), (890, 100))
        WIN.blit(font_text.render(f'Чёрных осталось: {len(self.black_pieces)}', True, 'Black'), (890, 200))
        pygame.draw.rect(WIN, 'black', [777 + 100, 0, 200, HEIGHT + info_rect_height], 3)

        for r, row in enumerate(self.board):
            for col, piece in enumerate(row):
                if piece != '.':
                    if piece[0] == 'w':
                        wht_pc = piece_dict[piece[1:]](r, col, WHITE)
                        wht_pc.draw(WIN, WHITE)
                    else:
                        blc_pc = piece_dict[piece[1:]](r, col, BLACK)
                        blc_pc.draw(WIN, BLACK)

    def draw_valid_moves(self, moves):
        if self.turn_step < 2:
            color = 'red'
        else:
            color = 'blue'

        for i in range(len(moves)):
            pygame.draw.circle(WIN, color, (moves[i][0] * SQUARE_WIDTH + 55, moves[i][1] * SQUARE_HEIGHT + 40), 5)

    def draw_selected_piece(self):
        color = ''
        for row_i, row in enumerate(self.board):
            for col, piece in enumerate(row):
                if piece != '.':
                    if self.turn_step < 2:
                        color = 'red'
                    elif self.turn_step >= 2:
                        color = 'blue'
                    if (row_i, col) == self.selected_piece:
                        pygame.draw.rect(WIN, color,
                                         [col * SQUARE_WIDTH + 1,
                                          row_i * SQUARE_HEIGHT + 1,
                                          SQUARE_WIDTH, SQUARE_HEIGHT], 3)



    def draw_check(self, black_moves, white_moves, counter):
        if self.turn_step < 2:
            if King in self.white_pieces:
                king_index = self.white_pieces.index(King)
                king_location = self.white_locations[king_index]
                for i in range(len(black_moves)):
                    if king_location in black_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(WIN, 'darkred',
                                             [self.white_locations[king_index][0] * SQUARE_WIDTH,
                                              self.white_locations[king_index][1] * SQUARE_HEIGHT,
                                              SQUARE_WIDTH, SQUARE_HEIGHT], 5)
        else:
            if King in self.black_pieces:
                king_index = self.black_pieces.index(King)
                king_location = self.black_locations[king_index]
                for i in range(len(white_moves)):
                    if king_location in white_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(WIN, 'darkblue', [self.black_locations[king_index][0] * SQUARE_WIDTH,
                                                               self.black_locations[king_index][1] * SQUARE_HEIGHT,
                                                               SQUARE_WIDTH, SQUARE_HEIGHT], 5)

    @staticmethod
    def draw_captured_pieces(captured_white, captured_black):
        for i, piece in enumerate(captured_white):
            piece_index = piece_list.index(piece)
            WIN.blit(small_black_images[piece_index], (880 + i * 5, 5))

        for i, piece in enumerate(captured_black):
            piece_index = piece_list.index(piece)
            WIN.blit(small_white_images[piece_index], (880 + i * 5, 50))

    def get_board(self):
        return self.board

    def print_board(self):
        print('=' * 100)
        for index, row in enumerate(self.board):
            print(f'{index}{row}')
        print('=' * 100)

    def update_board(self, new_board):
        self.board = new_board

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    def get_black_locations(self):
        return self.black_locations

    def get_white_locations(self):
        return self.white_locations

    def set_gamemode(self, gamemode: int):
        self.gamemode = gamemode
