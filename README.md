# CLI Todo Application

A simple command-line todo application built with Python that allows you to manage your tasks efficiently from the terminal.

## Features

- **Add Tasks**: Quickly add new tasks to your todo list
- **View Tasks**: Display all your current tasks with numbering
- **Delete Tasks**: Remove tasks you no longer need
- **Update Tasks**: Edit existing tasks
- **Mark Done**: Mark tasks as completed with a checkmark (✓)
- **Interactive Menu**: User-friendly interactive menu using questionary library

## Installation

### Prerequisites
- Python 3.10+ (uses match/case statements)
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/mdsiddique05/synet-task3-cli_todo-siddique.git
cd synet-task3-cli_todo-siddique
```

2. Install dependencies:
```bash
pip install questionary
```

## Usage

Run the application:
```bash
python todo.py
```

### Menu Options

When you run the application, you'll see an interactive menu with the following options:

1. **Add task** - Enter a new task description to add it to your list
2. **View task** - Display all current tasks with their numbers
3. **Delete task** - Select a task from the list to delete it
4. **Update task** - Select a task and modify its description
5. **Mark done** - Select a task and add a checkmark (✓) to mark it as completed
6. **Exit** - Close the application

## How It Works

### File Storage
Tasks are stored in a simple text file (`data.txt`):
- Each task is stored on a separate line
- Completed tasks have a checkmark (✓) appended to them
- The file is automatically created on first run

### Core Functions

- **`clear_screen()`**: Clears the terminal screen (works on Windows and Unix-based systems)
- **`load(li)`**: Adds a new task to the data file
- **`delt()`**: Deletes a selected task from the list
- **`upd()`**: Updates/edits a selected task

## Example Workflow

```
1. Start the application
2. Select "add task" and enter "Buy groceries"
3. Select "add task" and enter "Complete Python project"
4. Select "view task" to see your tasks
5. Select "mark done" and mark "Buy groceries" as completed
6. Select "view task" to see the checkmark next to the completed task
7. Select "update task" to change "Complete Python project" to "Complete Python project - Finished"
8. Select "exit" to close the application
```

## Project Structure

```
synet-task3-cli_todo-siddique/
├── README.md          # This file
├── todo.py            # Main application script
└── data.txt           # Task storage file (auto-generated)
```

## Technologies Used

- **Python 3.10+** - Programming language
- **questionary** - Interactive CLI library for menu selection

## Platform Support

- ✅ Windows
- ✅ macOS
- ✅ Linux

## License

This project is open source and available under the MIT License.

## Author

Created by [mdsiddique05](https://github.com/mdsiddique05)

## Notes

- Tasks are case-sensitive
- The application creates and manages the `data.txt` file automatically
- Empty lines in the data file are handled gracefully
- UTF-8 encoding is used for file operations to support special characters
