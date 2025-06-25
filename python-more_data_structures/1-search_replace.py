#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Return a new list where 'search' elements are replaced with 'replace'
    return [replace if element == search else element for element in my_list]
