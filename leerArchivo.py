class leerArchivo:

    def __init__(self):
        pass

    def leerArchivos(self):
        listaArchivos = []
        aux = open("propuestas.txt", "r")
        archivo = aux.readlines()
        for i in archivo:
            if i != "\n":
                auxiliar = i.strip("\n")
                listaArchivos.append(auxiliar)
        return listaArchivos


