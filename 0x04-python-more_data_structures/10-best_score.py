#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = list(a_dictionary.keys())
        name = ""
        score = 0
        for i in new:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                name = i
        return name
