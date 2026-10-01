from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# AFN que reconhece cadeias sobre  Σ={a,b}  que contenham a substring 'aba'
def build_afn_substring_aba():
    return NFA(
        states={'q0', 'q1', 'q2', 'q3'},
        input_symbols={'a', 'b'},
        transitions={
            'q0' : {'a' : {'q0', 'q1'}, 'b' : {'q0'}},
            'q1' : {'b' : {'q2'}},
            'q2' : {'a' : {'q3'}},
            'q3' : {'a' : {'q3'}, 'b' : {'q3'}},
        },
        initial_state='q0',
        final_states={'q3'},
    )

# Linguagem  L1  sobre  Σ={0,1} : Cadeias que possuem um número par de zeros
def build_afd_par_zeros():
    return DFA(
        states={'Qp', 'Qi'},
        input_symbols={'0', '1'},
        transitions={
            'Qp' : {'1' : 'Qp', '0' : 'Qi'},
            'Qi' : {'1' : 'Qi', '0' : 'Qp'},
        },
        initial_state='Qp',
        final_states={'Qp'},
    )

# Linguagem  L2  sobre  Σ={0,1} : Cadeias que terminam com o sufixo 01
def build_afd_sufixo_01():
    return DFA.from_suffix(
        input_symbols={'0', '1'},
        suffix='01',
    )
