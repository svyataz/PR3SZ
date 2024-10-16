import unittest
from inspection import inspection
from unittest.mock import patch
import io

class inspectionTest(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    def ansInput_test(self, mock_input):
        game_inst = inspection()
        game_inst.ansInput()
        self.assertEqual(game_inst.ans_getter(), 'Omsk')