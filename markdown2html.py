#!/usr/bin/python3
"""Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn't exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0"""

import sys
import os

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    markdown_file = sys.argv[1]
    output_name = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        exit(1)

    else:
        with open (output_name, "w") as htmlfile:
            with open(markdown_file, "r") as markdownfile:
                lines= markdownfile.readlines()
                for line in lines:
                    if line.startswith("######"):
                        htmlfile.write("<h6>" + line[7:-1] + "</h6>\n")
                        continue
                    if line.startswith("#####"):
                        htmlfile.write("<h5>" + line[6:-1] + "</h5>\n")
                        continue
                    if line.startswith("####"):
                        htmlfile.write("<h4>" + line[5:-1] + "</h4>\n")
                        continue
                    if line.startswith("###"):
                        htmlfile.write("<h3>" + line[4:-1] + "</h3>\n")
                        continue
                    if line.startswith("##"):
                        htmlfile.write("<h2>" + line[3:-1] + "</h2>\n")
                        continue
                    if line.startswith("#"):
                        htmlfile.write("<h1>" + line[2:-1] + "</h1>\n")
                        continue
