#!/usr/bin/python
#-*- coding: utf-8 -*-

class Encuesta:
    def __init__(self, nombre:str, listado_preguntas, listado_respuestas):
        self.nombre = nombre
        self.__listado_preguntas = listado_preguntas
        self.__listado_respuestas = listado_respuestas

    @property
    def listado_preguntas(self):
        return self.__listado_preguntas

    @property
    def listado_respuestas(self):
        return self.__listado_respuestas

    def modificar_nombre(self, nuevo_nombre:str):
        self.nombre = nuevo_nombre

    def mostrar_encuesta(self):
        print(self.nombre, self.listado_preguntas)

    def mostrar_respuestas(self):
        print(self.nombre, self.listado_respuestas)

