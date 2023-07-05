import pygame

from constants import WIDTH, HEIGHT, black_locations, white_locations, BLACK, WHITE
from Board import Board
from King import King
from Knight import Knight
from Bishop import Bishop
from Pawn import Pawn
from Rook import Rook
from Queen import Queen

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('♛Chess♛')

white_pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook,
                Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]
black_pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook,
                Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]



FPS = 30

turn_step = 0
valid_moves = []
selection = 100



def check_valid_moves():
    if turn_step < 2:
        moves_list = white_moves
    else:
        moves_list = black_moves
    valid_options = moves_list[selection]
    return valid_options

def check_moves(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        pos = locations[i]
        piece = pieces[i]
        if piece == Pawn:
            moves_list = Pawn(pos[1], pos[0], turn).move(pos)
        elif piece == Rook:
            moves_list = Rook(pos[1], pos[0], turn).move(pos)
        elif piece == Knight:
            moves_list = Knight(pos[1], pos[0], turn).move(pos)
        elif piece == Bishop:
            moves_list = Bishop(pos[1], pos[0], turn).move(pos)
        elif piece == Queen:
            moves_list = Queen(pos[1], pos[0], turn).move(pos)
        elif piece == King:
            moves_list = King(pos[1], pos[0], turn).move(pos)
        all_moves_list.append(moves_list)
    return all_moves_list

def draw_valid_moves(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'

    for i in range(len(moves)):
        pygame.draw.circle(WIN, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

white_moves = check_moves(white_pieces, white_locations, WHITE)
black_moves = check_moves(black_pieces, black_locations, BLACK)

captured_pieces_white = []
captured_pieces_black = []

def main():
    global turn_step, selection, valid_moves
    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:
        clock.tick(FPS)

        board.draw(WIN)
        pygame.display.update()

        if selection != 100:
            valid_moves = check_valid_moves()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'black'
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_piece[black_piece])
                            if black_pieces[black_piece] == King:
                                winner == 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)


    pygame.quit()


main()
