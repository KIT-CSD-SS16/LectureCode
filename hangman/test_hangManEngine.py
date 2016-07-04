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
        self.assertEqual(hangManEngine.readInput('A'),
        'You chose an "A" ')
        self.assertEqual(hangManEngine.readInput('B'),
        'You chose an "B" ')

#if there was a guess of a character, the Message should be changed to the input word
#with all chars, that have not already been guessed replaced with X.

    def test_intermediateString(self):
      hangManEngine = HangManEngine.HangManEngine('GLUCKSRAD')
      hangManEngine.readInput('Z')
      self.assertEqual(hangManEngine.getMessage(),
      'XXXXXXXXX')

      hangManEngine.readInput('R')
      self.assertEqual(hangManEngine.getMessage(),
      'XXXXXXRXX')


