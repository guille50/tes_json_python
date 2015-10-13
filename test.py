#!/usr/bin/python3.4
from re import match, sub
import string
import json

new_file = open('new_file', 'w')
new_dic = {}
with open("json1.json", "r") as ins:
    for line in ins:
        new_match = match('^.+".+$', line)
        if new_match  is not None:
            new_line  =  sub('(\s+|\,$|")','', new_match.string)            
            tmp_line = new_line.split(":")
            new_dic[tmp_line[0]]= tmp_line[1]            

new_file.write(json.dumps(new_dic, ensure_ascii=False, indent=4, sort_keys=True))

            
        