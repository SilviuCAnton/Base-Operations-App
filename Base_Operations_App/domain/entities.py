'''
Created on Feb 7, 2019

Modul pentru entitatile din aplicatie (numere)

@author: Silviu Anton
'''

class NumberInBase:
    
    #Fiecare numar este caracterizat printr-o baza si o valoare (valoarea e memorata ca sir de caractere)
    def __init__(self, base, value):
        self.__base = base
        self.__value = value

    def getBase(self):
        return self.__base
    
    def getValue(self):
        return self.__value
    
    #Aceasta functie dicteaza reprezentarea datei in cazuri de afisare (print)
    def __repr__(self):
        return self.getValue()