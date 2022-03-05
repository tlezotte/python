#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_PATH = os.path.join(PROJECT_DIRECTORY, "{{cookiecutter.project_slug}}")
PROJECT_TMP_PATH = os.path.join(PROJECT_DIRECTORY, "{{cookiecutter.project_slug}}_tmp")


def run_make(target):
    """Initialize a new project

    Args:
        target (string): name of make target to run
    """
    os.system("make " + target)

def copy_files():
    shutil.copyfile(PROJECT_TMP_PATH + "/.gitignore", PROJECT_PATH)
    shutil.copyfile(PROJECT_TMP_PATH + "/Makefile", PROJECT_PATH)
    shutil.copyfile(PROJECT_TMP_PATH + "/README.md", PROJECT_PATH)

def remove_tmp():
    shutil.rmtree(PROJECT_TMP_PATH)


if __name__ == '__main__':
    copy_files()
    remove_tmp()
    run_make("init")
