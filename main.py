#!/usr/bin/env python3

import subprocess

def Format():
    """Returns the functions inside the Formats a file given its structured
    description.
    """
    out = subprocess.run(['which', 'pip'], capture_output = True)
    print(out.stdout)

    BuildStructuralRepresentation()

def BuildStructuralRepresentation():
    """Executes the structural parsing of the file, i.e. splits it into
    UnwrappedLine's. Works with a text file of the following layout:
    LINE =
      NEWLINE |
      WHITESPACE int |
      TOKEN_INFO

    TOKEN_INFO =
      'TokenType (string) | TokenLength (int) | TokenText (string)'
    """

Format()
