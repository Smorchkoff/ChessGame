import pygame

pygame.init()

info_rect_width = 200
info_rect_height = 100
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 8, 8
SQUARE_WIDTH = (WIDTH + 80) // ROWS
SQUARE_HEIGHT = (HEIGHT + 50) // COLS

font = pygame.font.Font('Roboto-Light.ttf', 20)
font_text = pygame.sysfont.Font('assets/helvetica_regular.otf', 10)

piece_size = (75, 75)
small_piece_size = (40, 40)

WIN = pygame.display.set_mode((WIDTH + info_rect_width, HEIGHT + info_rect_height))

move_font = pygame.font.Font('Roboto-Light.ttf', 40)

black_texture = pygame.image.load('assets/black_wood.jpg').convert()
black_texture = pygame.transform.scale(black_texture, (SQUARE_WIDTH, SQUARE_HEIGHT))

white_texture = pygame.image.load('assets/white_wood.jpg').convert()
# white_texture = pygame.transform.scale(white_texture, (SQUARE_WIDTH, SQUARE_HEIGHT))

small_black_pawn = pygame.transform.scale(pygame.image.load('assets/Chess2/black_pawn.png').convert_alpha(),
                                          small_piece_size)
small_black_rook = pygame.transform.scale(pygame.image.load('assets/Chess2/black_rook.png').convert_alpha(),
                                          small_piece_size)
small_black_bishop = pygame.transform.scale(pygame.image.load('assets/Chess2/black_bishop.png').convert_alpha(),
                                            small_piece_size)
small_black_knight = pygame.transform.scale(pygame.image.load('assets/Chess2/black_knight.png').convert_alpha(),
                                            small_piece_size)
small_black_queen = pygame.transform.scale(pygame.image.load('assets/Chess2/black_queen.png').convert_alpha(),
                                            small_piece_size)
small_black_king = pygame.transform.scale(pygame.image.load('assets/Chess2/black_king.png').convert_alpha(),
                                          small_piece_size)
small_black_images = [small_black_pawn, small_black_rook, small_black_knight,
                      small_black_bishop, small_black_queen, small_black_king]

small_white_pawn = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_pawn.png').convert_alpha(),
                                          small_piece_size)
small_white_rook = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_rook.png').convert_alpha(),
                                          small_piece_size)
small_white_bishop = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_bishop.png').convert_alpha(),
                                            small_piece_size)
small_white_knight = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_knight.png').convert_alpha(),
                                            small_piece_size)
small_white_queen = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_queen.png').convert_alpha(),
                                           small_piece_size)
small_white_king = pygame.transform.scale(pygame.image.load('assets/Chess2/lightgray_king.png').convert_alpha(),
                                          small_piece_size)
small_white_images = [small_white_pawn, small_white_rook, small_white_knight,
                      small_white_bishop, small_white_queen, small_white_king]

big_font = pygame.font.Font('Roboto-Light.ttf', 36)

status_text = ['Белые: Выберите фигуру для хода!', 'Белые: Выберите ход!',
               'Черные: Выберите фигуру для хода!', 'Чёрные: Выберите ход!']

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

BLACK = 'black'
BLACK_SQUARE = 'darkgray'
WHITE = 'lightgray'
