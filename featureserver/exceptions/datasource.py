'''
    Created on October 15, 2012
    
    @author: michel
    '''

from .core import BaseException

class ConnectionException(BaseException):
    
    message="Connection to the layer '%s' could not be established."
    
    def __init__(self, locator, layer, code="", message="", dump = ""):
        self.message = self.message % layer
        if len(message) > 0:
            self.message = message
        BaseException.__init__(self, self.message, code, locator, layer, dump)

class PredicateNotFoundException(BaseException):

    message = "'%s' is not a valide predicate."

    def __init__(self, locator, predicate, layer="", code="", message="", dump=""):
        self.message = self.message % predicate
        if len(message) > 0:
            self.message = message
        BaseException.__init__(self, self.message, code, locator, layer, dump)

