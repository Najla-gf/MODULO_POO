#!/usr/bin/python
#-*- coding: utf-8 -*-

class LimitadaEdad:
    def __init__(self, edad_min: int, edad_max:int):
        self.edad_min = edad_min
        self.edad_max = edad_max

    def modificar_edad(self):
        pass
    
    def comprobar_edad(self, edad:int):
        return self.edad_min <= edad <= self.edad_max #la edad está entre el rango
    