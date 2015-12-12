#!/usr/bin/env python
from ChemicalLexer import ChemicalLexer
from tree import ElementNode, GroupingNode

class ChemicalParser(object):
    '''
    Parser for chemical formulas. the
    output is a dict of elements in the formula
    and their quantities.
    '''
    def __init__(self, formula):
        '''
        Constructor

        formula -- the formula to parse
        '''
        self.lexer = ChemicalLexer(formula)
        self.formula = GroupingNode()
        self.group_stack = []

    def current_group(self):
        '''
        Get the current group, either from the stack
        or self.formula if the stack is empty
        '''
        try:
            return self.group_stack[-1]
        except IndexError:
            return self.formula

    def element(self, token):
        '''
        Add an element to the current group
        '''
        node = ElementNode(token.value)
        group = self.current_group()
        group.add(node)

    def quantity(self, token):
        '''
        Quantify the most recent group or element node
        added to the current group
        '''
        node = self.current_group().last()
        if node:
            node.quantity = int(token.value)
        else:
            raise Exception("Missing Atom before quantifier {}".format(token.value))

    def left_grouping(self, token):
        '''
        When a left grouping symbol is encountered,
        push a new subformula onto the stack
        '''
        node = GroupingNode(token.value)
        self.group_stack.append(node)

    def right_grouping(self, token):
        '''
        When a right grouping symbol is encountered, this subformula is complete.
        pop the current subformula off the stack and add it
        to the subformula that is the new top of the stack.
        '''
        group = self.current_group()
        if group.closing_symbol() == token.value:
            node = self.group_stack.pop()
            group = self.current_group()
            group.add(node)
        else:
            raise Exception("Missing Grouping Symbol {}".format(group.closing_symbol()))

    def parse(self):
        '''
        Run the lexer and parse each token.
        self.formula will then contain a GroupingNode tree that represents
        the whole formula

        returns self.formula.get_atoms_dict()
        '''
        for token in self.lexer.token_gen():
            if token.tag == 'ELEMENT':
                self.element(token)
            elif token.tag == 'QUANTITY':
                self.quantity(token)
            elif token.tag == 'LEFT_GROUPING':
                self.left_grouping(token)
            elif token.tag == 'RIGHT_GROUPING':
                self.right_grouping(token)
            else:
                raise Exception("Invalid Token!")
        if self.group_stack:
            raise Exception("Missing Grouping Symbol {}".format(self.current_group().closing_symbol()))
        return self.formula

if __name__ == '__main__':
    try:
        while True:
            formula = raw_input('formula> ')
            if formula.lower() in ['quit', 'exit']:
                raise KeyboardInterrupt
            try:
                parser = ChemicalParser(formula)
                formula = parser.parse()
                print "Chemical Composition of {}:".format(formula)
                print formula.get_atoms_dict()
            except Exception as e:
                print e
            print ''
    except KeyboardInterrupt:
        print "Bye."
