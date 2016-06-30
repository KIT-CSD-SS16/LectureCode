__author__ = 'Thomas Hauth, Martin Heck'

import unittest
import logging
import HangManEngine

# todo: use also the mock library available in python 3.4

# python -m unittest discover
# file names must start with "test*.py"
class HangManEngineTest(unittest.TestCase):
    def test_getStartString(self):
        hangManEngine = HangManEngine.HangManEngine('NOTTESTING')
        self.assertEqual(hangManEngine.getMessage(),
        'This is a game of hangman. For an explanation, please search the web.' )

    def test_readAndReturnCharacter(self):
        hangManEngine = HangManEngine.HangManEngine('NOTTESTING')
        self.assertEqual(hangManEngine.readInput(),
        'You chose an "A" ')
