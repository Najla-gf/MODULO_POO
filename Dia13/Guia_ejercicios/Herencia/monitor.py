"""¡Manos a la obra! - Herencia
Desde el área de electrónica de una tienda de retail, se te ha solicitado diseñar la estructura de clases de sus monitores, 
donde cada monitor tendrá su propia resolución. Por ahora, se solicita considerar que, dentro de los monitores, existen los de tipo LED, 
y también existen los monitores multifunción. En este caso, considere crear una clase que permita crear monitores / televisor 2 en 1 
(debes considerar una clase Televisor)."""

from televisor import Televisor 

class Monitor(): 
    def __init__(self, resolucion) -> None: 
        self.resolucion = resolucion
        
class MonitorLED(Monitor): 
    pass

class MonitorTelevisor(Monitor, Televisor): 
    pass