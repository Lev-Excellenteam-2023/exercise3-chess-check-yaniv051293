import Piece
from ai_engine import chess_ai
from enums import Player
from chess_engine import game_state

from unittest.mock import Mock
import unittest


class test_interagtion(unittest.TestCase):

    def test_get_valid_piece_moves(self):
        knight = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        knight_mock = Mock(spec=knight)
        knight_mock.get_valid_piece_takes.return_value = []
        knight_mock.get_valid_peaceful_moves.return_value = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4),
                                                             (5, 2)]
        state = Mock()
        knight_mock.get_valid_piece_moves(state)

    def test_evaluate_board(self):
        """

        :return:
        """
        # test of the beginnig start
        state = game_state()
        ai = chess_ai()
        x = ai.evaluate_board(state, Player.PLAYER_1)
        assert x == 0
        # test of the calculating- (hypothetical situation- all the board with pawns)
        state_of_game = Mock()
        state_of_game.is_valid_piece.return_value = True
        state_of_game.get_piece.return_value = Piece.Pawn('p', 6, 3, Player.PLAYER_2)
        ai = chess_ai()
        x = ai.evaluate_board(state_of_game, Player.PLAYER_1)
        assert x == 640  # expected 10*8*8=640


if __name__ == '__main__':
    unittest.main()
