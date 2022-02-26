#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    subprocess.run(["make", "install"])

    if '{{ cookiecutter.project_type }}' == 'api':
        subprocess.run(["make", "api"])

    if '{{ cookiecutter.project_type }}' == 'cli':
        subprocess.run(["make", "cli"])

    subprocess.run(["make", "git"])
    subprocess.run(["make", "show"])

    remove_file("README.rst")
