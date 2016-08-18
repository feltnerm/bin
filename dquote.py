#!/usr/bin/env python3

from pprint import pprint
import os, os.path, re, sys
from tempfile import mkstemp
from shutil import move
from os import remove, close

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

FILE = "JSHINT_DQUOTE_YO"
LINES_TO_LINT = open(FILE, 'r').readlines()
REGEX = r"^(?P<filename>.*): line (?P<lineno>\d+)"

files = {}
for line in LINES_TO_LINT:
    match = re.match(REGEX, line)
    if match:
        groupdict = match.groupdict()
        filename, lineno = groupdict['filename'], int(groupdict['lineno'])
        if filename in files:
            files[filename].add(lineno)
        else:
            files[filename] = set([lineno])

(sort(files[file]) for file in files)

pprint(files)

total = sum([len(files[key]) for key in files])
print((colors.HEADER + "Total: %d " + colors.ENDC) % total)

for file in files:

    fd = open(os.path.normpath(file), 'r')
    file_lines = fd.readlines()
    for line in files[file]:
        s = colors.HEADER + "[%d] %s" + colors.ENDC
        print(s % (line, file))
        affected_line = file_lines[line-1]
        print(colors.FAIL + "- " + affected_line + colors.ENDC)
        fixed_line = affected_line.replace("'", '"')
        print(colors.OKGREEN + "+ " + fixed_line + colors.ENDC)

        answer = input("Look good? [Y/n]? ")
        #while answer.lower() not in ('y', 'n'):
        #    print("please answer...")
        #    answer = input("Look good? [Y/n]? ")

        if answer.lower() != 'n':
            file_lines[line-1] = fixed_line
    fd.close()

    answer = input("Save file? [Y/n]? ")
    #while answer.lower() not in ('y', 'n'):
    #    print("please answer...")
    #    answer = input("Look good? [Y/n]? ")

    if answer.lower() != 'n':
        fh, abs_path = mkstemp()
        new_file = open(abs_path, 'w')
        new_file.writelines(file_lines)
        new_file.close()
        close(fh)
        remove(file)
        move(abs_path, file)
        print(colors.OKBLUE + "Saved: " + file + colors.ENDC)
