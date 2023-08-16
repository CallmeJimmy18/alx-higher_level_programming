#!/usr/bin/python3
def best_score(a_dictionary):
    bestscore = -10
    bestname = ""
    if not a_dictionary:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > bestscore:
            bestscore = a_dictionary[i]
            bestname = i

    return bestname
