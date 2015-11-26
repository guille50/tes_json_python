# -*- coding: utf-8 -*-
# requirements: python 3.4, argparse

from re import split, match
from os.path import isfile
from os import rename
import json
import argparse


def clearFile(originFile, destinationFile):
    if isfile(originFile) is False:
        print("Invilid file source File")
        exit(1)
    newFile = open(destinationFile, 'w')
    newData = {}
    with open(originFile, "r",  encoding="utf8") as ins:
        for line in ins:
            tmpMatch = match('^.+".+$', line)        
            if tmpMatch  is not None:
                newLine = tmpMatch.string
                stringSplit = split('"', newLine)            
                newData[stringSplit[1]]= stringSplit[3]

    newFile.write(json.dumps(newData, ensure_ascii=False, indent=4, sort_keys=True))

def moveFiles(originFile, destinationFile):
    rename(originFile, destinationFile)


parser = argparse.ArgumentParser(description='Used to clear conflicted json files in git')
parser.add_argument('-s', '--source', metavar='s', action='store', required=True, help='Original conflicted file')
parser.add_argument('-d', '--destination', default= False, metavar='d', action='store', required=False, help='Destination of the cleaned file, if it is not supplied source file will be overwritten')
args = parser.parse_args()

if args.destination is False:
    args.destination = args.source+"~"
    clearFile(args.source, args.destination)
    moveFiles(args.destination, args.source)
    exit(0)
clearFile(args.source, args.destination)
exit(0)
