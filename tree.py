from dictutils import add_dicts, scale_dict

'''
Nodes for creating a parse tree for
chemical formulae.

ElementNodes are leaves in the tree
GroupingNodes are interior nodes, they have a list
    of children GroupingNodes or ElementNodes
'''

class ElementNode(object):
    '''
    Leaf node that represents some
    quantity of a single element (e.g. C, H4, O22)
    '''
    def __init__(self, element):
        '''
        Constructor

        element -- the element symbol as in the periodic table (e.g. T, Al)
        '''
        self.type = 'element'
        self.element = element
        self.quantity = 1

    def __str__(self):
        num = '' if self.quantity == 1 else self.quantity
        return "{}{}".format(self.element, num)

class GroupingNode(object):
    '''
    GroupingNode represents a single sub-formula
    in a chemical formula.
    '''
    def __init__(self, symbol = ''):
        '''
        Constructor

        symbol -- '', '(', '[', or '{'
            represents the left grouping symbol, this
            is used to match up the correct type of closing symbol.
            '' means this is the root GroupingNode and therefore does not
            have parentheses
        '''
        self.type = 'grouping'
        self.symbol = symbol
        self.quantity = 1
        self.children = []

    def add(self, node):
        '''
        Add a child node (ElementNode or GroupingNode)

        node -- the new child node
        '''
        self.children.append(node)

    def last(self):
        '''
        Get the last child node or None
        if there are no children.
        '''
        try:
            return self.children[-1]
        except IndexError:
            return None

    def add_quantity(self, quantity):
        '''
        Set the quantity for the last child node
        '''
        self.children[-1].quantity = quantity

    def closing_symbol(self):
        '''
        Get the matching grouping symbol for matching
        and display purposes.
        '''
        if self.symbol == '':
            return ''
        if self.symbol == '(':
            return ')'
        if self.symbol == '[':
            return ']'
        if self.symbol == '{':
            return '}'

    def get_atoms_dict(self):
        '''
        Get a dictionary of atoms and their quantitites by
        making an inorder traversal of the tree.
        '''
        atoms = {}
        for child in self.children:
            if child.type == 'element':
                atoms.setdefault(child.element, 0)
                atoms[child.element] += child.quantity * self.quantity
            elif child.type == 'grouping':
                child_atoms = child.get_atoms_dict()
                atoms = add_dicts(atoms, scale_dict(child_atoms, self.quantity))
        return atoms

    def __str__(self):
        '''
        Print the formula or subformula contained
        in this node and all child nodes
        '''
        num = '' if self.quantity == 1 else self.quantity
        return "{}{}{}{}".format(self.symbol, ''.join(str(child) for child in self.children), self.closing_symbol(), num)
