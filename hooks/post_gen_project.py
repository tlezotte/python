#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    os.system("make install")

    if '{{ cookiecutter.project_type }}' == 'api':
        os.system("make api")

    if '{{ cookiecutter.project_type }}' == 'cli':
        os.system("make cli")

    os.system("make git")
    os.system("make show")

    remove_file("README.rst")
