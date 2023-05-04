import random as R
from words import words_list

def get_word(): #function to get random word from our word_list in our words python file
    word = R.choice(words_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word) # this makes sure theres enough underscores for every letter in our word were trying to guess
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("lets playyyyyyyy Hangamanu!!(japanese accent)")
    #print(display_hangman(tries)) #we did not create this function yet
    print(word_completion)
    print("\n")
    #not keyword makes the guessed variable equal a True boolean value by changing the False boolean value
    while not guessed and tries > 0: #not keyword makes guessed a True boolean value and tries start off greater than zero, if tries equal to zero or guessed is changed to a True value this will stop the while loop.
        guess = input("Please guess a letter or word!: ".title()).upper()
        if guess == 1 and guess.isalpha():
            if guess in guessed_letters: # if you already guessed this letter
                print("boy you already guessed this letter".title(), guess , "come on now!!")
                #tries -= 1    -if you want to make it harder you can add this here or for a hard mode
            elif guess not in word: # if the letter you guessed is not in the word itself
                print("this letter".title(), guess, "is not in the word!!")
                print("you suck at this forreal!!".title())
                tries -= 1
                guessed_letters.append(guess.upper())
            else: #if the letter is correct and in the word itself
                print("Good job", guess, "is in the word!!")
                guessed_letters.append(guess.upper())
                word_as_list = list(word_completion) # this is a completely new variable
                indices = [i for i, letter in enumerate(word) if letter == guess] # enumerate function gives back to variables in a for loop the index for each word which is the variable i and the word itself which is the variable letter, this is a for loop.
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if '_' not in word_completion:
                    guessed = True #By making this true we end or stop the while loop from looping anymore
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word, ".title() + guess + ".")
            elif guess != word: # != operator for is not
                print(guess.title(), "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word #By making this true we end or stop the while loop from looping anymore
        else:
            print("not a valid guess you m0ther###")
            print(word_completion)
            print(display_hangman(tries)) #function not made yet
            print("\n")
        if guessed: #if guessed == True
            print("great job you guessed correctly and Won.".title())
        else:
            print("the word was ", word, ".")
            return "sorry you lost you need to get better boy.".title()


def display_hangman(tries):
    #final state: 1 head, 1 torso, 2 arms, 2 legs
    stages = ["""
                 -------   
                |      | 
                |       0
                |      / \ 
                |       |   
                |      / \  
                |
                |---------+ 
                """,
              """
                 -------
                |       |
                |       0
                |      / \ 
                |       |
                |      /
                |
                |__________+
              """,
              """
                -------
                |       |  
                |       0
                |      / \ 
                |       |
                |
                |__________+
              """,
              """
                 _______
                |        |
                |        0
                |       / \ 
                |
                |
                |
                |___________+
              """,
              """
                   __________
                 |            |
                 |            0
                 |           / 
                 |  
                 |  
                 |
                 ________________+
              """,
              """
                __________
               |            |
               |            0
               |
               |
               |
               |
                ______________+
              """,
              """
                _________
              |           |
              |
              |
              |
              |
              |
                _____________+
              """

              ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again?  (Y/N)  ").upper() == "Y": #the == operator is the comparison operator for if the input of the user is equal to Y.
        word = get_word()
        play(word)


if __name__ == "__main__":
   main()





