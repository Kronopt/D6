#!python2
# coding: utf-8

"""
INSTALL DEPENDENCIES
Installs module dependencies for D6_ui.pyw

HOW TO RUN:
    - Directly, by double clicking the script.
"""

import subprocess
import sys

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '1.0'
__date__ = '16:08h, 19/04/2017'


def install_dependencies():
    dependencies = ["kivy", "kivy.deps.glew", "kivy.deps.sdl2"]
    python_exe = sys.executable  # location of python executable, avoids dependency on windows PATH

    try:
        # check if pip is installed
        subprocess.check_output([python_exe, "-m", "pip", "--version"])

    except subprocess.CalledProcessError:
        print
        print "Pip is the recommended tool for installing Python packages, and usually comes bundled with python."
        print "Without pip, dependencies are much harder to install..."
        print
        raw_input("Press any key to exit")
        sys.exit()

    print "Installing dependencies for D6_ui.pyw"

    # Install dependencies
    subprocess.call([python_exe, "-m", "pip", "install"] + dependencies)

    print
    raw_input("Press any key to exit")

if __name__ == '__main__':
    install_dependencies()
