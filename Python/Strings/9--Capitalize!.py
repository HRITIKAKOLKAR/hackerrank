"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
#def solve(s):
#return ' '.join(word.capitalize() for word in s.split())
def solve(string):
        result = ''
        word = ''
        s_count = 0
        space = ' '
        for c in range(len(string)):
            if not string[c].isalnum():      # This is a space
                result += word.capitalize()  # append previous word to result
                word = ''                    # reset word to empty string
                s_count += 1                 # inc space count
            else:                            # space has ended
                result += space * s_count    # add previous space to result
                s_count = 0                  # reset space count
                word += string[c]            # add char to current word     
        result += word.capitalize()          # add remaining word at end of loop
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
