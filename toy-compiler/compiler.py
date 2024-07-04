#!/usr/bin/python3
## compiler for the woodpigeon programming language

import os
import re
from collections import namedtuple


SUPPORTED_EXT = [ ".wpidg", ".WPIDG"]
def sanitize(filename):
    ext = os.path.splitext(filename)[1]
    if ext not in SUPPORTED_EXT:
        raise AssertionError("extension {} not recognized. Supported types {}".format(ext, SUPPORTED_EXT))

Token = namedtuple('Token', ['type', 'value'])

class tokenizer:
    
    src = ""
    re_start = re.compile(r"^start")
    re_end = re.compile(r"^end")
    re_var = re.compile(r"^[a-zA-Z]+")
    re_int = re.compile(r"^[0-9]+")
    re_op  = re.compile(r"^\(")
    re_cp  = re.compile(r"^\)")
    re_comma = re.compile(r"^,")

    PATTERNS = [
        re_start,
        re_end  ,
        re_var  ,
        re_int  ,
        re_op   ,
        re_cp   ,
        re_comma
    ]

    TYPES = [
         "start", 
         "end",           
         "var",   
         "int",   
         "oparen",
        "cparen",
        "comma"
    ]
    

    def __init__(self, filename):
        sanitize(filename)
        with open(filename, 'r') as file:
            self.src = file.read()
    
    def which_token(self, word):
        for p in self.PATTERNS:
            match = p.search(word)
            if match:
                idx = self.PATTERNS.index(p)
                return (match, self.TYPES[idx])
        raise AssertionError("unexpected token:{}".format(word))


    def tokenize(self):
        tokens = []
        while self.src:
            self.src = self.src.strip()
            match = self.which_token(self.src)
            self.src = self.src[match[0].end():]
            tokens.append(Token(type=match[1], value=match[0].group(0)))
        #print(tokens)
        return tokens
            

        
        

t = tokenizer("main.wpidg")
tokens = t.tokenize()
print(tokens)
