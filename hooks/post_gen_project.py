#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """
    Remove the file if it exists
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def git_config(item):
    """
    Get a git user config value
    """
    config = subprocess.run(['git', 'config', '--global', 'user.' + item], stdout=subprocess.PIPE)
    results = config.stdout.decode('utf-8').strip()
    return results

def change_git_config(filename):
    """
    Change the git config user's name and email in the specified file
    """
    fin = open(filename, "rt")
    data = fin.read()
    data = data.replace('FULL_NAME', git_config("name"))
    data = data.replace('EMAIL', git_config("email"))
    fin.close()

    fin = open(filename, "wt")
    fin.write(data)
    fin.close()

def init_project():
    """
    Initialize a new project
    """
    os.system("make init")


if __name__ == '__main__':
    files = ["pyproject.toml","Makefile"]
    for file in files:
        change_git_config(file)

    init_project()
