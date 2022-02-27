# Python Template

## Requirements

### Install Cookiecutter

>A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.

```
brew install cookiecutter
```

### Install Poetry

>Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
- Installed: `$HOME/.poetry`

## Usefull Installs

### Install pyenv

>Simple Python version management

```
brew install pyenv
```

- Installed versions: `$HOME/.pyenv`

# Init Python Project

```
cookiecutter gh:tlezotte/python
cd [project_name]
make init
```
