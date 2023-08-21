import pygame
from pygame_widgets.button import Button

pygame.init()

info_rect_width = 200
info_rect_height = 100
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 8, 8
SQUARE_WIDTH = (WIDTH + 80) // ROWS
SQUARE_HEIGHT = (HEIGHT + 50) // COLS

font = pygame.font.Font('assets/fonts/helvetica_regular.otf', 20)
font_text = pygame.sysfont.Font('assets/fonts/helvetica_regular.otf', 10)
menu_font = pygame.font.Font('assets/fonts/MenuFont.ttf', 15)
medium_menu_font = pygame.font.Font('assets/fonts/MenuFont.ttf', size=40)
big_menu_font = pygame.font.Font('assets/fonts/MenuFont.ttf', 60)

piece_size = (75, 75)
small_piece_size = (40, 40)

WIN = pygame.display.set_mode((WIDTH + info_rect_width, HEIGHT + info_rect_height))

wood_bg = pygame.image.load('assets/images/wood_bg_menu.jpg').convert()
wood_bg = pygame.transform.scale(wood_bg, (WIDTH + info_rect_width, HEIGHT + info_rect_height))
move_font = pygame.font.Font('assets/fonts/helvetica_regular.otf', 40)

black_texture = pygame.image.load('assets/images/black_wood.jpg').convert()
black_texture = pygame.transform.scale(black_texture, (SQUARE_WIDTH, SQUARE_HEIGHT))

white_texture = pygame.image.load('assets/images/white_wood.jpg').convert()
# white_texture = pygame.transform.scale(white_texture, (SQUARE_WIDTH, SQUARE_HEIGHT))

small_black_pawn = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_pawn.png').convert_alpha(),
                                          small_piece_size)
small_black_rook = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_rook.png').convert_alpha(),
                                          small_piece_size)
small_black_bishop = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_bishop.png').convert_alpha(),
                                            small_piece_size)
small_black_knight = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_knight.png').convert_alpha(),
                                            small_piece_size)
small_black_queen = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_queen.png').convert_alpha(),
                                           small_piece_size)
small_black_king = pygame.transform.scale(pygame.image.load('./assets/Chess2/black_king.png').convert_alpha(),
                                          small_piece_size)
small_black_images = [small_black_pawn, small_black_rook, small_black_knight,
                      small_black_bishop, small_black_queen, small_black_king]

small_white_pawn = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_pawn.png').convert_alpha(),
                                          small_piece_size)
small_white_rook = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_rook.png').convert_alpha(),
                                          small_piece_size)
small_white_bishop = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_bishop.png').convert_alpha(),
                                            small_piece_size)
small_white_knight = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_knight.png').convert_alpha(),
                                            small_piece_size)
small_white_queen = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_queen.png').convert_alpha(),
                                           small_piece_size)
small_white_king = pygame.transform.scale(pygame.image.load('./assets/Chess2/lightgray_king.png').convert_alpha(),
                                          small_piece_size)
small_white_images = [small_white_pawn, small_white_rook, small_white_knight,
                      small_white_bishop, small_white_queen, small_white_king]

big_font = pygame.font.Font('assets/fonts/helvetica_regular.otf', 36)

status_text = ['Белые: Выберите фигуру для хода!', 'Белые: Выберите ход!',
               'Черные: Выберите фигуру для хода!', 'Чёрные: Выберите ход!']

# white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
#                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
#
# black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
#                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
#
# locations = [['w♜', 'w♞', 'w♝', 'w♛', 'w♚', 'w♝', 'w♞', 'w♜'],
#              ['w♟', 'w♟', 'w♟', 'w♟', 'w♟', 'w♟', 'w♟', 'w♟'],
#              ['.', '.', '.', '.', '.', '.', '.', '.'],
#              ['.', '.', '.', '.', '.', '.', '.', '.'],
#              ['.', '.', '.', '.', '.', '.', '.', '.'],
#              ['.', '.', '.', '.', '.', '.', '.', '.'],
#              ['b♟', 'b♟', 'b♟', 'b♟', 'b♟', 'b♟', 'b♟', 'b♟'],
#              ['b♜', 'b♞', 'b♝', 'b♛', 'b♚', 'b♝', 'b♞', 'b♜']]

BLACK = 'black'
BLACK_SQUARE = 'darkgray'
WHITE = 'lightgray'

pawn_points = [[0, 0, 0, 0, 0, 0, 0, 0],
               [5, 5, 5, 5, 5, 5, 5, 5],
               [1, 1, 2, 3, 3, 2, 1, 1],
               [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5],
               [0.5, 1, 1, -2, -2, 1, 1, 0.5],
               [0, 0, 0, 0, 0, 0, 0, 0]]
knight_points = [[-5, -4, -3, -3, -3, -3, -4, -5],
                 [-4, -2, 0, 0, 0, 0, -2, -4],
                 [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
                 [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
                 [-3, 0, 1.5, 2, 2, 1.5, 0, -3],
                 [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
                 [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
                 [-5, -4, -3, -3, -3, -3, -4, -5]]
bishop_points = [[-2, -1, -1, -1, -1, -1, -1, -2],
                 [-1, 0, 0, 0, 0, 0, 0, -1],
                 [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
                 [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
                 [-1, 0, 1, 1, 1, 1, 0, -1],
                 [-1, 1, 1, 1, 1, 1, 1, -1],
                 [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
                 [-2, -1, -1, -1, -1, -1, -1, -2]]
rook_points = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0.5, 1, 1, 1, 1, 1, 1, 0.5],
               [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
               [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
               [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
               [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
               [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
               [0, 0, 0, 0.5, 0.5, 0, 0, 0]]
queen_points = [[-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                [-1, 0, 0, 0, 0, 0, 0, -1],
                [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-1, 0, 0.5, 0, 0, 0, 0, -1],
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2]]
king_points = [[-3, -4, -4, -5, -5, -4, -4, -3],
               [-3, -4, -4, -5, -5, -4, -4, -3],
               [-3, -4, -4, -5, -5, -4, -4, -3],
               [-3, -4, -4, -5, -5, -4, -4, -3],
               [-2, -3, -3, -4, -4, -3, -3, -2],
               [-1, -2, -2, -2, -2, -2, -2, -1],
               [2, 2, 0, 0, 0, 0, 2, 2],
               [2, 3, 1, 0, 0, 1, 3, 2]]


def print_board(board):
    print('=' * 100)
    for index, row in enumerate(board):
        print(f'{index}{row}')
    print('=' * 100)


def set_button(surface, txt, x, y, width, func):
    return Button(
        surface,
        x,
        y,
        width,
        50,
        text=txt,
        font=menu_font,
        textColour='White',
        radius=10,
        inactiveColour=(135, 132, 132),
        hoverColour=(135, 132, 132),
        pressedColour=(135, 132, 132),
        hoverBorderColour='YELLOW',
        inactiveBorderColour=(135, 132, 132),
        borderThickness=3,
        shadowColour='lightgray',
        shadowDistance=5,
        onClick=lambda: func()
    )

text_colour = 'White'
main_colour = (135,132,132)
border_colour = 'Yellow'
shadow_colour = 'lightgray'


