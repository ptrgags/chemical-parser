class Token(object):
    '''
    Simple token structure
    '''
    def __init__(self, tag, value):
        '''
        Constructor
        tag -- token type as a string
        value -- token value (any type, usually string)
        '''
        self.tag = tag
        self.value = value

    def __repr__(self):
        return "Token({}, {})".format(self.tag, self.value)

    def __str__(self):
        return "{}: {}".format(self.tag, self.value)
