"""
Hangman.

Authors: Jake Powell, Sam Alvares, Chloe Rife.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random
####### Do NOT attempt this assignment before class! #######

#I will choose a random secret word from a dictionary.
#You set the MINIMUM length of that word.
#What MINIMUM length do you want for the secret word.
#you set the DIFFICULTY of the gam by setting the number of UNSUCCESSFUL choices you can make before you LOSE the game.  The traditional form of Hangman sets this number to 5.
#How many unsuccessful choices do you want to allow yourself?
#Here is what you know about the secret word:
#What letter do you want to try?
#Sorr!


def main():
    print('I will choose a random secret word from a dictionary.')
    print('You set the MINIMUM length of that word.')
    print()
    word_length = int(input('What MINIMUM length do you want for the secret word (less than 22 letters)?'))
    selected_word = random_word_gen(word_length)
    print(selected_word)
    tries_left=int(input('How many unsuccessful choices do you want to allow yourself?'))
    on_going_string=print_initial(len(selected_word))
    while True:
        guess_letter = guess()
        in_or_not=check(guess_letter,selected_word)
        if in_or_not==False:
            tries_left = tries_left - 1
            print('you have (below) tries left')
            print(tries_left)
        elif tries_left>0:
            on_going_string = print_so_far(on_going_string,selected_word,guess_letter)
            print(tries_left)
            if check_won(on_going_string,selected_word):
                break
        if tries_left==0:
            print()
            print('You lost, sucks to suck')
            break





def guess():
    guess_letter = str(input('What letter do you want to try?'))
    return guess_letter

def check(guess_letter,selected_word):
    for k in range(len(selected_word)):
        if selected_word[k] == guess_letter:
            print('Yes, shes in there')
            return True
    print('nope')
    return False

def random_word_gen(word_length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    while True:
        r = random.randrange(0, len(words) - 1)
        random_word = words[r]
        if len(random_word) >= word_length:
            selected_word = random_word
            return selected_word

def print_initial(selected_word_length):
    string= '-'*selected_word_length
    print(string)
    return string


def print_so_far(on_going_string,selected_word,guess_letter):
    new=''
    for k in range(len(selected_word)):
        if selected_word[k]==guess_letter:
            new=new+guess_letter
        elif selected_word[k]== on_going_string[k]:
            new=new+on_going_string[k]
        else:
            new=new+'-'
            print
    print(new)
    return new

def check_won(on_going_string,selected_word):
    if on_going_string==selected_word:
        print()
        print('You got em!')
        return True



main()