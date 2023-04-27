import Piece
from enums import Player

from unittest.mock import Mock
import unittest


class testing(unittest.TestCase):

    def test_get_valid_piece_takes_all_full(self):
        # test case all the possible move full with the another player pieces
        state = Mock()
        state.get_piece = lambda x, y: Piece.Pawn('p', x, y, Player.PLAYER_1)
        state.is_valid_piece = lambda x, y: True
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        getted = kni.get_valid_piece_takes(state)
        excepted = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
        assert len(getted) == len(excepted)
        for location in getted:
            assert location in excepted

    def test_get_valid_piece_takes_all_mine(self):
        # test case all the possible move full with the same player pieces
        state = Mock()
        state.get_piece = lambda x, y: Piece.Pawn('p', x, y, Player.PLAYER_2)
        state.is_valid_piece = lambda x, y: True
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        gated = kni.get_valid_piece_takes(state)
        excepted = []
        assert gated == excepted

    def test_get_valid_piece_takes_all_empty(self):
        # test case all the possible move free without any pieces
        state = Mock()
        state.is_valid_piece = lambda x, y: False
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        gated = kni.get_valid_piece_takes(state)
        excepted = []
        assert gated == excepted

    def test_get_valid_peaceful_moves_all_empty(self):
        # test case all the possible move free without any pieces
        state = Mock()
        state.get_piece = lambda x, y: Player.EMPTY
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        gated = kni.get_valid_peaceful_moves(state)
        excepted = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
        assert len(gated) == len(excepted)
        for location in gated:
            assert location in excepted

    def test_get_valid_peaceful_moves_all_full(self):
        # test case all the possible move full with any pieces
        state = Mock()
        state.get_piece = lambda x, y: Player.PLAYER_2
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        getted = kni.get_valid_peaceful_moves(state)
        excepted = []
        assert len(getted) == len(excepted)
        for location in getted:
            assert location in excepted

    def test_get_valid_peaceful_moves_half_full(self):
        # test case half the possible move full with any pieces
        state = Mock()
        generator = PieceGenerator(4)
        state.get_piece = lambda x, y: generator.generate_Piece(x,y)
        kni = Piece.Knight('n', 3, 3, Player.PLAYER_2)
        gated = kni.get_valid_peaceful_moves(state)
        excepted = [(4, 1), (4, 5), (5, 4), (5, 2)]
        assert len(gated) == len(excepted)
        for location in gated:
            assert location in excepted


class PieceGenerator:
    """
    class for generate some pieces for method
    """
    def __init__(self, number):
        self.counter = 0
        self.number_of_pieces = number

    def generate_Piece(self, x, y):
        self.counter += 1
        if self.counter <= self.number_of_pieces:
            return Piece.Pawn('p', x, y, Player.PLAYER_1)
        else:
            return Player.EMPTY


if __name__ == '__main__':
    unittest.main()
