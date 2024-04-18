#!/usr/bin/python
#-*- coding: utf-8 -*-

class LimitadaRegion:
    def __init__(self, lista_regiones: int):
        self.lista_regiones = lista_regiones

    def modificar_region(self):
        pass
    
    def comprobar_region(self, region:int):
        return region in self.lista_regiones #la region del usuario la comprobamos dentro dela lista de regiones
