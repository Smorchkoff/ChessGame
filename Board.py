import pygame
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from constants import BLACK, WHITE, ROWS, COLS, SQUARE_WIDTH, SQUARE_HEIGHT, white_locations, \
    black_locations, WIN, WIDTH, HEIGHT, info_rect_height, info_rect_width, black_texture, white_texture, font, \
    font_text, status_text, big_font, small_black_images, small_white_images

piece_list = [Pawn, Rook, Knight, Bishop, Queen, King]


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16

    @staticmethod
    def draw_cubes(win):
        win.blit(white_texture, (0, 0))
        # win.fill(BLACK_SQUARE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                # pygame.draw.rect(win, WHITE, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
                win.blit(black_texture, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT))
        for i in range(9):
            pygame.draw.line(win, 'black', (0, SQUARE_HEIGHT * i), (880, SQUARE_HEIGHT * i), 2)
            pygame.draw.line(win, 'black', (SQUARE_WIDTH * i, 0), (SQUARE_WIDTH * i, 650), 2)

    def create_board(self, win, white_pieces, black_pieces, turn_step):
        self.draw_cubes(win)
        win.blit(big_font.render(status_text[turn_step], True, 'black'), (190, 650))

        pygame.draw.rect(WIN, 'black', [0, 650, WIDTH + info_rect_width, 50], 3)
        win.blit(font_text.render(f'Белых осталось: {len(white_pieces)}', True, 'Black'), (890, 100))
        win.blit(font_text.render(f'Чёрных осталось: {len(black_pieces)}', True, 'Black'), (890, 200))
        pygame.draw.rect(WIN, 'black', [777 + 100, 0, 200, HEIGHT + info_rect_height], 3)

        for i, piece in enumerate(white_pieces):
            self.board.append([])

            piece(white_locations[i][0], white_locations[i][1], WHITE).draw(win, WHITE)
            self.board[i].append(piece(white_locations[i][0], white_locations[i][1], WHITE))

        for i, piece in enumerate(black_pieces):
            piece(black_locations[i][0], black_locations[i][1], BLACK).draw(win, BLACK)
            self.board[i].append(piece(black_locations[i][0], black_locations[i][1], BLACK))

    @staticmethod
    def draw_game_over(win, winner):
        pygame.draw.rect(win, 'black', (200, 200, 400, 100))
        win.blit(font.render(f'{winner} победил!', True, 'white'), (210, 210))
        win.blit(font.render(f'Нажмите (TEST), чтобы перезапустить игру!', True, 'white'), (210, 250))

    @staticmethod
    def draw_valid_moves(win, moves, turn_step):
        if turn_step < 2:
            color = 'red'
        else:
            color = 'blue'

        for i in range(len(moves)):
            pygame.draw.circle(WIN, color, (moves[i][0] * SQUARE_WIDTH + 55, moves[i][1] * SQUARE_HEIGHT + 40), 5)

    @staticmethod
    def draw_selected_piece(win, selection, white_pieces, black_pieces, turn_step):
        for i in range(len(white_pieces)):
            if turn_step < 2:
                if selection == i:
                    pygame.draw.rect(win, 'red',
                                     [white_locations[i][0] * SQUARE_WIDTH + 1,
                                      white_locations[i][1] * SQUARE_HEIGHT + 1,
                                      SQUARE_WIDTH, SQUARE_HEIGHT], 3)
        for i in range(len(black_pieces)):
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(win, 'blue',
                                     [black_locations[i][0] * SQUARE_WIDTH + 1,
                                      black_locations[i][1] * SQUARE_HEIGHT + 1,
                                      SQUARE_WIDTH, SQUARE_HEIGHT], 3)

    @staticmethod
    def draw_check(WIN, turn_step, white_pieces, black_pieces, black_moves, white_moves, counter):
        if turn_step < 2:
            if King in white_pieces:
                king_index = white_pieces.index(King)
                king_location = white_locations[king_index]
                for i in range(len(black_moves)):
                    if king_location in black_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(WIN, 'darkred',
                                             [white_locations[king_index][0] * SQUARE_WIDTH,
                                              white_locations[king_index][1] * SQUARE_HEIGHT,
                                              SQUARE_WIDTH, SQUARE_HEIGHT], 5)
        else:
            if King in black_pieces:
                king_index = black_pieces.index(King)
                king_location = black_locations[king_index]
                for i in range(len(white_moves)):
                    if king_location in white_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(WIN, 'darkblue', [black_locations[king_index][0] * SQUARE_WIDTH,
                                                               black_locations[king_index][1] * SQUARE_HEIGHT,
                                                               SQUARE_WIDTH, SQUARE_HEIGHT], 5)

    @staticmethod
    def draw_captured_pieces(win, captured_white, captured_black):
        for i, piece in enumerate(captured_white):
            piece_index = piece_list.index(piece)
            win.blit(small_black_images[piece_index], (880 + i * 5, 5))

        for i, piece in enumerate(captured_black):
            piece_index = piece_list.index(piece)
            win.blit(small_white_images[piece_index], (880 + i * 5, 50))
