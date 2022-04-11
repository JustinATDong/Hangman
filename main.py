
# -*- coding: utf-8 -*-
"""
Justin Dong
CPSC 223P-01
Thu Apr 7, 2021
donganhtuanjustin@fullerton.edu
"""

import random

# Hangman class.
class Hangman:
    
    def __init__(self, word, triesAllowed):
        self.word = word
        self.triesAllowed = triesAllowed
        self.usedLetters = []
        self.rightLetters = []
    

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        if letter in self.word:
            if letter in self.usedLetters:
                return True
            else:
                self.usedLetters.append(letter)
                self.rightLetters.append(letter)
                return True
        else:
            if letter in self.usedLetters:
                return False
            else:
                self.triesAllowed -= 1
                self.usedLetters.append(letter)
                return False

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        return self.triesAllowed

    
    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        dash = "-" * len(self.word)
        
        for i in range(len(self.word)):
            if self.word[i] in self.rightLetters:
                dash = dash[: i] + self.word[i] + dash[i + 1:]
        return dash

    
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        used = ''
        
        for u in self.usedLetters:
            used += u + '-'
            
        return used

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        dashes = self.GetDisplayWord()
        
        if '-' in dashes:
            return False
        else:
            return True
        

    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        pass

# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()
    
    Game = True
    
    # Seed the random number generator with current system time
    random.seed()
    
    # Convert the string of words in wordFile to a list,
    # then get a random word using
    # randomIndex = random.randint(min, max)
    
    words = list(wordFileText.split())
    randomIndex = random.randint (0, len(words))
    
    word = words[randomIndex]
    
    if len(word) >= 8:
        numberTries = len(word)
    else:
        numberTries = 8
    
    # Instantiate a game using the Hangman class
    game = Hangman(word, numberTries)
    
    # Use a while loop to play the game
    while Game:
        numberTries = game.GetNumTriesLeft()
        
        if numberTries == 0 and finalResult == False:
            print(f"You lost. The word was {word}")
            print("-----|\n |   |\n |   0\n |  /|\\\n |   U\n |  / \\\n | \n |\n---")
            print("\nTake this L")
            
            Game = False
            
        elif numberTries != 0:
            print("Your words:", game.GetDisplayWord())
            print(f"You have {numberTries} guesses left\n")
            
            userGuess = input("Guess a letter: ").lower()
            
            if len(userGuess) > 1:
                print("One letter at a time!")
                
            else:
                guessResult = game.Guess(userGuess)
                finalResult = game.GetGameResult()
                
                
            if guessResult == True:
                print("Nice! The letters you used:", game.GetLettersUsed())
            else:
                print("Nice try. The letters you used:", game.GetLettersUsed())
                
            
            if finalResult == True:
                print(f"You win! The word was {word}")
                print("-----|\n |    \n |    \n |     \n |   0\n |  \\|/\n |   U\n |  / \\\n---")
                Game == False
                
            else:
                continue