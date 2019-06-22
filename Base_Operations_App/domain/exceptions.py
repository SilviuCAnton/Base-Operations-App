'''
Created on Feb 10, 2019

Modul pentru exceptii

@author: Silviu Anton
'''

#Aici am definit exceptii proprii pentru usurarea intelegerii cauzei exceptiei
class ConversionError(Exception):
    pass

class OperationError(Exception):
    pass

class BaseError(Exception):
    pass