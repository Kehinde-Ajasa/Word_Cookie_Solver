"""This code is used to solve the word cookies game"""
import itertools


def get_user_input():
    """function to help accept all the user's inputs"""
    word_cookie = 'currency'  # input('Enter the word in the word cookie tray(in any order): ')
    return word_cookie


def open_dict_file():
    """function to help open up the dictionary file for accessing all the english language words"""
    with open('C:\\Users\\MY PC\\Desktop\\PYTHON PROJECTS\\RHEMA VERSIONS\\my.txt', 'r') as file:  # opening the file
        dictionary = file.read()
        # using the .split method to convert each word in the file to a individual and collectively as a list
        words = dictionary.split()
        return words


def sort_dictionary(a):
    """function to help scatter all the user's word into a distinct amount of letter words"""
    word_dictionary = {}
    for w in a:
        word_length = len(w)
        # using the string version of the length of the word as a key in the empty Rhema Dictionary
        if str(word_length) in word_dictionary:
            # creating a key for that particular number and adding items to it (the space in the string is for neatness)
            word_dictionary[str(word_length)] += f' {w}'
        else:
            word_dictionary[str(word_length)] = w
    return word_dictionary


def CookWords(function1, function2):
    """function to help scatter the words and get the final result of the rhema program"""
    final_result = []
    for item in range(len(function2), 2, -1):
        # printing result in reduction of one
        results = itertools.permutations(function2, item)
        for j in results:
            word_get = ''.join(j)
            # checking if a word is in the particular key
            if word_get in function1[str(len(word_get))]:
                final_result.append(word_get)
            else:
                pass
    return set(final_result)


print((CookWords(sort_dictionary(open_dict_file()), get_user_input())))