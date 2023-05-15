import string

sentence = input()
input_string = sentence.lower() + '#'

alphabet_list = list(string.ascii_lowercase)
state_list = ['start',
              'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
              'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12',
              's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12'
              ]

trans_tab = {}

for state in state_list:
  for alphabet in alphabet_list:
    trans_tab[(state, alphabet)] = 'error'
  trans_tab[(state, '#')] = 'error'
  trans_tab[(state, ' ')] = 'error'

trans_tab[('start', ' ')] = 'start'


#atuk
trans_tab[('start', 'a')] = 'q1'
trans_tab[('q1', 't')] = 'q2'
trans_tab[('q2', 'u')] = 'q3'
trans_tab[('q3', 'k')] = 's12'
trans_tab[('s12', ' ')] = 'r0'
trans_tab[('s12', '#')] = 'accept'

#akak
trans_tab[('start', 'a')] = 'q1'
trans_tab[('q1', 'k')] = 'q4'
trans_tab[('q4', 'a')] = 'q5'
trans_tab[('q5', 'k')] = 's12'

#kamek
trans_tab[('start', 'k')] = 'q6'
trans_tab[('q6', 'a')] = 'q7'
trans_tab[('q7', 'm')] = 'q8'
trans_tab[('q8', 'e')] = 'q9'
trans_tab[('q9', 'k')] = 's12'

#bace
trans_tab[('start', 'b')] = 'r1'
trans_tab[('r1', 'a')] = 'r2'
trans_tab[('r2', 'c')] = 'r3'
trans_tab[('r3', 'e')] = 's12'

#sudu
trans_tab[('start', 's')] = 'r4'
trans_tab[('r4', 'u')] = 'r5'
trans_tab[('r5', 'd')] = 'r6'
trans_tab[('r6', 'u')] = 's12'

#memandu
trans_tab[('start', 'm')] = 'r7'
trans_tab[('r7', 'e')] = 'r8'
trans_tab[('r8', 'm')] = 'r9'
trans_tab[('r9', 'a')] = 'r10'
trans_tab[('r10', 'n')] = 'r11'
trans_tab[('r11', 'd')] = 'r12'
trans_tab[('r12', 'u')] = 's12'

#buku
trans_tab[('start', 'b')] = 's1'
trans_tab[('s1', 'u')] = 's2'
trans_tab[('s2', 'k')] = 's3'
trans_tab[('s3', 'u')] = 's12'

#nasi
trans_tab[('start', 'n')] = 's4'
trans_tab[('s4', 'a')] = 's5'
trans_tab[('s5', 's')] = 's6'
trans_tab[('s6', 'i')] = 's12'

#gule
trans_tab[('start', 'g')] = 's7'
trans_tab[('s7', 'u')] = 's8'
trans_tab[('s8', 'l')] = 's9'
trans_tab[('s9', 'e')] = 's12'

#oto
trans_tab[('start', 'o')] = 's10'
trans_tab[('s10', 't')] = 's11'
trans_tab[('s11', 'o')] = 's12'

#transition for new token
trans_tab[('r0', ' ')] = 'r0'
trans_tab[('r0', 'a')] = 'q1'
trans_tab[('r0', 'k')] = 'r6'
trans_tab[('r0', 'b')] = 'r1'
trans_tab[('r0', 's')] = 'r4'
trans_tab[('r0', 'm')] = 'r7'
trans_tab[('r0', 'b')] = 's1'
trans_tab[('r0', 'n')] = 's4'
trans_tab[('r0', 'g')] = 's7'
trans_tab[('r0', 'o')] = 's10'
trans_tab[('r0', '#')] = 'accept'

#lexical analysis
idx_char = 0
state = 'start'
current_token = ''

while state != 'accept':
  current_char = input_string[idx_char]
  current_token += current_char
  
  state = trans_tab[(state, current_char)]
  if state == 's12' or state == 'r0' and current_char != ' ':
    print('current token: ', current_token, 'is valid')
    current_token = ''
  elif state == 'error':
    print('current token: ', current_token, 'is not valid')
    break
  idx_char += 1

if state == 'accept':
  print('all tokens in the following sentence: \"', sentence, '\" is valid')
else:
  print('all tokens in the following sentence: \"', sentence, '\" is not valid')

# PARSING PROCESS
print('\n')
token = sentence.lower().split()
token.append('EOS')

#symbols definition
non_terminals = ['S', 'N', 'V', 'O']
terminals = ['atuk', 'akak', 'kamek', 
        'bace', 'sudu', 'memandu', 'buku', 
        'nasi', 'gule', 'oto']

#parse table definition
parse_table = {}

parse_table[('S', 'atuk')] = ['N', 'V', 'O']
parse_table[('S', 'akak')] = ['N', 'V', 'O']
parse_table[('S', 'kamek')] = ['N', 'V', 'O']
parse_table[('S', 'bace')] = ['error']
parse_table[('S', 'sudu')] = ['error']
parse_table[('S', 'memandu')] = ['error']
parse_table[('S', 'buku')] = ['error']
parse_table[('S', 'nasi')] = ['error']
parse_table[('S', 'gule')] = ['error']
parse_table[('S', 'oto')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('N', 'atuk')] = ['atuk']
parse_table[('N', 'akak')] = ['akak']
parse_table[('N', 'kamek')] = ['kamek']
parse_table[('N', 'bace')] = ['error']
parse_table[('N', 'sudu')] = ['error']
parse_table[('N', 'memandu')] = ['error']
parse_table[('N', 'buku')] = ['error']
parse_table[('N', 'nasi')] = ['error']
parse_table[('N', 'gule')] = ['error']
parse_table[('N', 'oto')] = ['error']
parse_table[('N', 'EOS')] = ['error']

parse_table[('V', 'atuk')] = ['error']
parse_table[('V', 'akak')] = ['error']
parse_table[('V', 'kamek')] = ['error']
parse_table[('V', 'bace')] = ['bace']
parse_table[('V', 'sudu')] = ['sudu']
parse_table[('V', 'memandu')] = ['memandu']
parse_table[('V', 'buku')] = ['error']
parse_table[('V', 'nasi')] = ['error']
parse_table[('V', 'gule')] = ['error']
parse_table[('V', 'oto')] = ['error']
parse_table[('V', 'EOS')] = ['error']

parse_table[('O', 'atuk')] = ['error']
parse_table[('O', 'akak')] = ['error']
parse_table[('O', 'kamek')] = ['error']
parse_table[('O', 'bace')] = ['error']
parse_table[('O', 'sudu')] = ['error']
parse_table[('O', 'memandu')] = ['error']
parse_table[('O', 'buku')] = ['nasi']
parse_table[('O', 'nasi')] = ['nasi']
parse_table[('O', 'gule')] = ['gule']
parse_table[('O', 'oto')] = ['oto']
parse_table[('O', 'EOS')] = ['oto']


stack = []
stack.append('#')
stack.append('S')

#input reading initialization
idx = 0
symbol = token[idx]

#parsing process
while (len(stack) > 0 and state == 'accept'):
    top = stack[len(stack) - 1]
    print('Top = ', top)
    print('Symbol = ', symbol)
    if top in terminals:
        print('Top stack is a terminal symbol')
        if top == symbol:
            stack.pop()
            idx += 1
            symbol = token[idx]
            if symbol == 'EOS':
                print('Stack: ', stack)
                stack.pop()
        else:
            print('error')
            break
    elif top in non_terminals:
        print('Top stack is a non terminal symbol')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            pushed_symbol = parse_table[(top, symbol)]
            for j in range(len(pushed_symbol)-1,-1,-1):
                stack.append(pushed_symbol[j])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('Stack elements = ', stack)
    print()

#conclusion
print()
if symbol == 'EOS' and len(stack) == 0 and state == 'accept':
    print('Input string = ', sentence, 'accepted, gramatically correct')
else:
    print('Error. Input string = ', sentence, 'rejected, gramatically incorrect')