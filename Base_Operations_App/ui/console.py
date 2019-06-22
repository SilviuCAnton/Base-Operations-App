'''
Created on Feb 10, 2019

Modul pentru interactiunea cu utilizatorul

@author: Silviu Anton
'''
from domain.entities import NumberInBase
from services.baseOperationsService import BaseOperationsService
from domain.exceptions import ConversionError, BaseError, OperationError

class Console:
    
    def __init__(self):
        self.__menu = {1 : (self.__convertThroughBase10UI, "Convertiti prin baza intermediara 10"),
                       2 : (self.__convertToGreaterBaseUI, "Convertiti la o baza mai mare prin substitutie"),
                       3 : (self.__convertToLowerBaseUI, "Convertiti la o baza mai mica prin impartiri succesive"),
                       4 : (self.__fastConversionUI, "Convertiti intre bazele 2, 4, 8 si 16 prin conversii rapide"),
                       5 : (self.__addUI, "Adunati 2 numere in baze diferite, cu rezultatul in baza introdusa"),
                       6 : (self.__subtractUI, "Scadeti 2 numere in baze diferite, cu rezultatul in baza introdusa")}
        
    def __buildMenu(self, menu):
        print("Alegeti una dintre urmatoarele optiuni: ")
        for option in menu:
            print(option, menu[option][1])
        print("0 Inchideti aplicatia")
        
    def __convertThroughBase10UI(self):
        try:
            numberValue = input("Introduceti numarul dorit: ").upper()
            base = int(input("Introduceti baza in care este reprezentat: "))
            baseToConvertTo = int(input("Introduceti baza in care doriti sa-l convertiti: "))
            
            number = NumberInBase(base, numberValue)
            
            print()
            print("Valoare convertita in baza", baseToConvertTo, ":", BaseOperationsService.convertNumberThroughBase10(number, baseToConvertTo))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
             
        except ConversionError as ce:
            print()
            print(ce)
            print()
         
        except ValueError as ve:
            print()
            print(ve)
            print()
    
    def __convertToGreaterBaseUI(self):
        try:
            numberValue = input("Introduceti numarul dorit: ").upper()
            base = int(input("Introduceti baza in care este reprezentat: "))
            baseToConvertTo = int(input("Introduceti baza in care doriti sa-l convertiti: "))
            
            number = NumberInBase(base, numberValue)
            
            print()
            print("Valoare convertita in baza", baseToConvertTo, ":", BaseOperationsService.convertNumberThroughBase10(number, baseToConvertTo))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
            
        except ConversionError as ce:
            print()
            print(ce)
            print()
        
        except ValueError as ve:
            print()
            print(ve)
            print()
    
    def __convertToLowerBaseUI(self):
        try:
            numberValue = input("Introduceti numarul dorit: ").upper()
            base = int(input("Introduceti baza in care este reprezentat: "))
            baseToConvertTo = int(input("Introduceti baza in care doriti sa-l convertiti: "))
            
            number = NumberInBase(base, numberValue)
            
            print()
            print("Valoare convertita in baza", baseToConvertTo, ":", BaseOperationsService.convertNumberThroughBase10(number, baseToConvertTo))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
            
        except ConversionError as ce:
            print()
            print(ce)
            print()
        
        except ValueError as ve:
            print()
            print(ve)
            print()
    
    def __fastConversionUI(self):
        try:
            numberValue = input("Introduceti numarul dorit: ").upper()
            base = int(input("Introduceti baza in care este reprezentat: "))
            baseToConvertTo = int(input("Introduceti baza in care doriti sa-l convertiti: "))
            
            number = NumberInBase(base, numberValue)
            
            print()
            print("Valoare convertita in baza", baseToConvertTo, ":", BaseOperationsService.convertNumberThroughBase10(number, baseToConvertTo))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
            
        except ConversionError as ce:
            print()
            print(ce)
            print()
        
        except ValueError as ve:
            print()
            print(ve)
            print()
    
    def __addUI(self):
        try:
            number1Value = input("Introduceti primul numar dorit: ").upper()
            base1 = int(input("Introduceti baza in care este reprezentat: "))
            number2Value = input("Introduceti al doilea numar dorit: ").upper()
            base2 = int(input("Introduceti baza in care este reprezentat: "))
            resultBase = int(input("Introduceti baza in care doriti sa fie rezultatul adunarii: "))
            
            
            number1 = NumberInBase(base1, number1Value)
            number2 = NumberInBase(base2, number2Value)
            
            print()
            print("Rezultatul adunarii in baza", resultBase, ":", BaseOperationsService.addNumbers(number1, number2, resultBase))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
            
        except ConversionError as ce:
            print()
            print(ce)
            print()
        
        except OperationError as oe:
            print()
            print(oe)
            print()
        
        except ValueError as ve:
            print()
            print(ve)
            print()
    
    def __subtractUI(self):
        try:
            number1Value = input("Introduceti primul numar dorit: ").upper()
            base1 = int(input("Introduceti baza in care este reprezentat: "))
            number2Value = input("Introduceti al doilea numar dorit: ").upper()
            base2 = int(input("Introduceti baza in care este reprezentat: "))
            resultBase = int(input("Introduceti baza in care doriti sa fie rezultatul scaderii: "))
            
            
            number1 = NumberInBase(base1, number1Value)
            number2 = NumberInBase(base2, number2Value)
            
            print()
            print("Rezultatul scaderii in baza", resultBase, ":", BaseOperationsService.subtractNumbers(number1, number2, resultBase))
            print()
        
        except BaseError as be:
            print()
            print(be)
            print()
            
        except ConversionError as ce:
            print()
            print(ce)
            print()
        
        except OperationError as oe:
            print()
            print(oe)
            print()
        
        except ValueError as ve:
            print()
            print(ve)
            print()
        
    def run(self):
        while True:
            self.__buildMenu(self.__menu)
            
            try:
                choice = int(input("Introduceti optiunea dorita: "))
                
                if choice == 0:
                    print()
                    print("Se inchide aplicatia...")
                    print()
                    break
                
                self.__menu[choice][0]()
                
            except ValueError as ve:
                print()
                print(ve)
                print()
                continue
            
            except KeyError as ke:
                print()
                print(ke)
                print()
                continue
            
            
                    