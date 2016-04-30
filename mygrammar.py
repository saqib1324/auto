import myproj
import ply.lex as lex
import ply.yacc as yacc

start = 'expres'
tokens = (
        'STRING',
        'newline',
        'tab',
        'space',
        'arrayeach',
        'puts',
        'tag',
        'endingtag',
        'identifier',
        'number',
        'EQUAL',
        'operator',
        'leftbrace',
        'rightbrace',
        'COMMA'
        
)

### STARTING 
def p_starting(p):
    'expres : a b iterator'
    p[0] = ("start", p[1], p[2], p[3])
###### FIRST LINE (i=2) 
def p_assignment(p):
    'a : identifier EQUAL number'
    p[0] = ("assign", p[1], p[3])
###### SECOND LINE (arr=[1,2]) 
def p_arrayassignment(p):
    'b : identifier EQUAL leftbrace optionalargs rightbrace'    #optionalargs= 1,2 or 1 or nothing
    p[0] = ("arr_assign", p[1], p[4])
def p_optionalargs(p):
    'optionalargs : args'
    p[0] = p[1]
def p_optionalargsempty(p):
    'optionalargs : '
    p[0] = []
def p_args(p):  # 1,
    'args : number COMMA args'
    p[0] = [p[1]] + p[3]
def p_argslast(p): # one argument
    'args : number'
    p[0] = [p[1]]
###### NEXT LINES 
def p_iterator(p):
    'iterator : fline lines'
    p[0] = p[1],p[2]
#### first line of array.each iterator 
def p_fline(p):
    'fline : arrayeach tag operator identifier operator'
    p[0] = ("fline",p[1],p[2])
#### remaining lines of array.each iterator
def p_lines(p):
    'lines : lines lines'
    p[0]=("lines",p[1],p[2])
## printing a string
def p_lines1(p):
    'lines : puts STRING'
    p[0] = ("PRINT",p[2])
## printing a number
def p_lines2(p):
    'lines : puts number'
    p[0] = ("PRINT",p[2])
## adding a number to tag
def p_addnum(p):
    'lines : identifier EQUAL identifier operator number'
    p[0] = p[1],p[5]
## adding a number to tag
def p_addnum1(p):
    'lines : identifier EQUAL number operator identifier'
    p[0] = p[1],p[5]
## adding two numbers to tag
def p_addnum2(p):
    'lines : identifier EQUAL number operator number'
    p[0] = p[1],p[3],p[5]
## adding two identifiers to tag
def p_addnum3(p):
    'lines : identifier EQUAL identifier operator identifier'
    p[0] = p[1],p[3],p[5]
def p_error(p):
    print "Syntax error in input!"
def fileread():
        with open('iterator.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data 
    
jslexer = lex.lex(module=myproj)
jsparser = yacc.yacc()
data=fileread()
jsast = jsparser.parse(data,lexer=jslexer)
print jsast