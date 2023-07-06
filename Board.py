import pygame
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT, BLACK_SQUARE, white_locations, \
    black_locations, WIN, WIDTH, HEIGHT, info_rect_height, info_rect_width

piece_list = [Pawn, Rook, Knight, Bishop, Queen, King]



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
            pygame.draw.line(win, 'black', (0, SQUARE_HEIGHT * i), (880, SQUARE_HEIGHT * i), 2)
            pygame.draw.line(win, 'black', (SQUARE_WIDTH * i, 0), (SQUARE_WIDTH * i, 650), 2)

    def create_board(self, win, white_pieces, black_pieces):
        self.draw_cubes(win)

        pygame.draw.rect(WIN, (89, 52, 148), [0, 650, WIDTH + info_rect_width, 50], 5)
        pygame.draw.rect(WIN, (89, 52, 148), [777 + 100, 0, 200, HEIGHT + info_rect_height], 3)

        for i, piece in enumerate(white_pieces):
            self.board.append([])

            piece(white_locations[i][0], white_locations[i][1], WHITE).draw(win, WHITE)
            self.board[i].append(piece(white_locations[i][0], white_locations[i][1], WHITE))

        for i, piece in enumerate(black_pieces):
            try:
                piece(black_locations[i][0], black_locations[i][1], BLACK).draw(win, BLACK)
                self.board[i].append(piece(black_locations[i][0], black_locations[i][1], BLACK))
            except IndexError:
                for loc in black_locations:
                    print(f'len blackpieces = {len(black_pieces)}')
                    print(f'loc[{black_locations.index(loc)}]: {loc}')



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


