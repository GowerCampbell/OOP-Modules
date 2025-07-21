"""
OOP - MODULES

This Python script demonstrates how to set up professional-grade Python projects,
manage dependencies, and adhere to best practices like PEP 8 linting. It also
includes examples of modular programming, file organization, and testing.
"""

# =============================================================================
# SETTING UP PROFESSIONAL-GRADE PYTHON PROJECTS
# =============================================================================
"""
To establish a robust foundation for your Python project, follow these steps:
1. Set up a virtual environment.
2. Create a requirements.txt file for dependency management.
3. Install a linter (e.g., Flake8) to enforce coding standards.
4. Organize your project files into a clear and consistent structure.
"""

# =============================================================================
# VIRTUAL ENVIRONMENTS
# =============================================================================
"""
Virtual environments isolate project dependencies, ensuring they don't interfere
with other projects or the system-wide Python installation.

To create a virtual environment:
    python -m venv venv

To activate it:
    On Windows: venv\Scripts\activate
    On macOS/Linux: source venv/bin/activate
"""

# =============================================================================
# FILE STRUCTURE
# =============================================================================
"""
A well-organized project structure improves maintainability and collaboration.
Here’s an example structure:

project_name/
│
├── src/                   # Source code
│   ├── module1/           # Module 1
│   │   ├── __init__.py    # Marks the directory as a Python package
│   │   └── module1.py     # Module 1 implementation
│   └── module2/           # Module 2
│       ├── __init__.py
│       └── module2.py
│
├── tests/                 # Test files
│   ├── test_module1.py    # Tests for Module 1
│   └── test_module2.py    # Tests for Module 2
│
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── .gitignore             # Files/directories to ignore in version control
"""

# =============================================================================
# DEPENDENCY MANAGEMENT
# =============================================================================
"""
The requirements.txt file lists all project dependencies and their versions.
This ensures consistent installation across environments.

To generate a requirements.txt file:
    pip freeze > requirements.txt

To install dependencies from requirements.txt:
    pip install -r requirements.txt
"""

# =============================================================================
# VERSION CONTROL
# =============================================================================
"""
Use Git for version control to track changes, collaborate, and maintain a history
of your project.

To initialize a Git repository:
    git init
"""

# =============================================================================
# LINTING
# =============================================================================
"""
Linting analyzes code to flag errors, bugs, and style violations. It enforces
coding standards and improves code quality.

Example: Running Flake8 to check for PEP 8 compliance:
    flake8 example.py
"""

# =============================================================================
# EXAMPLE: PEP 8 LINTING
# =============================================================================
"""
Below is an example of code with intentional errors to demonstrate linting.
"""

def add_numbers(a, b):
    result = a + b
    print(result)

# Intentional error: using an undefined variable 'c'
print(c)

"""
Running Flake8 on this code will produce an error:
    example.py:7:7: F821 undefined name 'c'
"""

# =============================================================================
# DEFINING MODULES TO SEPARATE CONCERNS
# =============================================================================
"""
In Python, a module is a file containing Python definitions and statements.
Modules allow you to organize code into separate files, improving maintainability
and readability.
"""

# =============================================================================
# FILE ORGANIZATION IN VS CODE
# =============================================================================
"""
Here’s an example of a well-organized project structure:
"""

# my_project/
# │
# ├── main.py              # Main entry point
# ├── data_access.py       # Data access logic
# ├── business_logic.py    # Business logic
# ├── user_interface.py    # User interface
# ├── utilities.py         # Utility functions
# ├── config.py            # Configuration settings
# ├── tests/               # Test files
# │   └── tests.py
# └── constants.py         # Constant values

# =============================================================================
# MAIN MODULE (main.py)
# =============================================================================
"""
The main module is the entry point of the application.
"""

from user_interface import start_application

if __name__ == "__main__":
    start_application()

"""
Explanation:
- Imports the `start_application` function from the `user_interface` module.
- The `if __name__ == "__main__":` condition ensures the function is called only
  when the script is executed directly.
"""

# =============================================================================
# DATA ACCESS MODULE (data_access.py)
# =============================================================================
"""
The data access module handles interactions with the data source.
"""

class TaskRepository:
    def get_tasks(self):
        """Retrieve tasks from the data source."""
        # Placeholder implementation - replace with actual data retrieval logic
        pass

    def save_task(self, task):
        """Save a task to the data sink."""
        pass

"""
Explanation:
- Implements the repository pattern to separate data retrieval logic.
- Defines methods like `get_tasks` and `save_task` for interacting with the data source.
"""

# =============================================================================
# BUSINESS LOGIC MODULE (business_logic.py)
# =============================================================================
"""
The business logic module encapsulates the core functionality of the application.
"""

from data_access import TaskRepository

class TaskService:
    def __init__(self):
        """Initialize the TaskService with a TaskRepository."""
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        """Get all tasks from the data source."""
        return self.task_repository.get_tasks()

    def add_task(self, task):
        """Add a new task to the data source."""
        self.task_repository.save_task(task)

class Task:
    def __init__(self, title, description):
        """Initialize a Task object with a title and description."""
        self.title = title
        self.description = description

"""
Explanation:
- Encapsulates the business logic of the application.
- Uses `TaskRepository` to interact with the data source.
- Defines a `Task` class to represent tasks.
"""

# =============================================================================
# USER INTERFACE MODULE (user_interface.py)
# =============================================================================
"""
The user interface module provides a command-line interface for user interaction.
"""

from business_logic import TaskService

def start_application():
    """Start the Task Management Application."""
    task_service = TaskService()

    while True:
        print("Task Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tasks = task_service.get_all_tasks()
            print("Tasks: ")
            for task in tasks:
                print(f"- {task}")
        elif choice == "2":
            new_task = input("Enter task description: ")
            task_service.add_task(new_task)
            print("Task added successfully")
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

"""
Explanation:
- Provides a simple command-line interface for users to interact with the application.
- Uses `TaskService` to handle user actions.
"""

# =============================================================================
# UTILITIES MODULE (utilities.py)
# =============================================================================
"""
The utilities module contains helper functions used across the application.
"""

def format_date(date):
    """Format a date string."""
    pass

"""
Explanation:
- Defines utility functions like `format_date` for consistent date formatting.
"""

# =============================================================================
# CONFIGURATION MODULE (config.py)
# =============================================================================
"""
The configuration module holds settings for the application.
"""

FILENAME = "data.txt"

"""
Explanation:
- Contains configuration variables like `FILENAME` for data storage.
"""

# =============================================================================
# TESTS MODULE (tests.py)
# =============================================================================
"""
The tests module contains unit tests to validate the application's functionality.
"""

import unittest
from business_logic import TaskService, Task

class TestTaskService(unittest.TestCase):
    def test_add_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        task_service = TaskService()
        initial_task_count = len(task_service.get_all_tasks())
        new_task = Task(title="New Task", description="Description of the new task")

        # Act
        task_service.add_task(new_task)

        # Assert
        updated_task_count = len(task_service.get_all_tasks())
        self.assertEqual(updated_task_count, initial_task_count + 1)
        self.assertIn(new_task, task_service.get_all_tasks())

if __name__ == "__main__":
    unittest.main()

"""
Explanation:
- Uses the Arrange-Act-Assert pattern to structure tests.
- Ensures the `add_task` method works as expected.
"""

# =============================================================================
# CONSTANTS MODULE (constants.py)
# =============================================================================
"""
The constants module defines constant values used across the application.
"""

TASK_MAX_LENGTH = 100

"""
Explanation:
- Defines constants like `TASK_MAX_LENGTH` for maximum task description length.
"""

# =============================================================================
# FINAL NOTES
# =============================================================================
"""
- Use virtual environments to isolate dependencies.
- Follow PEP 8 guidelines for clean and readable code.
- Write tests to ensure your code works as expected.
- Organize your project into modules to separate concerns and improve maintainability.
"""