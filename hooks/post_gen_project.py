#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_PATH = os.path.join(PROJECT_DIRECTORY, "../{{cookiecutter.project_slug}}")


def run_make(target):
    """Initialize a new project

    Args:
        target (string): name of make target to run
    """
    os.system("make " + target)

def copy_files():
    shutil.copyfile(PROJECT_DIRECTORY + "/.gitignore", PROJECT_DIRECTORY)
    shutil.copyfile(PROJECT_DIRECTORY + "/Makefile", PROJECT_DIRECTORY)
    shutil.copyfile(PROJECT_DIRECTORY + "/README.md", PROJECT_DIRECTORY)

def remove_tmp():
    shutil.rmtree(PROJECT_DIRECTORY)


if __name__ == '__main__':
    copy_files()
    remove_tmp()
    run_make("init")
