import itertools
from itertools import permutations
import enchant
import math


def permute(string):
    strings = list(permutations(string))
    return strings

def unscramble(text):
    print("You word has {} combinations....Be Patient!".format(math.factorial(len(text))))
    strings = permute(text)
    for i in range(len(strings)):
            strings[i] = ''.join(strings[i])

    dictionary = enchant.Dict("en_US")
    current_string = 0
    words = []
    for i in strings:
        #print("On string {}".format(current_string))
        if dictionary.check(i):
            words.append(i)
        current_string +=1
    print(" ***** POSSIBLE WORDS ***** ")
    print(words)
    
print("Entering a word over 9 characters will take a substantial amount of time!")
text = input("Enter scrambled word or string: ")
words = text.split(" ")
for word in words:
    unscramble(word)



        

