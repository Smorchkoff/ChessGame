import pygame
from pygame_widgets.button import Button
import pygame_widgets
from constants import WIN, wood_bg, big_menu_font, medium_menu_font, menu_font, text_colour, main_colour, \
    border_colour, shadow_colour, WHITE, BLACK, SQUARE_WIDTH, SQUARE_HEIGHT, print_board
from colorama import Fore, Style
from AI import alpha_beta_minimax
from Board import Board, piece_dict
from King import King


# TODO Создайте игровую доску с помощью модуля Pygame. ##DONE##
#
# TODO Реализуйте логику ходов для каждой фигуры. ##DONE##
#
# TODO Разработайте алгоритм для ИИ, который будет принимать решения о ходах.
#      Вы можете использовать различные алгоритмы, такие как минимакс или алгоритм альфа-бета отсечения,
#      чтобы оценивать возможные ходы и выбирать наилучший.
#
# TODO Реализуйте функцию, которая будет проверять, является ли текущая позиция шахматной доски матом, патом или ничьей.
#
# TODO Наконец, создайте игровой цикл, который будет обрабатывать ходы игрока и ИИ,
#      обновлять доску и отображать изменения на экране.

pygame.init()

pygame.display.set_caption('♛Chess♛')
brd = Board()
black = False
white = True


def check_valid_moves(sel, white_mvs, black_mvs):
    if brd.turn_step < 2:
        moves_list = white_mvs
    else:
        moves_list = black_mvs
    valid_options = moves_list[sel]
    return valid_options


def check_all_moves(loc):
    all_moves_list = []
    for r, row in enumerate(loc):
        moves_list = []
        for col, piece in enumerate(row):
            pos = (col, r)
            if piece[0] == 'w':
                color = WHITE
            elif piece[0] == 'b':
                color = BLACK
            else:
                moves_list.append('.')
                continue
            moves_list.append(piece_dict[piece[1:]](col, r, color).move(pos, brd))
        all_moves_list.append(moves_list)
    return all_moves_list


def check_moves(pieces, loc, color):
    all_moves_list = []

    for i in range((len(pieces))):
        pos = loc[i]
        piece = pieces[i]
        moves = piece(pos[0], pos[1], color).move(pos, brd)
        # print(f'{Fore.BLUE}{color[0]}|{piece.__name__}[{pos}] -> {moves_list}{Fore.RESET}')
        # print(f'white - {white_locations}')
        # print(f'black - {black_locations}')
        all_moves_list.append(moves)
    return all_moves_list


# all_moves = check_all_moves(locations)
# all_moves2 = white_moves + black_moves

pygame.init()
play_btn = Button(
    WIN,
    400,
    200,
    300,
    50,
    text='Выбрать режим',
    font=menu_font,
    textColour=text_colour,
    radius=10,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    shadowColour=shadow_colour,
    shadowDistance=5,
    onClick=lambda: choose_menu()
)
quit_btn = Button(
    WIN,
    400,
    300,
    200,
    50,
    text='Выйти',
    font=menu_font,
    textColour=text_colour,
    radius=10,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    shadowColour=shadow_colour,
    shadowDistance=5,
    onClick=lambda: pygame.quit()
)
back_btn = Button(
    WIN,
    400,
    600,
    200,
    50,
    text='Назад',
    font=menu_font,
    textColour=text_colour,
    radius=10,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    shadowColour=shadow_colour,
    shadowDistance=5,
    onClick=lambda: main_menu()
)
USERvsAI_btn = Button(
    WIN,
    200,
    400,
    200,
    50,
    text='USERvsAI',
    font=menu_font,
    textColour=text_colour,
    radius=10,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    shadowColour=shadow_colour,
    shadowDistance=5,
    onClick=lambda: set_userVSai_mode(brd)
)
USERvsUSER_btn = Button(
    WIN,
    600,
    400,
    200,
    50,
    text='USERvsUSER',
    font=menu_font,
    textColour=text_colour,
    radius=10,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    shadowColour=shadow_colour,
    shadowDistance=5,
    onClick=lambda: set_userVSuser_mode(brd)
)
forfeit_btn = Button(
    WIN,
    876,
    650,
    125,
    50,
    text='Сдаться',
    font=menu_font,
    textColour=text_colour,
    radius=2,
    inactiveColour=main_colour,
    hoverColour=main_colour,
    pressedColour=main_colour,
    hoverBorderColour=border_colour,
    inactiveBorderColour=main_colour,
    borderThickness=3,
    # shadowColour=shadow_colour,
    # shadowDistance=5,
    onClick=lambda: draw_game_over(brd)
)
# play_btn = set_button(WIN, 'Choose the mode', 400 , 200, 300, choose_menu)
# quit_btn = set_button(WIN, 'Quit', 400, 300, 200, pygame.quit)
# tst_btn = set_button(WIN, 'TEST', 100, 300, 200, pygame.quit)


play_btn.hide()
quit_btn.hide()
back_btn.hide()
USERvsAI_btn.hide()
USERvsUSER_btn.hide()
forfeit_btn.hide()


def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        back_btn.hide()
        play_btn.show()
        quit_btn.show()
        # WIN.fill((0,50,100))
        WIN.blit(wood_bg, (0, 0))

        # alpha_surf = pygame.Surface((200, 200), pygame.SRCALPHA)
        # alpha_surf.fill((255, 255, 100, 128))

        WIN.blit(big_menu_font.render('CHESS GAME', True, 'White'), (300, 30))
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()


def choose_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        play_btn.hide()
        quit_btn.hide()
        back_btn.show()
        USERvsAI_btn.show()
        USERvsUSER_btn.show()
        WIN.blit(wood_bg, (0, 0))
        WIN.blit(medium_menu_font.render('Выбери режим!', True, 'White'), (300, 30))
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
    pygame.quit()


def set_userVSuser_mode(board):
    # global valid_moves, black_moves, white_moves, counter, white_old_pos, white_old_col, \
    #     white_old_row, black_old_row, black_old_col, black_old_pos, all_moves, click_coords, locations
    clock = pygame.time.Clock()
    counter = 0
    white_old_pos, white_old_col, white_old_row, black_old_row, black_old_col, black_old_pos = 0, 0, 0, 0, 0, 0,
    captured_pieces_white = []
    captured_pieces_black = []
    running = True
    back_btn.hide()
    forfeit_btn.show()
    selection = 100
    board.set_default_values()
    black_locations = board.get_black_locations()
    white_locations = board.get_white_locations()
    white_pieces = board.get_white_pieces()
    black_pieces = board.get_black_pieces()
    white_moves = check_moves(white_pieces, white_locations, WHITE)
    black_moves = check_moves(black_pieces, black_locations, BLACK)
    locations = board.get_board()
    valid_moves = []
    while running:
        USERvsUSER_btn.hide()
        USERvsAI_btn.hide()
        clock.tick(30)

        if counter < 30:
            counter += 3
        else:
            counter = 0

        board.create_board()
        board.draw_selected_piece()
        board.draw_check(black_moves, white_moves, counter)
        board.draw_captured_pieces(captured_pieces_white, captured_pieces_black)
        if selection != 100:
            valid_moves = check_valid_moves(selection, white_moves, black_moves)
            board.draw_valid_moves(valid_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0] // SQUARE_WIDTH
                y_coord = event.pos[1] // SQUARE_HEIGHT
                click_coords = (x_coord, y_coord)
                print(f'{Fore.YELLOW}{Style.BRIGHT}click_coords: {click_coords}{Fore.RESET}{Style.RESET_ALL}')
                if board.turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        board.winner = "Чёрный"
                    if click_coords in white_locations:
                        selection = board.white_locations.index(click_coords)
                        board.selected_piece = (click_coords[1], click_coords[0])
                        white_old_pos = locations[click_coords[1]][click_coords[0]]
                        white_old_col = click_coords[0]
                        white_old_row = click_coords[1]
                        if board.turn_step == 0:
                            board.turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        board.white_locations[selection] = click_coords
                        locations[click_coords[1]][click_coords[0]] = white_old_pos
                        locations[white_old_row][white_old_col] = '.'
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            # board.black_left -= 1
                            if black_pieces[black_piece] == King:
                                board.winner = 'Белый'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        print_board(board.board)
                        black_moves = check_moves(black_pieces, black_locations, BLACK)
                        white_moves = check_moves(white_pieces, white_locations, WHITE)
                        board.turn_step = 2
                        selection = 100
                        valid_moves = []
                if board.turn_step > 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        board.winner = 'Белый'
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        black_old_pos = locations[click_coords[1]][click_coords[0]]
                        black_old_col = click_coords[0]
                        black_old_row = click_coords[1]
                        if board.turn_step == 2:
                            board.turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        locations[click_coords[1]][click_coords[0]] = black_old_pos
                        locations[black_old_row][black_old_col] = '.'
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == King:
                                board.winner = 'Чёрный'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_moves = check_moves(black_pieces, black_locations, BLACK)
                        white_moves = check_moves(white_pieces, white_locations, WHITE)
                        board.turn_step = 0
                        selection = 100
                        valid_moves = []

        if board.winner != '':
            draw_game_over(brd)
        forfeit_btn.show()
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
    pygame.quit()


def set_userVSai_mode(board):
    back_btn.hide()
    USERvsUSER_btn.hide()
    USERvsAI_btn.hide()
    clock = pygame.time.Clock()
    click_coords = (100, 100)
    counter = 0
    white_old_pos, white_old_col, white_old_row, black_old_row, black_old_col, black_old_pos = 0, 0, 0, 0, 0, 0,
    captured_pieces_white = []
    captured_pieces_black = []
    running = True
    back_btn.hide()
    forfeit_btn.show()
    selection = 100
    board.set_default_values()
    black_locations = board.get_black_locations()
    white_locations = board.get_white_locations()
    white_pieces = board.get_white_pieces()
    black_pieces = board.get_black_pieces()
    white_moves = check_moves(white_pieces, white_locations, WHITE)
    black_moves = check_moves(black_pieces, black_locations, BLACK)
    locations = board.get_board()
    valid_moves = []
    while running:
        # clock.tick(60)

        if counter < 30:
            counter += 3
        else:
            counter = 0

        board.create_board()
        board.draw_selected_piece()
        board.draw_check(black_moves, white_moves, counter)
        board.draw_captured_pieces(captured_pieces_white, captured_pieces_black)

        if selection != 100:
            valid_moves = check_valid_moves(selection, white_moves, black_moves)
            board.draw_valid_moves(valid_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0] // SQUARE_WIDTH
                y_coord = event.pos[1] // SQUARE_HEIGHT
                click_coords = (x_coord, y_coord)
                print(f'{Fore.YELLOW}{Style.BRIGHT}click_coords: {click_coords}{Fore.RESET}{Style.RESET_ALL}')
                if board.turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        board.winner = "Чёрный"
                    if click_coords in white_locations:
                        selection = board.white_locations.index(click_coords)
                        print(valid_moves)
                        board.selected_piece = (click_coords[1], click_coords[0])
                        white_old_pos = locations[click_coords[1]][click_coords[0]]
                        white_old_col = click_coords[0]
                        white_old_row = click_coords[1]
                        if board.turn_step == 0:
                            board.turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        board.white_locations[selection] = click_coords
                        locations[click_coords[1]][click_coords[0]] = white_old_pos
                        locations[white_old_row][white_old_col] = '.'
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            # board.black_left -= 1
                            if black_pieces[black_piece] == King:
                                board.winner = 'Белый'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        board.create_board()
                        pygame.display.flip()
                        black_moves = check_moves(black_pieces, black_locations, BLACK)
                        white_moves = check_moves(white_pieces, white_locations, WHITE)
                        board.turn_step = 2
                        selection = 100
                        valid_moves = []
                if board.turn_step > 1:
                    board.create_board()
                    pygame.display.flip()
                    alpha_beta_minimax(locations, 3, float('-inf'), float('+inf'),
                                       black, board, captured_pieces_black)
                    black_moves = check_moves(black_pieces, black_locations, BLACK)
                    white_moves = check_moves(white_pieces, white_locations, WHITE)
                    board.turn_step = 0
                    selection = 100
                    valid_moves = []

        if board.winner != '':
            draw_game_over(board)
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
    pygame.quit()


def draw_game_over(board):
    running = True
    while running:
        forfeit_btn.hide()
        back_btn.show()
        WIN.fill((50, 0, 100))
        WIN.blit(menu_font.render(f'Победитель {board.winner}!', True, 'White'), (300, 200))
        WIN.blit(menu_font.render(f'Для перезапуста нажмите на кнопку.', True, 'White'), (300, 250))
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
