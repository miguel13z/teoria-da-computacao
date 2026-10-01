from automatos import *


def testes_substring_aba():
    afn_substring_aba = build_afn_substring_aba()
    afd_convertido = DFA.from_nfa(afn_substring_aba)

    testes_afn = ['a', 'b', 'ab', 'abb', 'aba', 'aaaaabbbbbbabbbbbbaaabaaaaaa', 'abababbbabaaaaaaabaababb', 'abcdaba', 'aaaabbbbbabaaaa', '']

    print("\n--- Testes de Aceitação ---")
    for case in testes_afn:
        resultado_afd = afd_convertido.accepts_input(case)
        resultado_afn = afn_substring_aba.accepts_input(case)

        print(f'Cadeia: {case}  -->  AFN: {resultado_afn} | AFD: {resultado_afd}')

def testes_par_zero():
    afd_par_zeros = build_afd_par_zeros()

    cases = ['', '1', '111111', '010', '00', '0', '0111111110', '0111111', '00000000011']

    for case in cases:
        resultado = afd_par_zeros.accepts_input(case)
        print(f'String: {case}  -->  {resultado}')

def testes_sufixo_01():
    afd_sufixo_01 = build_afd_sufixo_01()

    cases = ['', '1', '01', '1111101', '000000000', '1110', '010101', '0101011']

    for case in cases:
        resultado = afd_sufixo_01.accepts_input(case)
        print(f'String: {case}  -->  {resultado}')

def main():
    testes_substring_aba()
    #testes_par_zero()
    #testes_sufixo_01()


main()
