#!/usr/bin/env/python

import sys
import re

def fix_csv(name):
    with open(name, 'r', encoding='utf8') as f:
        s = f.read()
        if ';' in s:
            s = s.replace(',', '.')
            s = s.replace(';', ',')
        else:
            print(name, "is already fine")
            return
        with open(name, 'w', encoding='utf8') as ff:
            ff.write(s)
            ff.close()
    print(name, "is now a correct CSV")

def main():
    args = sys.argv[1:]
    if args == []:
        print("No file given")
        return
    else:
        for file in args:
            if bool(re.search(".csv$", file)):
                try:
                    fix_csv(file)
                except FileNotFoundError:
                    print("Oops!", file, "does not exist")
            else:
                print(file, "is not a valid CSV file")

main()