#!/usr/bin/env/python

import sys
import re

def fix_csv(name):
    with open(name, 'r') as f:
        s = f.read().replace(',', '.')
        s = s.replace(';', ',')
        with open(name, 'w') as ff:
            ff.write(s)
            ff.close()

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
                    print("done")
                except FileNotFoundError:
                    print("Oops!", file, "does not exist")
            else:
                print(file, "is not a valid csv file")

main()