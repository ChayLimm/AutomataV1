import pygraphviz as pgv
from collections import defaultdict
from itertools import combinations

class FiniteAutomaton:

    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state, start=False, accept=False):
        self.states.add(state)
        if start:
            self.start_state = state
        if accept:
            self.accept_states.add(state)

    def add_transition(self, from_state, to_state, symbol):
        if not from_state or not to_state or not symbol:
            print("Error: from_state, to_state, and symbol must all be non-null and non-empty.")
            return 

        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        if symbol not in self.transitions[from_state]:
            self.transitions[from_state][symbol] = set()
        self.transitions[from_state][symbol].add(to_state)
        self.alphabet.add(symbol)

    def to_graph(self, filename):
        graph = pgv.AGraph(directed=True)
        for state in self.states:
            if state in self.accept_states:
                graph.add_node(state, shape='doublecircle')
            else:
                graph.add_node(state)
        for from_state, paths in self.transitions.items():
            for symbol, to_states in paths.items():
                for to_state in to_states:
                    graph.add_edge(from_state, to_state, label=symbol)
        if self.start_state:
            graph.add_node('start', shape='plaintext', label='')
            graph.add_edge('start', self.start_state)
        graph.layout(prog='dot')
        graph.draw(filename)

    def is_deterministic(self):
        for state, transitions in self.transitions.items():
            for symbol in transitions:
                if len(transitions[symbol]) > 1:
                    return False
        return True

    def accepts_string(self, string):
        current_states = {self.start_state}
        for symbol in string:
            next_states = set()
            for state in current_states:
                if state in self.transitions and symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states
        return bool(current_states & self.accept_states)

    def nfa_to_dfa(self):
        dfa = FiniteAutomaton()
        start_state = frozenset([self.start_state])
        states_map = {start_state: 'q0'}
        dfa.add_state('q0', start=True)
        queue = [start_state]
        new_state_counter = 1
        
        while queue:
            current = queue.pop(0)
            current_label = states_map[current]
            for symbol in self.alphabet:
                next_states = set()
                for state in current:
                    if state in self.transitions and symbol in self.transitions[state]:
                        next_states.update(self.transitions[state][symbol])
                if not next_states:
                    continue
                next_state_frozen = frozenset(next_states)
                if next_state_frozen not in states_map:
                    new_state_label = f'q{new_state_counter}'
                    states_map[next_state_frozen] = new_state_label
                    dfa.add_state(new_state_label, accept=bool(next_states & self.accept_states))
                    new_state_counter += 1
                    queue.append(next_state_frozen)
                dfa.add_transition(current_label, states_map[next_state_frozen], symbol)
        
        return dfa

    def minimize_dfa(self):
        # Initial partition
        P = [self.accept_states, self.states - self.accept_states]
        W = [self.accept_states.copy()]
        
        while W:
            A = W.pop()
            for symbol in self.alphabet:
                X = {state for state in self.states if state in self.transitions and symbol in self.transitions[state] and self.transitions[state][symbol] & A}
                new_P = []
                for Y in P:
                    intersection = X & Y
                    difference = Y - X
                    if intersection and difference:
                        new_P.append(intersection)
                        new_P.append(difference)
                        if Y in W:
                            W.remove(Y)
                            W.append(intersection)
                            W.append(difference)
                        else:
                            W.append(intersection if len(intersection) <= len(difference) else difference)
                    else:
                        new_P.append(Y)
                P = new_P
        
        minimized_dfa = FiniteAutomaton()
        state_map = {}
        for i, block in enumerate(P):
            state_name = f'q{i}'
            for state in block:
                state_map[state] = state_name
            minimized_dfa.add_state(state_name, start=bool(self.start_state in block), accept=bool(block & self.accept_states))
        
        for state in self.states:
            if state in self.transitions:
                for symbol, next_states in self.transitions[state].items():
                    for next_state in next_states:
                        minimized_dfa.add_transition(state_map[state], state_map[next_state], symbol)
        
        return minimized_dfa

# #A Example usage:
# fa = FiniteAutomaton()
# fa.add_state('q0', start=True)
# fa.add_state('q1', accept=True)
# fa.add_transition('q0', 'q1', 'a/b')
# fa.add_transition('q1', 'q0', '')
# fa.to_graph('finite_automaton.png')

# print(fa.is_deterministic())  #B Example usage

# print(fa.accepts_string('ab'))  #C Example usage
# print(fa.accepts_string('aa'))  #D Example usage

# dfa = fa.nfa_to_dfa()
# dfa.to_graph('dfa.png')

# min_dfa = dfa.minimize_dfa() #e Example usage
# min_dfa.to_graph('minimized_dfa.png')