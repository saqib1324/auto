import ply.lex as lex

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

t_ignore                = ' \t\v\r\n' # shortcut for whitespace

def t_STRING(t):
        r'"[^"]*"'
        t.value = t.value[1:-1] # drop "surrounding quotes"
        return t

def t_newline(t):
        r'\n'
        return t
        
def t_tab(t):
        r'\s\s\s\s'
        return t

def t_space(t):
        r'\s'
        return t
        
def t_arrayeach(t):
        r'[A-Za-z][A-Za-z_]*\.each'
        return t

def t_puts(t):
        r'puts'
        return t
def t_tag(t):
        r'do'
        return t
def t_endingtag(t):
        r'end'
        return t

def t_identifier(t):
        r'[A-Za-z][A-Za-z_]*'
        return t
        
def t_number(t):
        r'[0-9]+'
        return t

def t_EQUAL(t):
        r'='
        return t

def t_operator(t):
        r'[<|>*/|==|=|!=|+|-]'
        return t

def t_leftbrace(t):
        r'\['
        return t
        
def t_rightbrace(t):
        r'\]'
        return t
 


def t_COMMA(t):
        r','
        return t



# def t_WORD(t):
#         r'[^ <>\n]+'
#         return t

        
def t_error(t):
        pass

def fileread():
        with open('iterator.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data
        
def main():
        data=fileread()
        print data
        iteratorlex = lex.lex()
        iteratorlex.input(data)
        while True:
                tok = iteratorlex.token()
                if not tok: break
                print tok
        

if __name__ == "__main__":
        main()
        