import sys
import ply.lex as lex

tokens = ('INT','FLOAT','INCLUDE','HEADER', 'NAME')
literals = "+(),;{}="
t_ignore  = ' \t'

t_INCLUDE = r'\#include'
t_HEADER = r'\<[a-zA-Z_/-]+.h>'
t_NAME = r'[a-zA-Z]+[0-9]*[a-zA-Z]*'

def t_INT(t):
    r'int'
    t.value = 'long'
    return t

def t_FLOAT(t):
    r'float'
    t.value = 'double'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python %s <input file>" % sys.argv[0])
    fp = open(sys.argv[1], "r")
    if (fp == 0):
        sys.exit("File not open: %s" % sys.argv[1])

    lexer = lex.lex()
    tmp = fp.readlines()
    fp.close()
    data = ""
    for i in tmp:
        data += i

    lexer.input(data)
    line = 1
    lexpos = 0
    prev = ''
    while True:
        tok = lexer.token()
        if not tok:
            break
        
        if line != tok.lineno:
            num = tok.lineno - line
            print("\n"*num,end='')
            line = tok.lineno
            lexpos += num
            prev = ''
        
        num = tok.lexpos - lexpos
        print(' '*num,end='')
        prev = str(tok.value)
        lexpos = tok.lexpos + len(prev)
        if tok.type == 'INT' or tok.type == 'FLOAT':
            lexpos-=1
        print(tok.value,end='')
        
