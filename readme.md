# Task Tracker

Task Tracker is a project used to track and manage your tasks. In this project, you will build a simple command-line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Technologies Used
- Python
- VS Code

## Features
The application runs from the command line, accepts user actions and inputs as arguments, and stores the tasks in a JSON file. The user should be able to:

- Add, update, and delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/nanhpauyu/Python-CLI-Task-Tracker.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Python-CLI-Task-Tracker
   ```
3. Run the application and enjoy!

## Example Commands

- Add a task:
  ```sh
  python task_cli.py add "Buy groceries"
  ```
- Update a task:
  ```sh
  python task_cli.py update 1 "Buy groceries and cook dinner"
  ```
- Delete a task:
  ```sh
  python task_cli.py delete 1
  ```
- Mark a task as in progress:
  ```sh
  python task_cli.py mark-in-progress 1
  ```
- Mark a task as done:
  ```sh
  python task_cli.py mark-done 1
  ```
- List all tasks:
  ```sh
  python task_cli.py list
  ```
- List all completed tasks:
  ```sh
  python task_cli.py list done
  ```
- List all pending tasks:
  ```sh
  python task_cli.py list todo
  ```
- List all tasks in progress:
  ```sh
  python task_cli.py list in-progress
  ```

