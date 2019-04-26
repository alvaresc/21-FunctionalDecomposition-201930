"""
Hangman.

Authors: Jake Powell, Sam Alvares, Chloe Rife.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# done: 2. Implement Hangman using your Iterative Enhancement Plan.

import random
####### Do NOT attempt this assignment before class! #######



def main():
    print('I will choose a random secret word from a dictionary.')
    print('You set the MINIMUM length of that word.')
    print()
    word_length = int(input('What MINIMUM length do you want for the secret word (less than 22 letters)?'))
    selected_word = random_word_gen(word_length)
    #print(selected_word)
    tries_left=int(input('How many unsuccessful choices do you want to allow yourself?'))
    on_going_string=print_initial(len(selected_word))
    while True:
        guess_letter = guess()
        in_or_not=check(guess_letter,selected_word)
        if in_or_not==False:
            tries_left = tries_left - 1
            on_going_string = print_so_far(on_going_string,selected_word,guess_letter)
            print()
            print('You have {} unsuccessful guesses left'.format(tries_left))

        elif tries_left>0:
            on_going_string = print_so_far(on_going_string,selected_word,guess_letter)
            print()
            print('You have {} unsuccessful guesses left'.format(tries_left))
            if check_won(on_going_string,selected_word):
                break
        if tries_left==0:
            print()
            print('You lost, sucks to suck')
            break
        print('*****************************************************')





def guess():
    guess_letter = str(input('What letter do you want to try?'))
    print()
    return guess_letter

def check(guess_letter,selected_word):
    for k in range(len(selected_word)):
        if selected_word[k] == guess_letter:
            print('Yup, shes in there')
            print()
            return True
    print('Nope, try again!')
    print()
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
    print('Heres what ya got so far')
    print(new)
    return new

def check_won(on_going_string,selected_word):
    if on_going_string==selected_word:
        print()
        print('You got em!')
        return True


while True:
    main()
    play_again=str(input('Do you want to play again? Yes or No'))
    if play_again == 'No':
        break