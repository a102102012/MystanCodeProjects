"""
File: hangman.py
Name:Sue Lin 林詩賢
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. Create dashed that covers the length of random word
    2. Create a loop that runs n_Turns
    3. Guess check
        - correct: show covered words, guess next
        - success: show covered words, show winner tagline, end game
        - wrong: decrease guess times count, guess next
        - failed: show the answer, show loser tagline, end game
    """
    # 1. Create dashed that covers the length of random word
    word = random_word()
    cover = cover_up(word)
    # game start
    print('The word looks like ' + cover)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    # 2. Create a loop that runs n_Turns
    for i in range(N_TURNS):
        print('Your guess: ', end='')
        input_ch = input().upper()  # case-insensitive
        input_ch = illegal_checker(input_ch)  # input format to be single alphabet
        # correct guess
        while word.find(input_ch) != -1:
            cover = check_input_return_cover(word, cover, input_ch)
            # check point for winner
            if cover == word:
                return print('You are correct!\nYou win!!\nThe word was: '+word)
            else:  # guess again
                check_input_return_sentence(word, cover, input_ch)
                print('You have ' + str(N_TURNS - i) + ' wrong guesses left.')
                print('Your guess: ', end='')
                input_ch = input().upper()
                input_ch = illegal_checker(input_ch)
        # check point for loser
        if i == N_TURNS-1:
            print('There is no '+ input_ch +'\'s in the word. \n'+'You are completely hung :( \nThe word was: ' + word)
            hung_man()
            return
        # wrong guess, decrease guess times
        check_input_return_sentence(word, cover, input_ch)
        print('You have ' + str(N_TURNS-i-1) + ' wrong guesses left.')
        hang_man(i)


def cover_up(word):
    """
    :param: str, the answer
    :return: str, all dashed
    """
    cover = ''
    for i in range(len(word)):
        cover += '-'
    return(cover)


def illegal_checker(input_ch):
    """
    :param: str or int, user's new input
    :return: str, new input pass
    Ask the user enter the correct format "single character" to end the loop
    """
    while input_ch.isalpha() == False or len(input_ch) != 1:
        print('Illegal format.\n' + 'Your guess: ', end='')
        input_ch = input().upper()
    return input_ch


def check_input_return_cover(word, cover, input_ch):
    """
    :param 1: str, the answer
    :param 2: str, the guess record
    :param 3: str, the new input
    :return: str, updated guess record
    Correct guess -> return updated guess record
    Wrong guess -> return original guess record
    """
    new_cover = ''
    while word.find(input_ch) != -1 : #
         for i in range(len(word)):
             if word[i] == input_ch:
                 new_cover += input_ch
             else:
                 new_cover += cover[i]
         return new_cover
    return cover


def check_input_return_sentence(word, cover, input_ch):
    """
    :param 1: str, the answer
    :param 2: str, the guess record
    :param 3: str, the new input
    :return: str, updated guess record
    Return full sentences with correct guess version and wrong guess version
    """
    new_cover = ''
    while word.find(input_ch) != -1 :
         for i in range(len(word)):
             if word[i] == input_ch:
                 new_cover += input_ch
             else:
                 new_cover += cover[i]
         return print('You are correct!\n'+'The word looks like '+new_cover)
    return print('There is no '+ input_ch +'\'s in the word. \n'+'The word looks like '+cover)


def hang_man(j):
    """
    'param1' int, loop times
    """
    hang_man = ''
    for i in range(j+2):
        if i == 0:
            hang_man += '===\n'
        if i == 1:
            hang_man += ' O\n'
        if i == 2:
            hang_man += '/'
        if i == 3:
            hang_man += '|'
        if i == 4:
            hang_man += '\\\n'
        if i == 5:
            hang_man += '/'
        if i == 6:
            hang_man += ' \\'
    print(hang_man)

def hung_man():
    """
    'param1' int, loop times
    """
    hang_man = ''
    for i in range(7):
        if i == 0:
            hang_man += '===\n'
        if i == 1:
            hang_man += ' X\n'
        if i == 2:
            hang_man += '/'
        if i == 3:
            hang_man += '|'
        if i == 4:
            hang_man += '\\\n'
        if i == 5:
            hang_man += '/'
        if i == 6:
            hang_man += ' \\'
    print(hang_man)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
