#!/usr/bin/python
#-*- coding: utf-8 -*-

class ListadoRespuestas:
    def __init__(self, lista_respuestas:int, usuario):
        self.usuario = usuario
        self.__lista_respuestas = lista_respuestas

    @property
    def lista_respuestas(self):
        return self.__lista_respuestas
    