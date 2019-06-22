'''
Created on Feb 8, 2019

Service pentru operatiile cu numere reprezentate in diferita baze

@author: Silviu Anton
'''
from utils.conversions import Conversion
from utils.arithmetics import ArithmeticOperations
from domain.exceptions import ConversionError, BaseError

class BaseOperationsService:
    
    @staticmethod
    def convertNumberThroughBase10(number, baseToConvertTo):
        '''
        Description: converteste un numar intr-o alta baza prin baza intermediara 10
        
        In:
            - number - numarul dat
            - baseToConvertTo - baza in care il convertim 
        Out:
            - resultNumber - numarul rezultat in baza dorita
        
        Exceptions:
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number.getValue():
            if ord(digit) >= ord(chr(65 + number.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number.getBase()))
        
        numberInBase10 = Conversion.convertBySubstitution(number, 10)
        resultNumber = Conversion.convertByDivision(numberInBase10, baseToConvertTo)
        
        return resultNumber
    
    @staticmethod
    def convertToGreaterBase(number, baseToConvertTo):
        '''
        Description: converteste un numar intr-o alta baza, mai mare, prin metoda substitutiei
        
        In:
            - number - numarul dat
            - baseToConvertTo - baza in care il convertim 
        Out:
            - resultNumber - numarul rezultat in baza dorita
            
        Exceptions:
            - ridica ConversionError daca baza e mai mica decat cea a numarului
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number.getValue():
            if ord(digit) >= ord(chr(65 + number.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number.getBase()))
        
        if number.getBase() > baseToConvertTo:
            raise ConversionError("Baza la care doriti sa convertiti este mai mica!!!")
        return Conversion.convertBySubstitution(number, baseToConvertTo)
        
    @staticmethod
    def convertToLowerBase(number, baseToConvertTo):
        '''
        Description: converteste un numar intr-o alta baza, mai mica, prin metoda impartirilor repetate
        
        In:
            - number - numarul dat
            - baseToConvertTo - baza in care il convertim 
        Out:
            - resultNumber - numarul rezultat in baza dorita
        
        Exceptions:
            - ridica ConversionError daca baza e mai mare decat cea a numarului
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number.getValue():
            if ord(digit) >= ord(chr(65 + number.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number.getBase()))
        
        if number.getBase() < baseToConvertTo:
            raise ConversionError("Baza la care doriti sa convertiti este mai mare!!!")
        return Conversion.convertByDivision(number, baseToConvertTo)
    
    @staticmethod
    def fastConvertion(number, baseToConvertTo):
        '''
        Description: conversie rapida intre bazele 2, 4, 8, 16
        
        In:
            - number - numarul de convertit
            - baseToConvertTo - baza in care va fi convertit numarul
        Out:
            - resultNumber - numarul convertit in baza dorita
        
        Exceptions:
            - ridica ConversionError daca bazele nu sunt 2, 4, 8 asu 16
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number.getValue():
            if ord(digit) >= ord(chr(65 + number.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number.getBase()))
        
        if number.getBase() not in [2, 4, 8, 16] or baseToConvertTo not in [2, 4, 8, 16]:
            raise ConversionError("Bazele trebuie sa fie 2, 4, 8 sau 16!!!")
        
        if number.getBase() == 2:
            resultNumber = Conversion.convertFrom2(number, baseToConvertTo)
        elif baseToConvertTo == 2:
            resultNumber = Conversion.convertTo2(number)
        else:
            resultNumber = Conversion.convertTo2(number)
            resultNumber = Conversion.convertFrom2(resultNumber, baseToConvertTo)
        
        return resultNumber
    
    @staticmethod
    def addNumbers(number1, number2, resultBase):
        '''
        Description: aduna 2 numere reprezentate in orice baza si returneaza rezultatul in baza indicata
        
        In:
            - number1 - primul numar
            - number2 - al doilea numar
            - resultBase - baza in care va fi reprezentat rezultatul 
        Out:
            - suma celor 2 numere, in baza indicata
            
        Exceptions:
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number1.getValue():
            if ord(digit) >= ord(chr(65 + number1.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number1.getBase()))
            
        for digit in number2.getValue():
            if ord(digit) >= ord(chr(65 + number2.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number2.getBase()))
        
        if number1.getBase() in [2, 4, 8, 16] and resultBase in [2, 4, 8, 16]:
            number1 = BaseOperationsService.fastConvertion(number1, resultBase)
        elif number1.getBase() == 10:
            number1 = BaseOperationsService.convertNumberThroughBase10(number1, resultBase)
        elif number1.getBase() < resultBase:
            number1 = BaseOperationsService.convertToGreaterBase(number1, resultBase)
        else: 
            number1 = BaseOperationsService.convertToLowerBase(number1, resultBase)
            
        if number2.getBase() in [2, 4, 8, 16] and resultBase in [2, 4, 8, 16]:
            number2 = BaseOperationsService.fastConvertion(number2, resultBase)
        elif number2.getBase() == 10:
            number2 = BaseOperationsService.convertNumberThroughBase10(number2, resultBase)
        elif number2.getBase() < resultBase:
            number2 = BaseOperationsService.convertToGreaterBase(number2, resultBase)
        else: 
            number2 = BaseOperationsService.convertToLowerBase(number2, resultBase)
            
        return ArithmeticOperations.addNumbersWithSameBase(number1, number2)
    
    @staticmethod
    def subtractNumbers(number1, number2, resultBase):
        '''
        Description: scade 2 numere reprezentate in orice baza si returneaza rezultatul in baza indicata
        
        In:
            - number1 - descazutul
            - number2 - scazatorul
            - resultBase - baza in care va fi reprezentat rezultatul
            
        Out:
            - diferenta celor 2 numere, in baza indicata
            
        Exceptions:
            - ridica BaseError daca numarul nu este reprezentat corect in baza introdusa
        '''
        for digit in number1.getValue():
            if ord(digit) >= ord(chr(65 + number1.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number1.getBase()))
            
        for digit in number2.getValue():
            if ord(digit) >= ord(chr(65 + number2.getBase() - 10)):
                raise BaseError("Numarul nu este reprezentat corect in baza " + str(number2.getBase()))
        
        if number1.getBase() in [2, 4, 8, 16] and resultBase in [2, 4, 8, 16]:
            number1 = BaseOperationsService.fastConvertion(number1, resultBase)
        elif number1.getBase() == 10:
            number1 = BaseOperationsService.convertNumberThroughBase10(number1, resultBase)
        elif number1.getBase() < resultBase:
            number1 = BaseOperationsService.convertToGreaterBase(number1, resultBase)
        else: 
            number1 = BaseOperationsService.convertToLowerBase(number1, resultBase)
            
        if number2.getBase() in [2, 4, 8, 16] and resultBase in [2, 4, 8, 16]:
            number2 = BaseOperationsService.fastConvertion(number2, resultBase)
        elif number2.getBase() == 10:
            number2 = BaseOperationsService.convertNumberThroughBase10(number2, resultBase)
        elif number2.getBase() < resultBase:
            number2 = BaseOperationsService.convertToGreaterBase(number2, resultBase)
        else: 
            number2 = BaseOperationsService.convertToLowerBase(number2, resultBase)
            
        return ArithmeticOperations.subtractNumbersWithSameBase(number1, number2)
    