import re
from Token import Token

class ChemicalLexer(object):
    '''
    Lexer for chemical formulae
    '''
    TOKEN_TYPES = [
        (r'[A-Z][a-z]?', 'ELEMENT'),
        (r'[0-9]+',      'QUANTITY'),
        (r'\[|\(',    'LEFT_GROUPING'),
        (r'\]|\)',    'RIGHT_GROUPING'),
    ]
    def __init__(self, formula):
        '''
        Constructor

        formula -- chemical formula
        '''
        self.formula = formula
        self.pos = 0
        self.token_types = [(re.compile(pattern), tag) for pattern, tag in self.TOKEN_TYPES]

    def token_gen(self):
        '''
        Read through the formula and generate
        Tokens as a stream
        '''
        while self.pos < len(self.formula):
            error = True
            for regex, tag in self.token_types:
                match = regex.match(self.formula, self.pos)
                if match:
                    error = False
                    yield Token(tag, match.group(0))
                    self.pos = match.end(0)
                    break
                else:
                    continue
            if error:
                raise Exception('Syntax Error:\nInvallid token in input "{}"\nstarting at position {}: "{}"'.format(self.formula, self.pos, self.formula[self.pos:]))
