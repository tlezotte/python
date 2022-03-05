#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run_make(target):
    """Initialize a new project

    Args:
        target (string): name of make target to run
    """
    os.system("make " + target)

def copy_files():
    shutil.copyfile("../{{cookiecutter.project_slug}}_tmp/.gitignore", ".gitignore")
    shutil.copyfile("../{{cookiecutter.project_slug}}_tmp/Makefile", "Makefile")
    shutil.copyfile("../{{cookiecutter.project_slug}}_tmp/README.md", "README.md")

def remove_tmp():
    shutil.rmtree("../{{cookiecutter.project_slug}}_tmp")


if __name__ == '__main__':
    copy_files()
    remove_tmp()
    run_make("init")
