# import lex
import ply.lex as lex
# import lex

tokens = (
        # 'space',
        # 'tab',
        'newline',
        'tab',
        'space',
        # 'assignment',
        'arrayeach',
        'identifier',
        'number',
        'operator',
        'leftbrace',
        'rightbrace',
        
)

#t_ignore                = ' \t\v\r' # shortcut for whitespace

# def t_STRING(t):
#         r'"[^"]*"'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t
  

def t_newline(t):
        r'\n'
        return t
        
        
def t_tab(t):
        r'\s\s\s\s'
        return t

def t_space(t):
        r'\s'
        return t
        
        
# def t_assignment(t):
#         r'[A-Za-z][A-Za-z_]*\s=\s[0-9]+'
#         return t
        
def t_arrayeach(t):
        r'[A-Za-z][A-Za-z_]*\.each'
        return t
def t_identifier(t):
        r'[A-Za-z][A-Za-z_]*'
        return t
        
def t_number(t):
        r'[0-9]+'
        return t
        
def t_operator(t):
        r'[<|>|==|=|!=|+|-]'
        return t
        

        
# def t_braces(t):
#         # r'{[^{}]*}'
#         # r'"["]*"'
#         r'{[^{]*}'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t
def t_leftbrace(t):
        r'{'
        return t
def t_rightbrace(t):
        r'}'
        return t
  
# def t_EQUAL(t):
#         r'='
#         return t

# def t_STRING(t):
#         r'"[^"]*"'
#         # r'"["]*"'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t

# def t_WORD(t):
#         r'[^ <>\n]+'
#         return t

        
def t_error(t):
        pass

# text = "Hello \t<b>World</c>"

def fileread():
        # print 2
        with open('rubycode.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data
        
def main():
        # text = " i = 13  2 3abc\n \t"
        text=fileread()
        print text
        htmllex = lex.lex()
        htmllex.input(text)
        while True:
                tok = htmllex.token()
                if not tok: break
                print tok
        

if __name__ == "__main__":
        main()
        