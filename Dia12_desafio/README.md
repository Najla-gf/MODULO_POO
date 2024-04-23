# Desafío del Día 12

Este código incluye una solución para un desafío planteado el Día 12. Se trata de un sistema para cargar usuarios desde un archivo de texto y procesarlos en Python.

# Integrantes Grupo 2:
    - Edinson Ahumada
    - Yanina Belmar
    - Najla Gatica
    - Pablo Hernández
    - Manuel Ruiz
    - Livio Gutierrez

## Funcionalidades

1. **Escribir Error:**
    - La función `escribir_error(err)` registra errores en un archivo de registro (`error.log`) junto con la marca de tiempo en la que ocurrieron.

2. **Cargar Usuarios:**
    - La función `cargar_usuarios(archivo)` carga usuarios desde un archivo de texto (`usuarios.txt`) en formato JSON. Si hay errores en el formato de los datos, registra los errores en el archivo de registro de errores.

3. **Procesamiento de Usuarios:**
    - Los usuarios cargados se procesan y se imprime su información básica en la consola.

## Uso

1. Asegúrate de tener un archivo `usuarios.txt` con datos de usuarios en formato JSON en el directorio `Dia12_desafio`.

2. Ejecuta el script Python para cargar y procesar los usuarios.

## Ejemplo de Uso

```python
usuarios = cargar_usuarios('Dia12_desafio/usuarios.txt')
for usuario in usuarios:
    print(f'{usuario.nombre} {usuario.apellidos} - {usuario.email}')
