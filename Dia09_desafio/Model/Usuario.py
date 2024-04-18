#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self, correo:str, edad:int, region:int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def modificar_usuario(self, nuevo_correo:str, nueva_edad:int, nueva_region:int):
        self.correo = nuevo_correo
        self.edad = nueva_edad
        self.region = nueva_region


    def contestar_encuesta(self, encuesta, respuesta):
        listado_respuesta = ListadoRespuestas(self, respuesta)
        encuesta.listado_respuesta.append(listado_respuesta)



