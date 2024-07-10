import os
# import sys
from pprint import pprint
import inquirer
# files = os.listdir()
from os import walk

files = []
dirnames = []

for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    files.extend(filenames)
    dirnames.extend(dirnames)
    break

dirnames = list(set(dirnames))

questions = [
    inquirer.List(
        "Item",
        message="What do you need?",
        choices= files + dirnames,
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)