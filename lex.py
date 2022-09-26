import ply.lex as lex
import sys

# 1 + 2 * x123 + if x then 31 else 42

reserved = {
  'if': 'IF',
  'then': 'THEN',
  'else': 'ELSE'
}

tokens = [
  'NUM',
  'PLUS',
  'MINUS',
  'MULT',
  'DIV',
  'POW',
  'ID',
  'LBR',
  'RBR'
] + list(reserved.values())

def t_ID(t):
  r'[a-z_][a-z_0-9]*'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_POW = r'\*\*'
t_LBR = r'\('
t_RBR = r'\)'

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

def main():
  lexer = lex.lex()
  lexer.input(sys.argv[1])

  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok)

if __name__ == "__main__":
    main()