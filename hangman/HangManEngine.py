__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    self.guessedChars = []

  def getMessage(self):
    if not self.guessedChars:
      return\
      'This is a game of hangman. For an explanation, please search the web.'
    return\
    'XXXXXXXXX'

  def readInput(self, testChar = None):
    if testChar:
      guessChar = testChar
    else:
      guessChar = input('Choose a character: ')
    self.guessedChars.append(guessChar)
    return\
    '''You chose an "''' + guessChar + '''" '''
