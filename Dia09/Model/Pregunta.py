#!/usr/bin/python
#-*- coding: utf-8 -*-

class Pregunta:
    def __init__(self, enunciado:str, ayuda:str, requerida:bool, lista_alternativas):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__lista_alternativas = lista_alternativas

    @property #Getter para la lista de alternativas
    def lista_alternativas(self):
        return self.__lista_alternativas

    def mostrar_enunciado(self):
        return print(self.mostrar_enunciado)

