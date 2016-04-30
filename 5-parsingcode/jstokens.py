import ply.lex as lex

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### Not used in this problem.
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

#
# Write your code here.
#


states = ( ( 'javascripteolcomment', 'exclusive'),  ('javascriptdelimitedcomment', 'exclusive'), )

def t_javascripteolcomment(t):
    r'//'
    t.lexer.begin('javascripteolcomment')

def t_javascripteolcomment_end(t):
    r'\n'
    t.lexer.begin('INITIAL')


def t_javascriptdelimitedcomment(t):
  r'/\*'
  t.lexer.begin('javascriptdelimitedcomment')

def t_javascriptdelimitedcomment_end(t):
  r'\*/'
  t.lexer.begin('INITIAL')

t_javascriptdelimitedcomment_ignore = r'.'
t_javascripteolcomment_ignore  = r'.'

def t_javascripteolcomment_error(t):
  t.lexer.skip(1)

def t_javascriptdelimitedcomment_error(t):
  t.lexer.skip(1)

t_ANDAND =  r'&&'
t_COMMA =  r','
t_DIVIDE =  r'/'
t_ELSE =  r'else'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_FALSE =  r'false'
t_FUNCTION = r'function'
t_GE =  r'>='
t_GT =   r'>'
t_IF =  r'if'
t_LBRACE = r'\{'
t_LE =  r'<='
t_LPAREN =   r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE =  r'\}'
t_RETURN = r'return'
t_RPAREN =  r'\)'
t_SEMICOLON =   r';'
t_TIMES = r'\*'
t_TRUE =  r'true'
t_VAR =   r'var'

t_ignore = ' \t\v\r' # whitespace

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)


def t_IDENTIFIER(token):
        r'[A-Za-z][A-Za-z_]*'
        return token
def t_NUMBER(token):
        r'-?[0-9]+(?:\.[0-9]*)?'
        token.value = float(token.value)
        return token
def t_STRING(token):
        r'"(?:[^?\\]|(?:\\.))*"'
        token.value = token.value[1:-1]
        return token

