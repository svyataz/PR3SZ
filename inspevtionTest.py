import unittest
from inspection import inspection
from unittest.mock import patch
from io import StringIO

class inspectionTest(unittest.TestCase):

    def inputTest(self, myIn, diagnosis, myOut):
        with patch('builtins.input', side_effect = myIn), patch('sys.stdout', new = StringIO()) as fake_out:
            game_inst = inspection()
            self.assertEqual(game_inst.startInspection(), diagnosis)
            self.assertEqual(fake_out.getvalue().strip(), myOut)

    def test_ally(self):
        self.inputTest(['y', 'y', 'y', 'y'], 'Diagnosis:hypertensive disease',
                       "do you have shortness of breath ?(y/n):"
                       "do you have palpitation ?(y/n):"
                       "do you have pain chest ?(y/n):"
                       "do you have asthenia ?(y/n):"
                       )

    def test_asthma(self):
        self.inputTest(['y', 'n', 'n', 'y', 'n', 'y', 'y'], 'Diagnosis:asthma',
                       'do you have shortness of breath ?(y/n):'
                       'do you have palpitation ?(y/n):'
                       'do you have unresponsiveness ?(y/n):'
                       'do you have chest tightness ?(y/n):'
                       'do you have pain chest ?(y/n):'
                       'do you have wheezing ?(y/n):'
                       'do you have symptom aggravating factors ?(y/n):'
                       )

    def test_missinput(self):
        self.inputTest(['y', 'something', 'y', 'y', 'y'], 'Diagnosis:hypertensive disease',
                       'do you have shortness of breath ?(y/n):'
                       'do you have palpitation ?(y/n):'
                       'incorrect answer\n'
                       'do you have palpitation ?(y/n):'
                       'do you have pain chest ?(y/n):'
                       'do you have asthenia ?(y/n):'
                       )

    def test_alln(self):
        self.inputTest(['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                       'You are healthy',
                       "do you have shortness of breath ?(y/n):"
                       "do you have feeling hopeless ?(y/n):"
                       "do you have unresponsiveness ?(y/n):"
                       "do you have swelling ?(y/n):"
                       "do you have lethargy ?(y/n):"
                       "do you have general discomfort ?(y/n):"
                       "do you have mass of body structure ?(y/n):"
                       "do you have decreased body weight ?(y/n):"
                       "do you have heavy feeling ?(y/n):"
                       "do you have pain abdominal ?(y/n):"
                       "do you have mental status changes ?(y/n):"
                       "do you have prostatism ?(y/n):"
                       "do you have headache ?(y/n):"
                       "do you have scar tissue ?(y/n):"
                       "do you have worry ?(y/n):"
                       "do you have monocytosis ?(y/n):"
                       "do you have rhonchus ?(y/n):"
                       "do you have awakening early ?(y/n):"
                       "do you have wheezing ?(y/n):"
                       "do you have paralyse ?(y/n):"
                       "do you have lesion ?(y/n):"
                       "do you have cushingoid facies ?(y/n):"
                       "do you have ambidexterity ?(y/n):"
                       )