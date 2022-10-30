"""This code is used to solve the word cookies game"""
import itertools


def open_dictionary_file():
    """Opening up the file containing over 350 thousand words"""
    with open('C:\\Users\\MY PC\\Desktop\\PYTHON PROJECTS\\Dictionary.txt', 'r') as filename:
        dic_file = filename.read()
        dic_list = dic_file.split()
    return dic_list


def word_cookies_dictionary(a_function):
    """Creating a dictionary with the keys as a casted number to string
    and values as empty list that would get words appended during sorting."""
    universal_dictionary = {'1': [], '2': [], '3': [], '4': [], '5': [],
                                        '6': [], '7': [], '8': [], '9': [], '10': [],
                                        '11': [], '12': [], '13': [], '14': [], '15': [],
                                        '16': [], '17': [], '18': [], '19': [], '20': [],
                                        '21': [], '22': [], '23': [], '24': [], '25': [], '26': [], }
    for i in a_function:
        if str(len(i)) in universal_dictionary:
            universal_dictionary[str(len(i))].append(i)
        else:
            universal_dictionary[str(len(i))] = []
    return universal_dictionary


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


display_final_result(n_letter_words((create_anagrams(word_cookies_dictionary(open_dictionary_file()), get_user_input()))))
