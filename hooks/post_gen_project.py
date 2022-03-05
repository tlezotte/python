#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run_make(target):
    """Initialize a new project

    Args:
        target (string): name of make target to run
    """
    os.system("make " + target)


if __name__ == '__main__': 
    run_make("init")
