class questionPresident:

    def __init__(self):
        pass

    # Preguntas sobre candidatos
    def EncuestaCandidatos(self):
        opcion = True
        while opcion:
            RodolfoH = 0
            GustavoP = 0
            ninguno = 0

            print(
                "Bienvenido al programa para tener más seguridad sobre tu candidato en segunda vuelta.\nA continuación te haremos 10 preguntas,"
                " marca 1 si estas de acuerdo, marca 2 si no estas de acuerdo.\n")

            PreguntaUno = input("1)¿Está usted de acuerdo con modificar la reforma tributaria?: ")
            if PreguntaUno == "1":
                RodolfoH = RodolfoH + 1
            if PreguntaUno == "2":
                GustavoP = GustavoP + 1

            PreguntaDos = input("2)¿Está usted de acuerdo con el pago por horas en el trabajo?: ")
            if PreguntaDos == "1":
                ninguno = ninguno + 1
            if PreguntaDos == "2":
                GustavoP = GustavoP + 1
                RodolfoH = RodolfoH + 1

            PreguntaTres = input("3)¿Está usted de acuerdo con el tratado de paz?: ")
            if PreguntaTres == "1":
                GustavoP = GustavoP + 1
            if PreguntaTres == "2":
                RodolfoH = RodolfoH + 1

            preguntaCuatro = input("4)¿Está usted de acuerdo con reformar o eliminar la legalidad del aborto?: ")
            if preguntaCuatro == "1":
                GustavoP = GustavoP + 1
            if preguntaCuatro == "2":
                RodolfoH = RodolfoH + 1


            preguntaCinco = input("5)¿Está usted de acuerdo que debería exigirse a todos los ciudadanos de 18 años que presten al menos un año de servicio militar?: ")
            if preguntaCinco == "1":
                RodolfoH = RodolfoH + 1
            if preguntaCinco == "2":
                GustavoP = GustavoP + 1

            preguntaSeis = input("6)¿Está usted de acuerdo con subir la edad para recibir la pensión?: ")
            if preguntaSeis == "1":
                ninguno = ninguno + 1
            if preguntaSeis == "2":
                RodolfoH = RodolfoH + 1
                GustavoP = GustavoP + 1

            preguntaSiete = input("7)¿Está usted de acuerdo que el gobierno debe hacer recortes en el gasto público para reducir la deuda nacional?: ")
            if preguntaSiete == "1":
                GustavoP = GustavoP + 1
                RodolfoH = RodolfoH + 1
            if preguntaSiete == "2":
                ninguno = ninguno + 1

            preguntaOcho = input("8)¿Está usted de acuerdo con despenalizar y legalizar el consumo de la marihuana?: ")
            if preguntaOcho == "1":
                GustavoP = GustavoP + 1
            if preguntaOcho == "2":
                RodolfoH = RodolfoH + 1

            preguntaNueve = input("9)¿Está usted de acuerdo con el fracking?: ")
            if preguntaNueve == "1":
                RodolfoH = RodolfoH + 1
            if preguntaNueve == "2":
                GustavoP = GustavoP + 1


            preguntaDiez = input("10)¿Está usted de acuerdo que en Colombia debería aumentar los impuestos a los ricos?: ")
            if preguntaDiez == "1":
                GustavoP = GustavoP + 1
                opcion = False
            if preguntaDiez == "2":
                RodolfoH = RodolfoH + 1

            print("Gustavo Petro: ", GustavoP)
            print("Rodolfo Hernandez: ", RodolfoH)