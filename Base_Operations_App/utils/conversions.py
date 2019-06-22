'''
Created on Feb 9, 2019

Modul pentru operatiile de conversie

@author: Silviu Anton
'''
from domain.entities import NumberInBase
from utils.arithmetics import ArithmeticOperations
from math import sqrt

class Conversion:
    
    #Dictionar pentru conversiile rapide intre bazele 2,4,8,16 ( variabila statica in clasa statica Conversion )
    #Este un dictionar de dictionare!!! Fiecare subdictionar corespunde unei baze (4, 8 sau 16)
    fastConversionDict = { 4 : {"0": "00", "1" : "01", "2": "10", "3" : "11"},
                           8 : {"0" : "000", "1" : "001", "2": "010", "3" : "011", "4" : "100", "5" : "101", "6" : "110", "7" : "111"},
                           16 : {"0" : "0000", "1" : "0001", "2": "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110",
                                 "7" : "0111", "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101",
                                 "E" : "1110", "F" : "1111"}}
    
    @staticmethod
    def convertBySubstitution(number, baseToConvertTo):
        '''
        Description: Converteste un numar dintr-o baza mai mica intr-una mai mare prin substitutie
        
        In:
            - number - numarul de convertit 
            - baseToConvertTo - baza in care convertim
        Out:
            - numberInDesiredBase - numarul convertit in baza dorita
        '''
        power = 0
        numberInDesiredBase = NumberInBase(baseToConvertTo, '0')
        numberValue = number.getValue()
        base = number.getBase()
        
        #Cat timp mai sunt cifre in numar executa
        while len(numberValue) > 0:
            #Se aplica normal algorimul conversiei prin substitutie
            #Operatorul ** inseamna ridicare la putere
            digit = NumberInBase(baseToConvertTo, numberValue[-1]) 
            numberToAdd = ArithmeticOperations.multiplyByDigit(NumberInBase(baseToConvertTo, str(base ** power)), digit)
            numberInDesiredBase = ArithmeticOperations.addNumbersWithSameBase(numberInDesiredBase, numberToAdd)
            power += 1
            
            numberValue = numberValue[:-1]
            
        return numberInDesiredBase
    
    @staticmethod
    def convertByDivision(number, baseToConvertTo):
        '''
        Description: converteste un number dintr-o baza mai mare intr-o baza mai mica prin impartiri succesive
        
        In:
            - number - numarul de convertit
            - baseToConvertTo - baza in care se va converti numarul
            
        Out:
            - resultNumber - numarul convertit in baza corespunzatoare
        '''
        resultValue = ''
        base = number.getBase()
        numberValue = number.getValue()
        copyBase = baseToConvertTo
        
        #Facem o copie a bazei pentru a o putea folosi in calcul si ca cifra mai mare decat 9
        if copyBase > 9:
            copyBase = chr(65 + baseToConvertTo - 10)
        
        #Cat timp mai sunt cifre in numar repeta
        while len(numberValue) > 0:
            #Se aplica normal algoritmul conversiei prin impartiri repetate
            numberToDivide = NumberInBase(base, numberValue)
            number, remainder = ArithmeticOperations.divideByDigit(numberToDivide, NumberInBase(base, str(copyBase)))
            digit = remainder.getValue()
            
            #Tratam cazul cifrelor mai mari decat 9
            if int(digit) > 9:
                resultValue += chr(65 + int(digit) - 10) 
            else: resultValue += str(digit)
            
            numberValue = number.getValue()
        
        #Asiguram ordinea corecta a cifrelor
        resultValue = resultValue[::-1]
        
        #Eliminam cifra de 0 din fata numarului
        if resultValue[0] == '0':
            resultValue = resultValue[1:]
            
        resultNumber = NumberInBase(baseToConvertTo, resultValue)
        return resultNumber  
    
    @staticmethod
    def convertTo2(number):
        '''
        Description: converteste un numar din baza 4,8 sau 16 in baza 2
        
        In:
            - number - numarul de convertit
        Out:
            - numarul convertit in baza 2
        '''
        base = number.getBase()
        conversionDict = Conversion.fastConversionDict[base]
        numberValue = number.getValue()
        resultValue = ""
        
        #Se converteste folosind in mod direct dictionarul de conversie, declarat static in clasa statica Conversion
        for digit in numberValue:
            resultValue += conversionDict[digit]
        
        #Eliminam cifrele de 0 din fata rezultatului    
        while resultValue[0] == '0' and len(resultValue) > 1:
            resultValue = resultValue[1:]
        
        return NumberInBase(2, resultValue)
    
    @staticmethod
    def convertFrom2(number, baseToConvertTo):
        '''
        Description: converteste un numar din baza 2 in baza 4, 8 sau 16
        
        In:
            - number - numarul de convertit
            - baseToConvertTo - baza in care va fi convertit numarul
        Out:
            - numarul convertit in baza dorita
        '''
        resultValue = ""
        conversionDict = Conversion.fastConversionDict[baseToConvertTo]
        
        #Inversam ordinea cifrelor in numar pentru a le putea grupa in grupuri de cifre de la dreapta la stanga    
        numberValue = number.getValue()
        numberValue = numberValue[::-1]
        
        #Calculam numarul de cifre dintr-un grup (in functie de baza aleasa pentru conversie)    
        numberOfDigits = int(round(sqrt(baseToConvertTo)))
        
        #Folosind list comprehension am extras o lista ce contine toate grupurile de cifre
        digitList = [numberValue[i : i + numberOfDigits]  for i in range(0, len(numberValue), numberOfDigits)]
        
        #Inversam fiecare grup pentru a obtine numerele corecte la conversie    
        for index in range(len(digitList)):
            digitList[index] = digitList[index][::-1]
        
        #Adaugam 0 in fata grupului care nu are numarul corect de cifre, pana acesta e atins    
        while len(digitList[-1]) < numberOfDigits:
            digitList[-1] = '0' + digitList[-1]
        
        #Folosind list comprehension cream o lista cu toate cheile din dictionar care au valoarea grupului de cifre in baza 2
        #Deoarece valorile din dictionar sunt unice, aceasta lista va contine doar o singura cifra, cea in baza in care dorim sa convertim, lista fiind doar un artificiu ajutator        
        for digit in digitList:
            newDigit = [key for (key, value) in conversionDict.items() if value == digit] 
            #Adaugam cifra obtinuta prin conversie la rezultat
            resultValue += newDigit[0]
        
        #Asiguram ordinea corecta a cifrelor in numar    
        resultValue = resultValue[::-1]
            
        return NumberInBase(baseToConvertTo, resultValue)
        