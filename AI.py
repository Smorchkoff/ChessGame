import copy
import random
from numpy import flipud

from King import King
from Board import piece_dict
from constants import WHITE, BLACK, rook_points, knight_points, bishop_points, queen_points, \
    king_points, pawn_points
import time
from colorama import Fore, Style


# Simple move, lvl1 #
def simple_game(board, pieces, location, moves, enemy_loc, enemy_pieces, captured_pieces):
    while True:
        # piece = random.choice(pieces)
        try:
            loc = random.choice(location)
            selection = location.index(loc)
            piece = pieces[selection]
            move = random.choice(moves[selection])
            if move in enemy_loc:
                enemy_piece = enemy_loc.index(move)
                captured_pieces.append(enemy_pieces[enemy_piece])
                enemy_pieces.pop(enemy_piece)
                enemy_loc.pop(enemy_piece)
        except IndexError:
            continue

        print(f'piece - {piece}[{selection}]\nlocation - {loc}\nmove - {move}')
        board[move[1]][move[0]] = board[loc[1]][loc[0]]
        board[loc[1]][loc[0]] = '.'
        location[selection] = move
        return board


# Set AI move with Minimax(depth 1), lvl2 #
def minimax(board, depth, maximizing_player, class_board, captured_pieces=None):
    winner = ''
    start_time = time.time()
    # Second Solution
    true_board = board
    if depth == 0 or winner != '':
        return evaluate_position(board)

    if maximizing_player:
        cords = ()
        max_score = float('-inf')
        best_move = None
        for row_i, row in enumerate(board):
            for col, piece in enumerate(row):
                if piece != '.':
                    for move in find_legal_moves(piece, (col, row_i), class_board):
                        old_value = piece
                        copy_board = copy.deepcopy(true_board)
                        new_board, winner = make_move(copy_board, row_i, col, move)
                        score = minimax(new_board, depth - 1, False, class_board)
                        if score > max_score:
                            max_score = score
                            best_move = move
                            cords = (row_i, col)
                else:
                    continue
        return max_score
    else:
        cords = ()
        min_score = float('+inf')
        # min_score_list = []
        # best_move_list = []
        best_move = None
        for row_i, row in enumerate(board):
            for col, piece in enumerate(row):
                if piece != '.':
                    if piece[0] == 'b':
                        legal_moves = find_legal_moves(piece, (col, row_i), class_board)
                        if not legal_moves:
                            continue
                        for move in legal_moves:
                            copy_board = copy.deepcopy(board)
                            new_board, winner = make_move(copy_board, row_i, col, move)
                            score = minimax(new_board, depth - 1, True, class_board)
                            board = true_board
                            if score < min_score:
                                min_score = score
                                best_move = move
                                cords = (row_i, col)
                                # min_score_list.append(min_score)
                                # best_move_list.append(move)
                    else:
                        continue
                else:
                    continue

        # min_score_index = min_score_list.index(min(min_score_list))
        # best_move = best_move_list[min_score_index]
        make_move(board, cords[0], cords[1], best_move, class_board, captured_pieces)
        print(
            f'{Fore.RED}{Style.BRIGHT}Score: {min_score}\nLoc: {cords}\nMove: {(best_move[1], best_move[0])}{Fore.RESET}{Style.RESET_ALL}')
        print(
            f'{Fore.YELLOW}{Style.BRIGHT}Function Minimax(depth = {depth}) was completed {round(time.time() - start_time, 5)} seconds.{Fore.RESET}{Style.RESET_ALL}')
        return min_score


###################################################################

def alpha_beta_minimax(board, depth, alpha, beta, maximizing_player, class_board, captured_pieces=None):
    winner = ''
    start_time = time.time()
    # Second Solution
    true_board = board
    if depth == 0 or winner != '':
        return evaluate_position(board)

    if maximizing_player:
        cords = ()
        max_score = float('-inf')
        best_move = None
        for row_i, row in enumerate(board):
            for col, piece in enumerate(row):
                if piece != '.':
                    for move in find_legal_moves(piece, (col, row_i), class_board):
                        old_value = piece
                        copy_board = copy.deepcopy(true_board)
                        new_board, winner = make_move(copy_board, row_i, col, move)
                        score = alpha_beta_minimax(new_board, depth - 1, alpha, beta, False, class_board)
                        board = true_board
                        alpha = max(alpha, score)
                        if score > max_score:
                            max_score = score
                            best_move = move
                            cords = (row_i, col)
                        if alpha >= beta:
                            break
                else:
                    continue
        return max_score
    else:
        cords = ()
        min_score = float('+inf')
        # min_score_list = []
        # best_move_list = []
        best_move = None
        for row_i, row in enumerate(board):
            for col, piece in enumerate(row):
                if piece != '.':
                    if piece[0] == 'b':
                        legal_moves = find_legal_moves(piece, (col, row_i), class_board)
                        if not legal_moves:
                            continue
                        for move in legal_moves:
                            copy_board = copy.deepcopy(board)
                            new_board, winner = make_move(copy_board, row_i, col, move)
                            score = alpha_beta_minimax(new_board, depth - 1, alpha, beta, True, class_board)
                            board = true_board
                            beta = min(beta, score)
                            if score < min_score:
                                min_score = score
                                best_move = move
                                cords = (row_i, col)
                            if alpha >= beta:
                                break
                                # min_score_list.append(min_score)
                                # best_move_list.append(move)
                    else:
                        continue
                else:
                    continue

        # min_score_index = min_score_list.index(min(min_score_list))
        # best_move = best_move_list[min_score_index]
        make_move(board, cords[0], cords[1], best_move, class_board, captured_pieces)
        print(
            f'{Fore.RED}{Style.BRIGHT}Score: {min_score}\nLoc: {cords}\nMove: {(best_move[1], best_move[0])}{Fore.RESET}{Style.RESET_ALL}')
        print(
            f'{Fore.YELLOW}{Style.BRIGHT}Function Minimax(depth = {depth}) was completed {round(time.time() - start_time, 5)} seconds.{Fore.RESET}{Style.RESET_ALL}')
        return min_score


def evaluate_position(board):
    piece_values = {
        '♚': 20000,  # король
        '♛': 900,  # ферзь
        '♜': 500,  # ладья
        '♝': 330,  # слон
        '♞': 320,  # конь
        '♟': 100,  # пешка
    }

    piece_adv_values = {
        '♚': king_points,  # король
        '♛': queen_points,  # ферзь
        '♜': rook_points,  # ладья
        '♝': bishop_points,  # слон
        '♞': knight_points,  # конь
        '♟': pawn_points,  # пешка
    }

    score = 0

    for row_i, row in enumerate(board):
        for col, piece in enumerate(row):
            if piece != '.':
                if piece[0] == 'w':  # белая фигура
                    score += piece_adv_values[piece[1]][row_i][col] + piece_values[piece[1]]
                else:  # черная фигура
                    score -= flipud(piece_adv_values[piece[1]])[row_i][col] + piece_values[piece[1]]

    return score


def make_move(board, row, col, move, class_board=None, captured_pieces=None):
    # First Solution
    # # print(move[1])
    winner = ''
    if board[move[1]][move[0]] == 'w♚':
        winner = 'Черный'

    old_val = board[row][col]
    moving = board[move[1]][move[0]]
    board[move[1]][move[0]] = board[row][col]
    board[row][col] = '.'
    if class_board is not None and captured_pieces is not None:
        selection = class_board.black_locations.index((col, row))
        class_board.black_locations[selection] = move
        if move in class_board.white_locations:
            enemy_piece = class_board.white_locations.index(move)
            if class_board.white_pieces[enemy_piece] == King:
                class_board.winner = 'Чёрный'

            captured_pieces.append(class_board.white_pieces[enemy_piece])
            class_board.white_pieces.pop(enemy_piece)
            class_board.white_locations.pop(enemy_piece)

    return board, winner


def find_legal_moves(piece, position, class_board):
    if piece[0] == 'w':
        color = WHITE
    else:
        color = BLACK
    pc = piece_dict[piece[1]]
    moves_list = pc(position[0], position[1], color).move(position, class_board)
    return moves_list
