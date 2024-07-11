# File Browser

A simple, interactive file browser written in Python. This tool allows users to navigate through their file system using a command-line interface. It provides a convenient way to open files and directories without leaving the terminal.

## Features

- **Browse Files and Directories**: Navigate through your file system with ease.
- **Open Files**: Open files with the default or specified applications directly from the interface.
- **Navigate to Parent or Root Directory**: Quickly move to the parent directory or jump to the root directory with a single command.
- **Open in File Manager**: Open the current directory in your system's file manager for a graphical view.
- **Customizable**: Easily configure the file opener, file explorer, and code editor paths according to your preferences.

## Requirements

- Python 3.x
- `rich` library for rich text and beautiful formatting in the terminal.
- `inquirer` library for interactive command-line interfaces.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries by running:

```bash
pip install rich inquirer
```

## Usage

To start the file browser, navigate to the directory containing main.py and run:

```bash
python main.py
```

Follow the on-screen prompts to navigate through your file system.

## Configuration

The script uses a default configuration for opening files and directories. You can customize the file opener, file explorer, and code editor by modifying the data dictionary in main.py:

```python
data = {
    "FileOpener": "notepad",  # Default file opener
    "FileExplorer": "explorer",  # Default file explorer
    "CodeEditor": "code",  # Default code editor (Visual Studio Code)
}
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.