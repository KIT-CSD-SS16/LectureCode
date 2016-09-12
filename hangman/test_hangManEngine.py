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
      '---------')

      hangManEngine.readInput('R')
      self.assertEqual(hangManEngine.getMessage(),
      '------R--')

      hangManEngine.readInput('G')
      hangManEngine.readInput('L')
      hangManEngine.readInput('U')
      hangManEngine.readInput('C')
      hangManEngine.readInput('K')
      hangManEngine.readInput('S')
      hangManEngine.readInput('A')
      hangManEngine.readInput('D')
      self.assertEqual(hangManEngine.getMessage(),
      'GLUCKSRAD \n You won the game.')

      hangManEngine.readInput('N')
      self.assertEqual(hangManEngine.getMessage(),
      '')

    def test_end(self):
      hangManEngine = HangManEngine.HangManEngine('A')
      self.assertFalse(hangManEngine.isFinished())
      hangManEngine.readInput('A')
      hangManEngine.getMessage()
      self.assertTrue(hangManEngine.isFinished())

# if the number of wrong guesses reaches 7, the game ends as well.
# for this test, it is extremely important to be careful in the implementation
# not to handle only the case where the readInput is called with an argument!
      hangManEngine = HangManEngine.HangManEngine('RAD')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      hangManEngine.readInput('U')
      self.assertTrue(hangManEngine.isFinished())
      self.assertEqual(hangManEngine.readInput('U'),
      "You lost the game!")



