#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    # TODO: implement me. had '1 cup' as the return value...why?
    decoded = []
    for i in str:
        try:
            decoded.append( ENCODING.get(i," "))
        except:
            pass
 
    return "".join(decoded)


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # TODO: implement me
    lst = line.split("#")
    d_amt = ""
    for l in lst[0]:
        try:
            d_amt = d_amt + ENCODING[l]
        except:
            d_amt = d_amt + " "
    d_desc = ""
    for l in lst[1]:
        try:
            d_desc = d_desc + ENCODING[l]
        except:
            d_desc = d_desc + " "

    #description = decoded.split("#")
    new_ingredient = Ingredient(d_amt, d_desc)
    #new_ingredient.amount = amount
    #new_ingredient.description = description
    return new_ingredient #.amount,  new_ingredient.description  #Ingredient("1 cup", "butter")


def main():
    """A program that decodes a secret recipe"""
    # TODO: implement me
    with open("secret_recipe.txt", "r") as infile, open("decoded_recipe.txt", "w") as outfile:
        for line in infile:
            line = line.strip()
            decoded_ingredient = decode_ingredient(line)
            if decoded_ingredient is not None:
                outfile.write(str(decoded_ingredient.amount) + str(decoded_ingredient.description) + '\n')

if __name__ == "__main__":
    main()
