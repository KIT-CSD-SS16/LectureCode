__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    self.guessedChars = []
    self.secretWord = secretWord

  def sendXorChar(self, letter):
    for char in self.guessedChars:
      if letter == char:
        return letter
    return 'X'


  def getMessage(self):
    if not self.guessedChars:
      return\
      'This is a game of hangman. For an explanation, please search the web.'
    output = ''
    for letter in self.secretWord:
      output += self.sendXorChar(letter)

    return output

  def readInput(self, testChar = None):
    if testChar:
      guessChar = testChar
    else:
      guessChar = input('Choose a character: ')
    self.guessedChars.append(guessChar)
    return\
    '''You chose an "''' + guessChar + '''" '''
