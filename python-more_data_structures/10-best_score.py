#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # Find the key with the maximum integer value
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
