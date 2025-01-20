import copy
from board import Board


class AI:

    def minimax(self, game_board: Board, maximizing: bool, depth, alpha, beta):
        """
        This function implements the minimax algorithm.
        :param game_board: this is the board on which the algorithm will be applied
        :param maximizing: this is a boolean value which tells the algorithm if it is maximizing or not
        :param depth: this is the depth of the algorithm
        :param alpha: this is the alpha value of the algorithm
        :param beta: this is the beta value of the algorithm
        :return: it returns the evaluation of the board and the best move
        """
        current_state = game_board.final_state()
        if depth == 0:
            return current_state, None
        if current_state == 1:
            return 1, None
        if current_state == -1:
            return -1, None
        if game_board.is_board_full():
            return 0, None
        if maximizing:
            maximum_evaluation = -100
            best_move = None
            columns = game_board.possible_columns()
            for column in columns:
                temporary_board = copy.deepcopy(game_board)
                temporary_board.make_move(column, "red")
                if temporary_board.final_state() == 1:
                    return 1, column
                evaluation = self.minimax(temporary_board, False, depth - 1, alpha, beta)[0]
                if evaluation > maximum_evaluation:
                    maximum_evaluation = evaluation
                    best_move = column
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return maximum_evaluation, best_move
        elif not maximizing:
            minimum_evaluation = 100
            best_move = None
            columns = game_board.possible_columns()
            for column in columns:
                temporary_board = copy.deepcopy(game_board)
                temporary_board.make_move(column, "yellow")
                if temporary_board.final_state() == -1:
                    return -1, column
                evaluation = self.minimax(temporary_board, True, depth - 1, alpha, beta)[0]
                if evaluation < minimum_evaluation:
                    minimum_evaluation = evaluation
                    best_move = column
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return minimum_evaluation, best_move

    def evaluate(self, game_board: Board):
        evaluation, move = self.minimax(game_board, False, 3, -1000, 1000)
        print(f"AI has chosen to place the circle in column {move} with an evaluation of {evaluation}")
        return move
