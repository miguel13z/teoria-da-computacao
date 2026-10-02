from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.fa.gnfa import GNFA

#Sobre  Σ={a,b} , construa um AFD que aceite cadeias de comprimento  ≥1  cujo primeiro símbolo seja estritamente igual ao último.
afd_primeiro_igual_ultimo = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0':   {'a': 'q1', 'b': 'q3'},
        'q1':   {'a': 'q1', 'b': 'q2'},
        'q2':   {'a': 'q1', 'b': 'q2'},
        'q3':   {'a': 'q4', 'b': 'q3'},
        'q4':   {'a': 'q4', 'b': 'q3'},
    },
    final_states={'q1', 'q3'},
    initial_state='q0'
)