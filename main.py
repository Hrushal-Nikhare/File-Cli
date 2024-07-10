import os
# import sys
# from pprint import pprint
from rich import print
import inquirer
# files = os.listdir()
from os import walk
import subprocess


files = []
dirnames = []

for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    files.extend(filenames)
    dirnames.extend(dirnames)
    break

dirnames = list(set(dirnames))
# for dir in dirnames:
#     directory = ":open_file_folder: + dir"

files = ["📄 " + file for file in files]
dirnames = ["📂 " + dir for dir in dirnames]

questions = [
    inquirer.List(
        "Item",
        message="What do you need?",
        choices= files + dirnames,
    ),
]

answers = inquirer.prompt(questions)
# print(answers)
file = answers['Item'][2:]
# print(file)

print("🫡 You selected: [bold red]" + answers["Item"] + "[/bold red]")
subprocess.Popen(["notepad",file])
# pprint(answers)