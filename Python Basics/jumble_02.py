#JUMBLING WORDS FUNCTIONS

import random

def choose():
    words=['telephone','cake','rainbow','house','school','tablet','yatch','happy']
    pick=random.choice(words)  
    return(pick)

def jumble(word):
    jword=random.sample(word, len(word))
    return(jword)