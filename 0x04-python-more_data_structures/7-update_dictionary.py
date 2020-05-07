#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary.update({'value' : key})
    else:
        a_dictionary.update({'value' : key})
    return a_dictionary
