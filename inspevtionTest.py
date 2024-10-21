import unittest
from inspection import inspection
from unittest.mock import patch
from io import StringIO

class inspectionTest(unittest.TestCase):

    def inputTest(self, myIn, myOut):
        with patch('builtins.input', side_effect = myIn), patch('sys.stdout', new = StringIO()) as fake_out:
            game_inst = inspection()
            self.assertEqual(game_inst.startInspection(), myOut)

    def test_ally(self):
        self.inputTest(['y', 'y', 'y', 'y'], 'Diagnosis:hypertensive disease')

    def test_asthma(self):
        self.inputTest(['y', 'n', 'n', 'y', 'n', 'y', 'y'], 'Diagnosis:asthma')

    def test_missinput(self):
        self.inputTest(['y', 'something', 'y', 'y', 'y'], 'Diagnosis:hypertensive disease')

    def test_alln(self):
        self.inputTest(['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            'You are healthy')