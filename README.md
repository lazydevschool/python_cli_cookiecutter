# python_cli_cookiecutter

Welcome to the Battle Tested Python CLI Cookiecutter! This project is designed to help you quickly and easily create a well-structured Python CLI application.

- [Full Walkthrough Video Tutorial](https://youtu.be/ybPwP9DXyOo)
- [Full Walkthrough Blog Tutorial](https://lazydev.school/python-cli-tutorial/)

## Prerequisites

You will need to have `cookiecutter` installed on your machine. You can install it via pip.  You want a global installation so you can use it in any directory.  The safe way to do this is to install it via pipx.

```bash
pip install pipx && pipx ensurepath && pipx install cookiecutter
```

## Usage

```bash
# using ssh
cookiecutter git@github.com:lazydevschool/python_cli_cookiecutter.git
```

OR

Clone the repo to your local machine and run cookiecutter with a path to the directory to the cookie cutter locally.

```bash
cookiecutter /path/to/python-cli-cookiecutter
```

You will be prompted for 3 inputs:

- `project_name`: Human readable project name
- `project_snake`: Project name in snake case (e.g. my_awesome_project)
- `cli_entrypoint`: Entrypoint for the CLI (e.g. my_awesome_cli)

:::note

The project snake will be the name you use to do imports in your project so make sure to keep it short, lowercase, and only use underscores (no hyphens, numbers, punctuation, etc.)

:::
