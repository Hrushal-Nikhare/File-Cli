import os
from rich import print
import inquirer
from rich.progress import track
from rich.panel import Panel
import json
from os import walk
import subprocess

# print(os.path.abspath('config.json'))

with open(os.path.abspath('config.json'),"r") as json_data:
    data = json.load(json_data)
print(data)

def FileBrowser(last_dir=os.getcwd()):
    files = []
    dirnames = []

    for dirpath, dirnames, filenames in track(walk(last_dir)):
        files.extend(filenames)
        dirnames.extend(dirnames)
        break

    dirnames = list(set(dirnames))
    # for dir in dirnames:
    #     directory = ":open_file_folder: + dir"

    files = ["📄 " + file for file in files]
    dirnames = ["📂 " + dir for dir in dirnames]

    print(Panel(f"\n📁 {last_dir}",title = "Current Folder",expand=False))
    #list of choices
    choices = files + dirnames + ["📁 Open in File Manager", "🔼 Go Up", "🏠 Go to root", "❌ Exit"]
    questions = [
        inquirer.List(
            "Item",
            message="What would you like to do?",
            choices=choices,
        ),
    ]

    answers = inquirer.prompt(questions)
    file = answers["Item"].split(" ", 1) + [last_dir]
    return file


def FileHandler(selected_file, last_dir=os.getcwd()):
    if selected_file[0] == "📄":
        # subprocess.Popen(["notepad", file[1]])
        try:
            subprocess.Popen([f"{data['FileOpener']}", os.path.join(last_dir, selected_file[1])])
        except Exception as e:
            subprocess.Popen(["notepad", os.path.join(last_dir, selected_file[1])])
        finally:
            exit()

    elif selected_file[0] == "📂":
        new_dir = os.path.join(last_dir, selected_file[1])
        while True:
            selected_file = FileBrowser(new_dir)
            FileHandler(selected_file, new_dir)

    elif selected_file[0] == "🔼":
        new_dir = os.path.dirname(last_dir)
        while True:
            selected_file = FileBrowser(new_dir)
            FileHandler(selected_file, new_dir)

    elif selected_file[0] == "🏠":
        home_dir = os.path.abspath(".").split(os.path.sep)[0] + os.path.sep
        while True:
            selected_file = FileBrowser(home_dir)
            FileHandler(selected_file, home_dir)

    elif selected_file[0] == "📁":
        subprocess.Popen(["explorer", last_dir])
        exit()

    elif selected_file[0] == "❌":
        exit()


while True:
    file = FileBrowser()
    FileHandler(file, file[2])

# print("🫡 You selected: [bold red]" + answers["Item"] + "[/bold red]")
# subprocess.Popen(["notepad",file[1]])
# pprint(answers)
