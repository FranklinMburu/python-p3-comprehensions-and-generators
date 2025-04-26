# lib/list_comprehension.py

def return_evens(seq):
    return [num for num in seq if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]
