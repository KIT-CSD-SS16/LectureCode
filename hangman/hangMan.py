#! /usr/bin/env python3.4

import logging

import HangManEngine

def main():
  # my code here
  hangManEngine = HangManEngine.HangManEngine('RAD')
  while not hangManEngine.isFinished():
      print (hangManEngine.getMessage())
      print (hangManEngine.readInput())

if __name__ == "__main__":
  main()
