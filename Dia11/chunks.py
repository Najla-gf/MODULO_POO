#CHUNKS de bytes:
#grupo de una cantidad de elementos

chunk_size = 72
with open("dia11/logs/error.log", "rb") as archivo:
    chunk = archivo.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = archivo.read(chunk_size)


