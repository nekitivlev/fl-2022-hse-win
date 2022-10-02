import ply.lex as lex
import sys

tokens = [
    'START',
    'NON_TERMINAL',
    'TERMINAL',
    'EPS',
    'EQUIV',
    'NEXT_TERM',
    'END_OF_LINE'
]


def clean(token_val):
    token_val = token_val.replace("\\$", "\$")
    return token_val


def clean_non_term(token_val):
    token_val = token_val.replace("\\$", "$")
    return clean(token_val)


def clean_term(token_val):
    token_val = token_val.replace("\\\&", "\&")
    return clean(token_val)

def find_row(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_START(t):
    r"start\ =\ \$([^$\$]*?(\$[^$]{1})*)*\$;"
    t.value = clean(t.value[9:-2])
    return t


def t_NON_TERMINAL(t):
    r'\$[^\\$]*((\\\$)?[^\\$]*)*\$'
    t.value = clean_non_term(t.value[1:-1])
    return t


def t_TERMINAL(t):
    r'\&[^\\&]*((\\\&)?[^\\&]*)*\&'
    t.value = clean_term(t.value[1:-1])
    return t


t_EQUIV = r'='
t_EPS = r'@'
t_NEXT_TERM = r'\|'
t_END_OF_LINE = r';'

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Unexpected character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)





def main():
    filename = sys.argv[1]
    lexer = lex.lex()
    with open(filename, "r") as filein, open(filename + ".out", "w") as fileout:
        lexer = lex.lex()
        lexer_input = "".join(filein.readlines())
        lexer.input(lexer_input)

        print(file=fileout)
        while True:
            tokens = lexer.token()
            if not tokens:
                break
            tokens.lexpos = find_row(lexer_input, tokens)
            print(tokens, file=fileout)


if __name__ == "__main__":
    main()