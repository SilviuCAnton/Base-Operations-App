'''
Created on Feb 8, 2019

Modul pentru operatiile aritmetice

@author: Silviu Anton
'''
from domain.entities import NumberInBase
from domain.exceptions import OperationError

class ArithmeticOperations:
    
    @staticmethod
    def addNumbersWithSameBase(number1, number2):
        '''
        Description: aduna doua numere ce au aceeasi baza - rezultatul tot in baza sursa
        
        In: 
            - number1 - primul numar
            - number2 - al doilea numar
        Out:
            - rezultatul adunarii celor 2 numere in baza sursa 
            
        Exceptions:
            - ridica OperationError daca numere nu au aceeasi baza
        '''
        transport = 0
        base = number1.getBase()
        
        if base != number2.getBase():
            raise OperationError("Numerele trebuie sa aiba aceeasi baza!!!")
        
        resultValue = ''
        number1Value = number1.getValue()
        number2Value = number2.getValue()
        
        #Cat timp avem de adunat cifre in ambele numere repetam
        while len(number1Value) > 0 and len(number2Value) > 0:
            #Aici verificam daca sunt cire mai mari decat 9 si tratam acest caz
            if ord(number1Value[-1]) < ord('A'):
                digit1 = int(number1Value[-1])
            else:
                digit1 = 10 + (ord(number1Value[-1]) - ord('A'))
                
            if ord(number2Value[-1]) < ord('A'):
                digit2 = int(number2Value[-1])
            else:
                digit2 = 10 + (ord(number2Value[-1]) - ord('A'))    
            
            #Calculam restul dupa formula
            remainder = (digit1 + digit2 + transport) % base
            
            #Tratam cazul cifrelor mai mari decat 9
            if remainder > 9:
                resultValue += chr(65 + (remainder - 10))
            else: resultValue += str(remainder)
            
            #Calculam transportul dupa formula
            transport = (digit1 + digit2 + transport) // base
            
            #Eliminam cifrele adunate
            number1Value = number1Value[:-1]
            number2Value = number2Value[:-1]
        
        #Aici tratam cazul in care au ramas cifre in primul numar    
        while len(number1Value) > 0:
            if ord(number1Value[-1]) < ord('A'):
                digit1 = int(number1Value[-1])
            else:
                digit1 = 10 + (ord(number1Value[-1]) - ord('A'))
                
            remainder = (digit1 + transport) % base
            
            if remainder > 9:
                resultValue += chr(65 + (remainder - 10))
            else: resultValue += str(remainder)

            transport = (digit1 + transport) // base
            number1Value = number1Value[:-1]
        
        #Aici tratam cazul in care au ramas cifre in al doilea numar    
        while len(number2Value) > 0:
            if ord(number2Value[-1]) < ord('A'):
                digit2 = int(number2Value[-1])
            else:
                digit2 = 10 + (ord(number2Value[-1]) - ord('A')) 
                
            remainder = (digit2 + transport) % base
            
            if remainder > 9:
                resultValue += chr(65 + (remainder - 10))
            else: resultValue += str(remainder)

            transport = (digit2 + transport) // base
            number2Value = number2Value[:-1]
                
        if transport > 0:
            if transport > 9:
                resultValue += chr(65 + (transport - 10))
            else: resultValue += str(transport)
        
        #Asiguram ordinea corecta a cifrelor in numar
        resultValue = resultValue[::-1]
            
        return NumberInBase(base, resultValue)
    
    @staticmethod
    def subtractNumbersWithSameBase(number1, number2):
        '''
        Description: scade doua numere ce au aceeasi baza - rezultatul tot in baza sursa (number1 - number2)
        
        In: 
            - number1 - primul numar (descazutul)
            - number2 - al doilea numar (scazatorul)
        Out:
            - rezultatul scaderii celor 2 numere in baza sursa 
            
        Exceptions:
            - ridica OperationError daca numere nu au aceeasi baza
        '''
        base = number1.getBase()
        number1Value = number1.getValue()
        number2Value = number2.getValue()
        transport = 0
        resultValue = ''   
        
        if base != number2.getBase():
            raise OperationError("Numerele trebuie sa aiba aceeasi baza!!!")     
        
        #Cat timp mai avem cifre in ambele numere de scazut repetam
        while len(number1Value) > 0 and len(number2Value) > 0:
            #Aici verificam daca sunt cire mai mari decat 9 si tratam acest caz
            if ord(number1Value[-1]) < ord('A'):
                digit1 = int(number1Value[-1])
            else:
                digit1 = 10 + (ord(number1Value[-1]) - ord('A'))
                
            if ord(number2Value[-1]) < ord('A'):
                digit2 = int(number2Value[-1])
            else:
                digit2 = 10 + (ord(number2Value[-1]) - ord('A'))    
            
            #Calculam cifra rezulatat si transportul dupa formula 
            if digit1 + transport >= digit2:
                if digit1 + transport < 0:
                    resultDigit = base + transport - digit2
                    transport = -1
                else:
                    resultDigit = digit1 + transport - digit2
                    transport = 0
            else:
                resultDigit = base + digit1 + transport - digit2
                transport = -1
            
            #Tratam cazul cifrelor mai mari decat 9
            if resultDigit > 9:
                resultValue += chr(65 + (resultDigit - 10))
            else: resultValue += str(resultDigit)    
            
            number1Value = number1Value[:-1]
            number2Value = number2Value[:-1]
        
        #Tratam cazul in care au mai ramas cifre in descazut    
        while len(number1Value) > 0:
            if ord(number1Value[-1]) < ord('A'):
                digit1 = int(number1Value[-1])
            else:
                digit1 = 10 + (ord(number1Value[-1]) - ord('A'))
            
            if digit1 + transport < 0:
                resultDigit = base + transport
                transport = -1  
            else:  
                resultDigit = digit1 + transport
                transport = 0
             
            if resultDigit > 9:
                resultValue += chr(65 + (resultDigit - 10))
            else: resultValue += str(resultDigit)
 
            number1Value = number1Value[:-1]
        
        #Asiguram ordinea corecta a cifrelor in numar
        resultValue = resultValue[::-1]
        
        #Eliminam cifrele de 0 din fata numarului
        while resultValue[0] == '0' and len(resultValue) > 1:
            resultValue = resultValue[1:]
        
        return NumberInBase(base, resultValue)
    
    @staticmethod
    def multiplyByDigit(number, digit):
        '''
        Description: inmulteste un numbar cu o cifra (in baza curenta)
        
        In:
            - number - factor1
            - digit - factor2 (cifra)
        Out:
            - rezultatul inmultirii (in baza sursa)
            
        Exceptions:
            - ridica OperationError daca numere nu au aceeasi baza
        '''
        transport = 0
        resultValue = ''
        numberValue = number.getValue()
        base = number.getBase()
        digitValue = digit.getValue()
        
        if base != digit.getBase():
            raise OperationError("Numerele trebuie sa aiba aceeasi baza!!!")
        
        #Cat timp mai avem cifre in numar repeta
        while len(numberValue) > 0:
            #Aici verificam daca sunt cire mai mari decat 9 si tratam acest caz
            if ord(numberValue[-1]) < ord('A'):
                valueToMultiply = int(numberValue[-1])
            else:
                valueToMultiply = 10 + (ord(numberValue[-1]) - ord('A'))
                
            if ord(digitValue) < ord('A'):
                digitIntValue = int(digitValue)
            else:
                digitIntValue = 10 + (ord(digitValue) - ord('A'))
            
            #Calculam cifra rezultat si transportul dupa formula     
            resultDigit = (valueToMultiply * digitIntValue + transport) % base
            transport = (valueToMultiply * digitIntValue + transport) // base
            
            #Tratam cazul cifrelor mai mari decat 9
            if resultDigit > 9:
                resultValue += chr(65 + (resultDigit - 10))
            else: resultValue += str(resultDigit)
               
            numberValue = numberValue[:-1]
        
        #Tratam cazul in care mai avem o cifra in transport
        if transport > 0:
            if transport > 9:
                resultValue += chr(65 + (transport - 10))
            else: resultValue += str(transport)
        
        #Asiguram ordinea corecta a cifrelor in numar
        resultValue = resultValue[::-1]
                
        return NumberInBase(base, resultValue)
        
    
    @staticmethod
    def divideByDigit(number, digit):
        '''
        Description: imparte un numbar la o cifra (in baza curenta)
        
        In:
            - number - deimpartitul
            - digit - impartitorul (cifra)
        Out:
            - catul si restul impartirii
            
        Exceptions:
            - ridica OperationError daca numere nu au aceeasi baza
        '''
        transport = 0
        resultValue = ''
        numberValue = number.getValue()
        base = number.getBase()
        initialLen = len(numberValue)
        digitValue = digit.getValue()
        
        if base != digit.getBase():
            raise OperationError("Numerele trebuie sa aiba aceeasi baza!!!")
        
        #Cat timp mai avem cifre in numar repeta
        while len(numberValue) > 0:
            #Aici verificam daca sunt cire mai mari decat 9 si tratam acest caz
            if ord(numberValue[0]) < ord('A'):
                valueToDivide = int(numberValue[0])
            else:
                valueToDivide = 10 + (ord(numberValue[0]) - ord('A'))
                
            if ord(digitValue) < ord('A'):
                digitIntValue = int(digitValue)
            else:
                digitIntValue = 10 + (ord(digitValue) - ord('A'))
            
            #Calculam cifra rezultat si transportul dupa formula      
            resultDigit = (transport * base + valueToDivide) // digitIntValue
            transport = (transport * base + valueToDivide) % digitIntValue
            
            #Tratam cazul in care prima cifra a rezultatului e 0 si nu o memoram
            if len(numberValue) == initialLen and resultDigit == 0:
                pass
            else:
                if resultDigit > 9:
                    resultValue += chr(65 + (resultDigit - 10))
                else: resultValue += str(resultDigit)
              
            numberValue = numberValue[1:]
            
        return NumberInBase(base, str(resultValue)), NumberInBase(base, str(transport))
