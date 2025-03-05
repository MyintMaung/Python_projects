import random
from words import words

def check_valid(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

