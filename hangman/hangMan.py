#! /usr/bin/env python3.4

import logging

import HangManEngine

def main():
  # my code here
  hangManEngine = HangManEngine.HangManEngine('GLUCKSRAD')
  while hangManEngine.getMessage():
      print (hangManEngine.getMessage())
      print (hangManEngine.readInput())
print ('Bye')

if __name__ == "__main__":
  main()
