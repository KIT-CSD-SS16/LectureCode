__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    pass

  def getMessage(self):
    return\
    'This is a game of hangman. For an explanation, please search the web.'

  def readInput(self, testChar = None):
    if testChar:
      guessChar = testChar
    else:
      guessedChar = input('Choose a character: ')
    return\
    '''You chose an "''' + guessedChar + '''" '''
