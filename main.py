"""This code is used to solve the word cookies game"""
import itertools
from sorted_dictionary import *

arranged_dictionary = my_dict


def get_user_input():
    """Function to help accept the user's input and store"""
    word_cookie = input('Enter the word in the word cookie tray(in any order):  ')
    return word_cookie


def create_anagrams(function1, function2):
    """Function to help create anagrams of different length of the users word"""
    final_result = []
    for item in range(len(function2), 2, -1):
        # printing result in reduction of one
        results = itertools.permutations(function2, item)
        for j in results:
            word_get = ''.join(j)
            # checking if func word is in the particular key
            if word_get in function1[str(len(word_get))]:
                final_result.append(word_get)
            else:
                pass
    return set(final_result)


def n_letter_words(data):
    """Function to arrange the result gotten in terms of length of letters"""
    arranged_results = dict()
    for word in data:
        length_of_word = len(word)
        if str(length_of_word) in arranged_results:
            arranged_results[str(length_of_word)] += f', {word} '
        else:
            arranged_results[str(length_of_word)] = word
    return arranged_results


def display_final_result(data):
    """Function to return the final result in a formatted loop"""
    for result in data:
        print(f"{result} letter words-->{data[result]}")


display_final_result(n_letter_words((create_anagrams(arranged_dictionary, get_user_input()))))
