#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    name = subprocess.run(['git', 'config', '--global', 'user.name'], stdout=subprocess.PIPE)
    user_name = name.stdout.decode('utf-8').strip()
    email = subprocess.run(['git', 'config', '--global', 'user.email'], stdout=subprocess.PIPE)
    user_email = email.stdout.decode('utf-8').strip()

    # Replace git name and email in pyproject.toml
    fin = open("pyproject.toml", "rt")
    data = fin.read()
    data = data.replace('FULL_NAME', user_name)
    data = data.replace('EMAIL', user_email)
    fin.close()

    fin = open("pyproject.toml", "wt")
    fin.write(data)
    fin.close()

    # Replace git name and email in Makefile
    fin = open("Makefile", "rt")
    data = fin.read()
    data = data.replace('FULL_NAME', user_name)
    data = data.replace('EMAIL', user_email)
    fin.close()

    fin = open("Makefile", "wt")
    fin.write(data)
    fin.close()

    # Init make build
    os.system("make init")
