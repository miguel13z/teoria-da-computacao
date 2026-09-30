from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


afn_substring_aba = NFA(
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

afd_convertido = DFA.from_nfa(afn_substring_aba)
