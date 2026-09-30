from automatos import afn_substring_aba, afd_convertido


def testes_validacao():
    testes_afn = ['a', 'b', 'ab', 'abb', 'aba', 'aaaaabbbbbbabbbbbbaaabaaaaaa', 'abababbbabaaaaaaabaababb', 'abcdaba', 'aaaabbbbbabaaaa', '']

    print("\n--- Testes de Aceitação ---")
    for case in testes_afn:
        resultado_afd = afd_convertido.accepts_input(case)
        resultado_afn = afn_substring_aba.accepts_input(case)

        print(f'Cadeia: {case}  -->  AFN: {resultado_afn} | AFD: {resultado_afd}')

def main():
    testes_validacao()


main()
