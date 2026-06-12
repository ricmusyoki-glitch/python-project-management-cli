# Python Project Management CLI

A command-line tool to manage users, projects, and tasks. Built for MODULE-4-LABS using OOP, file I/O, and external packages.

## Features
- Create and list users
- Create and list projects  
- Add tasks to projects with status tracking
- Data persisted to JSON file
- Unit tested with pytest

## Tech Stack
- **Python 3.12**
- **Typer** - CLI framework
- **Rich** - Terminal formatting
- **Pytest** - Unit testing

## Setup


git clone https://github.com/ricmusyoki-glitch/python-project-management-cli.git
cd python-project-management-cli
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## Usage


# Users
python main.py add-user "Alice" "alice@example.com"
python main.py list-users

# Projects
python main.py add-project "My Project" "A description"
python main.py list-projects

# Tasks
python main.py add-task "Fix bug" 1


## Run Tests


pytest tests/


## Project Structure


 main.py          # CLI entry point
 models/          # User, Project, Task models
 utils/           # JSON file I/O
 tests/           # Unit tests
 data/            # Persisted JSON data

