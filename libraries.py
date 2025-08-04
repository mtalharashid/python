# When you install python you also get random library by default
import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# --------------------------------------------- use FROM in Import ------------------------------------------------------

# form is a keyword in python that you can use when importing a function form a module but it allows you to be little but specific then Import 

# from random import choice
# toss = choice(["head", "tail"])
# print(toss)

# --------------------------------------------- RAND INT ------------------------------------------------------

# randint find random number

# number = random.randint(1, 10)
# print(number)

# ---------------------------------------------  SHUFFLE ------------------------------------------------------

# cards = ["king", "Queen", "jack"]
# random.shuffle(cards)
# print(cards)
# for card in cards:
    # print(card)
    
# ------------------------------------------ Statistics ------------------------------------------------------

# find avrage of some value

# import statistics
# print(statistics.mean([100, 90]))

# ------------------------------------------ Command-line argument ------------------------------------------------------

import sys

# try:
#     print("hello my name is", sys.argv[1])
# except IndexError:
#     print("too few arguments")


# ------------------------------------------ Cowsay ------------------------------------------------------

import cowsay

if len(sys.argv) == 2:
    cowsay.trex("hellow," + sys.argv[1])