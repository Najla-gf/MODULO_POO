# Descripción del Proyecto

El equipo de desarrollo ha decidido crear una API utilizando Python para gestionar campañas de marketing. Aunque aún se está evaluando qué framework se aplicará, la primera etapa del proyecto consiste en crear la arquitectura de clases básica que permita instanciar una campaña. Esta arquitectura debe contener los tipos de anuncio más solicitados por los clientes.

## Diagrama de Clases

El siguiente diagrama de clases muestra la estructura de clases que se utilizará en la API:

![Diagrama de Clases](Dia13/Prueba/Diagrama.png)

## Archivos de Código

### anuncio.py

Este archivo define la clase `Anuncio` y sus subclases `Video`, `Display` y `Social`. Estas clases representan diferentes tipos de anuncios y contienen métodos para establecer atributos como ancho, alto, URL de archivo, URL de clic, subtipo, duración, entre otros. Además, se define un método `mostrar_formatos()` para mostrar los formatos y subtipos disponibles.

### campana.py

En este archivo se encuentra la clase `Campana`, que representa una campaña de marketing. Esta clase gestiona una lista de anuncios y proporciona métodos para crear campañas, modificar el nombre de la campaña y obtener información sobre los anuncios asociados.

### error.py

Aquí se definen dos clases de excepciones personalizadas: `SubTipoInvalidoError` y `LargoExcedidoError`. Estas excepciones se utilizan para manejar errores relacionados con subtipos inválidos de anuncios y nombres de campañas demasiado largos, respectivamente.

### demo.py

Este archivo contiene una función `manejar_excepciones()` que demuestra el manejo de excepciones en el contexto de la creación de una instancia de `Campana` y la modificación de su nombre y el subtipo de un anuncio. Se capturan las excepciones relacionadas con nombres de campañas demasiado largos o subtipos inválidos, y se registran en un archivo `error.log`.

## Ejemplo de Uso

Para ejecutar el manejo de excepciones, asegúrate de tener todos los archivos de código en la misma carpeta y ejecuta el archivo `demo.py`. 

```bash
python demo.py
