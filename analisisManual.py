from main import textoVerdadero


class analisisManual:

    def __init__(self):
        pass

#ANALISIS DE SENTIMIENTOS
    def analisis(self):
        palabrasPositivas = ["progreso", "futuro", "equidad", "justicia", "imparcial"]
        palabrasNegativas = ["mamerto", "paraco", "corrupciòn", "paramilitar", "hampones", "guerrillero", "primera linea", "Hijueputa"]
        contadorPositivas =0
        contadorNegativas=0
        tweetsNeutro = 0
        tweetsPositivos = 0
        tweetsNegativos = 0

        for palabra in textoVerdadero:
            if palabra in palabrasPositivas:
                contadorPositivas += 1
            elif palabra in palabrasNegativas:
                contadorNegativas += 1

        if contadorPositivas == contadorNegativas:
            tweetsNeutro += 1
            print("El tweet es Neutro, hay: " + str(tweetsNeutro))
        elif contadorPositivas > contadorNegativas:
            tweetsPositivos += 1
            print("El tweet es positivo, hay: " + str(tweetsPositivos))
        else:
            tweetsNegativos += 1
            print("El tweet es negativo, hay: " + str(tweetsNegativos))

        print("Hay " + str(contadorPositivas) + " palabras positivas")
        print("Hay " + str(contadorNegativas) + " palabras negativas")