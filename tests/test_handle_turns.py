import unittest
from models.handle_turns import HandleTurns
from models.human_player import HumanPlayer
from models.bot_player import BotPlayer

class TestHandleTurns(unittest.TestCase):

    def setUp(self):
        self.handleTurns = HandleTurns()


    def test_has_current_player_token_property(self):
        self.assertEqual( self.handleTurns.currentPlayerToken, None )

    def test_sets_current_player_token(self):
        self.handleTurns.set_currentPlayerToken('O')
        self.assertEqual( self.handleTurns.currentPlayerToken, 'O' )

    def test_trigger_new_turn_is_X(self):
        self.handleTurns.set_currentPlayerToken('O')
        self.handleTurns.change()
        self.assertEqual( self.handleTurns.currentPlayerToken, 'X' )

    def test_trigger_new_turn_is_O(self):
        self.handleTurns.set_currentPlayerToken('X')
        self.handleTurns.change()
        self.assertEqual( self.handleTurns.currentPlayerToken, 'O' )

if __name__ == '__main__':
    unittest.main()
