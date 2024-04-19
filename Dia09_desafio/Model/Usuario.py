#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self, correo:str, edad:int, region:int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    def modificar_usuario(self, nuevo_correo:str, nueva_edad:int, nueva_region:int):
        self.__correo = nuevo_correo
        self.__edad = nueva_edad
        self.__region = nueva_region

    @property
    def correo(self):
        return self.__correo
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def region(self):
        return self.__region

    def contestar_encuesta(self, encuesta, respuesta):
        listado_respuesta = ListadoRespuestas(self, respuesta)
        encuesta.listado_respuesta.append(listado_respuesta)



