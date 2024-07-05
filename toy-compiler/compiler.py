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
re_start = re.compile(r"^start")
re_end = re.compile(r"^end")
re_var = re.compile(r"^[a-zA-Z]+")
re_int = re.compile(r"^[0-9]+")
re_op  = re.compile(r"^\(")
re_cp  = re.compile(r"^\)")
re_comma = re.compile(r"^,")

PATTERNS = {
       "start"  : re_start,
       "end"    : re_end  ,
       "var"    : re_var  ,
       "int"    : re_int  ,
       "oparen" : re_op   ,
       "cparen" : re_cp   ,
       "comma"  : re_comma
       }


class tokenizer:
    
    src = ""

    def __init__(self, filename):
        sanitize(filename)
        with open(filename, 'r') as file:
            self.src = file.read()
    
    def which_token(self, word):
        for p in PATTERNS:
            match = PATTERNS[p].search(word)
            if match:
                return (match, p)
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
            
################
#### PARSER ####
################
'''
now that we've split the source file into a legitimate token stream,
we need to parse that token stream based on the rules of the woodpidgen language.
i.e., this is the part where the language syntax is verified against
the provided program.
'''

Function = namedtuple('Function', ['name', 'args', 'impl'])

class parser:
    tokens = []
    def __init__(self, tokens):
        self.tokens = tokens
    
    def parse_tokens(self):
        self.parse_function

    def parse_function(self):
        self.pop_token("start")
        fn_name = self.pop_token("var")
        fn_args = self.parse_args()
        fn_impl = self.parse_impl()
        self.pop_token("end")
        return Function(name=fn_name.value, args=[arg_token.value for arg_token in fn_args], impl=fn_impl.value)


    def parse_args(self):
        args = []
        self.pop_token("oparen")
        if self.tokens[0].type == "var":
            args.append(self.pop_token("var"))
        while self.tokens[0].type == "comma":
            self.pop_token("comma")
            args.append(self.pop_token("var"))
        self.pop_token("cparen")
        return args

    def parse_impl(self):
        return self.pop_token("int")

    def pop_token(self, etype):
        token = self.tokens[0]
        if token.type == etype:
            self.tokens = self.tokens[1:]
            return token
        else:
            raise AssertionError("unexpected token type: {}, expected: {}".format(token, etype))

            


### TESTER
t = tokenizer("main.wpidg")
tokens = t.tokenize()
print(tokens)
p = parser(tokens)

print("THE FUNCTION")
print(p.parse_function())

