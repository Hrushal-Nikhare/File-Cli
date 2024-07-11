#! /usr/bin/env python3
"""
Title: File Browser
Author: Hrushal Nikhare

"""

# standard
import os
from os import walk
import subprocess

# rich
from rich import print as rprint
from rich.panel import Panel
from rich.align import Align

# inquirer
import inquirer


data = {
    "FileOpener": "notepad",
    "FileExplorer": "explorer",
    "CodeEditor": "code",
}
code_file = ("py", "css", "json", "html", "js", "java", "cpp", "c", "php", "rb", "go")


def file_browser(last_dir=os.getcwd()):
    """
    Function to browse files and directories
    """
    files = []
    dirnames = []

    for _, dirnames, filenames in walk(last_dir):
        # _ is dirpath
        files.extend(filenames)
        dirnames.extend(dirnames)
        break

    dirnames = list(set(dirnames))

    files = ["📄 " + file for file in files]
    dirnames = ["📂 " + dir for dir in dirnames]

    rprint(
        Align(
            Panel(f"\n📁 {last_dir}", title="Current Folder", expand=False),
            align="center",
        )
    )
    # list of choices
    choices = (
        files
        + dirnames
        + ["📁 Open in File Manager", "🔼 Go Up", "🏠 Go to root", "❌ Exit"]
    )
    questions = [
        inquirer.List(
            "Item",
            message="What would you like to do?",
            choices=choices,
        ),
    ]

    answers = inquirer.prompt(questions)
    file_info = answers["Item"].split(" ", 1) + [last_dir]  # type: ignore
    return file_info


def file_handler(selected_file, last_dir=os.getcwd()):
    """
    Function to handle the selected file
    """
    if selected_file[0] == "📄":
        file_to_open = os.path.join(last_dir, selected_file[1])
        try:
            if selected_file[1].split(".")[-1] in code_file:
                subprocess.Popen([data["CodeEditor"], file_to_open], shell=True)
            else:
                subprocess.Popen([f"{data['FileOpener']}", file_to_open])

        except (OSError, FileNotFoundError) as error:
            rprint(f"Fatal Error: {error} \nOpening with default editor...")
            subprocess.Popen(["notepad", file_to_open])

        finally:
            exit()

    elif selected_file[0] == "📂":
        new_dir = os.path.join(last_dir, selected_file[1])
        while True:
            selected_file = file_browser(new_dir)
            file_handler(selected_file, new_dir)

    elif selected_file[0] == "🔼":
        new_dir = os.path.dirname(last_dir)
        while True:
            selected_file = file_browser(new_dir)
            file_handler(selected_file, new_dir)

    elif selected_file[0] == "🏠":
        home_dir = os.path.abspath(".").split(os.path.sep)[0] + os.path.sep
        while True:
            selected_file = file_browser(home_dir)
            file_handler(selected_file, home_dir)

    elif selected_file[0] == "📁":
        try:
            subprocess.Popen([data["FileExplorer"], last_dir])
        except (OSError, FileNotFoundError):
            subprocess.Popen(["explorer", last_dir])
        exit()

    elif selected_file[0] == "❌":
        exit()


while True:
    file = file_browser()
    file_handler(file, file[2])

