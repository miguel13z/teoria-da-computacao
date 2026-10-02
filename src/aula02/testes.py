from automatos import afd_primeiro_igual_ultimo


cases = ['', 'ab', 'a', 'b', 'bb', 'aba', 'abbbbbbbba', 'aaaaaaaaaab']
for case in cases:
    resultado = afd_primeiro_igual_ultimo.accepts_input(case)
    print(f'Cadeia: {case}      -->     {resultado}')


string_teste = 'ababaa'
passos = list(afd_primeiro_igual_ultimo.read_input_stepwise(string_teste))
for i, estado in enumerate(passos):
    if i == 0:
        print(f'Estado inicial   -->     {estado}')
    else:
        print(f'Processando "{string_teste[i - 1]}"     -->     {estado}')

