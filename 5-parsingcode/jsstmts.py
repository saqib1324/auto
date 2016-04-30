import ply.yacc as yacc
import ply.lex as lex
import jstokens # use our JavaScript lexer
#from jstokens import tokens # use our JavaScript tokens
start = 'js' # the start symbol in our grammar
precedence = (
        ('left', 'OROR'),
        ('left', 'ANDAND'),
        ('left', 'EQUALEQUAL'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'NOT'),
)

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
        'IDENTIFIER',   # factorial
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       # 1234 5.678
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       # "this is a \"tricky\" string"
        'TIMES',        # *
        'TRUE',         # TRUE
        'VAR',          # var
)

def p_js(p):
    'js : element js'
    p[0] = [p[1]] + p[2]
def p_js_empty(p):
    'js : '
    p[0] = [ ]
def p_element_function(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('function', p[2], p[4], p[6])
def p_element_statement(p):
    'element : stmt SEMICOLON'
    p[0] = ('stmt', p[1])
def p_optparams(p):
    'optparams : params'
    p[0] = p[1]
def p_optparams_empty(p):
    'optparams : '
    p[0] = []
def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [ p[1] ] + p[3]
def p_params_last(p):
    'params : IDENTIFIER'
    p[0] = [ p[1] ]
def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]
def p_statements(p):
    'statements : stmt SEMICOLON statements'
    p[0] = [ p[1] ] + p[3]
def p_statements_empty(p):
    'statements : '
    p[0] = []
def p_stmt_if_then(p):
    'stmt : IF exp compoundstmt'
    p[0] = ('if-then', p[2], p[3])
def p_stmt_if_then_else(p):
    'stmt : IF exp compoundstmt ELSE compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])
def p_stmt_assignment(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ('assign', p[1], p[3])
def p_stmt_return(p):
    'stmt : RETURN exp'
    p[0] = ('return', p[2])
def p_stmt_var(p):
    'stmt : VAR IDENTIFIER EQUAL exp'
    p[0] = ('var', p[2], p[4])
def p_stmt_exp(p):
    'stmt : exp'
    p[0] = ('exp', p[1])
# For now, we will assume that there is only one type of expression.
def p_exp_identifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1])
jslexer = lex.lex(module=jstokens)
jsparser = yacc.yacc()
input_string = "x=5"
jslexer.input(input_string)
parse_tree = jsparser.parse(input_string,lexer=jslexer)
print parse_tree
