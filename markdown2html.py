#!/usr/bin/python3

import sys
import os

if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    markdown_file = sys.argv[1]
    output_name = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        exit(1)

    else:
        exit(0)
