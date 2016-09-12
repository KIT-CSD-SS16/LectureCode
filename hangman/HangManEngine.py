__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    self.guessedChars = []
    self.secretWord = secretWord
    self.gameIsWon = False
    self.CountOfWrongGuesses = 0

  def isFinished(self):
    return self.gameIsWon or (self.CountOfWrongGuesses > 6)

  def sendXorChar(self, letter):
    for char in self.guessedChars:
      if letter == char:
        return letter
    return '-'
    print ("Bug")

  def getMessage(self):
    if self.isFinished() == True:
        if not self.gameIsWon:
          return 'You lost the game!'
        return ''
    if not self.guessedChars:
      return\
      'This is a game of hangman. For an explanation, please search the web.'
    output = ''
    for letter in self.secretWord:
      output += self.sendXorChar(letter)

    if '-' not in output:
      output += ' \n You won the game.'
      self.gameIsWon=True
    return output

  def readInput(self, testChar = None):
    if self.gameIsWon == True:
      return "Game going to terminate itself."
    if testChar:
      guessChar = testChar
    else:
      guessChar = input('Choose a character: ')
    # increase counter, if testChar not in secretWord
    if  str(self.secretWord).find(guessChar)== -1:
      self.CountOfWrongGuesses +=1

    self.guessedChars.append(guessChar)
    if (self.CountOfWrongGuesses > 6 ):
      return 'You lost the game!'
    return\
    '''You chose an "''' + guessChar + '''" '''
