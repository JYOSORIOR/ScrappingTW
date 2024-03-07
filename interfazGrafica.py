from tkinter import *
import tweepy
import pandas as pd
import matplotlib.pyplot as plt

def click():
    label1=Label(ventana)
    label1.place(x="100", y="200")

def analisis():
    # Leer claves de twitter
    api_key = "zpmslWcxmAdFeIChym9Bv4lOI"
    api_key_secret = "DVRYwIfNU5av32fAMYdGAUxA3oAHQ4BbsF2IzmHO1jwVq2ICtE"

    access_token = "1261647634328162310-93Ia28pQCfxqUfwJseD9ny9KOcMZg6"
    access_token_secret = "j4qUvNkX9YtQ5Dlv9ml7WSCiNItami5FZpOcjldkhUrVL"

    # Autenticar claves de twitter

    auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q=texto1.get(), count=1000)
    print(len(tweets))
    palabrasPositivas = ["progreso", "futuro", "equidad", "responsable", "justicia", "imparcial", "admirablemente",
                         "habil", "adaptado", "alcanzable", "ventaja", "defensor", "poder", "agil", "adecuado",
                         "garantia", "autentico", "desempeño", "inteligente", "fortaleza", "pacto", "libertad",
                         "gentil", "generoso", "honesto", "heroe", "ingeniero", "record", "sincero", "un+", "abundar",
                         "abunda", "abundancia", "abundante", "accesible", "accesible", "aclamación", "aclamado",
                         "aclamación", "espaldarazo", "elogios", "cómodo", "acomodativo", "realizar", "logrado",
                         "preciso", "precisamente", "realizable", "logro", "logros", "alcanzable", "perspicacia",
                         "adaptable", "adaptado", "adecuado", "ajustable", "admirable", "admirablemente", "admiración",
                         "admirar", "admirador", "admirativo", "admirativamente", "adorable", "adorar", "adorado",
                         "adorador", "cariñoso", "con adoración", "hábil", "hábilmente", "adular", "adulación",
                         "adulador", "avanzado", "ventaja", "ventajoso", "ventajosamente", "ventajas", "aventurero",
                         "aventurero", "defensor", "defendido", "defensores", "afabilidad", "afable", "afablemente",
                         "afectación", "afecto", "cariñoso", "afinidad", "afirmar", "afirmación", "afirmativo",
                         "afluencia", "afluente", "poder pagar", "asequible", "asequible", "asequible", "ágil",
                         "ágilmente", "agilidad", "agradable", "simpatía", "agradablemente", "todo al rededor",
                         "seductor", "seductoramente", "altruista", "altruistamente", "asombrado", "asombro", "asombra",
                         "increíble", "Asombrosamente", "ambicioso", "ambiciosamente", "mejorar", "dócil", "amenidad",
                         "amabilidad", "amablemente", "amable", "amabilidad", "amistoso", "amistosamente", "amistad",
                         "amplio", "ampliamente", "entretener", "entretenido", "graciosamente", "ángel", "angelical",
                         "apoteosis", "apelación", "atractivo", "aplaudir", "apreciable", "agradecer", "apreciado",
                         "aprecia", "agradecido", "apreciativamente", "adecuado", "aprobación", "aprobar", "ardiente",
                         "ardientemente", "ardor", "articular", "aspiración", "aspiraciones", "aspirar", "garantía",
                         "garantías", "asegurar", "ciertamente", "asegurando", "asombrar", "asombroso"]

    palabrasNegativas = ["mamerto", "paraco", "sucia", "delito", "decepción", "cizaña", "riesgo", "demanda",
                         "corrupciòn", "paramilitar", "hampones", "guerrillero", "primera linea", "hijueputa",
                         "dos caras", "machista", "agresivo", "grosero", "pesimo", "arrogante", "asesino", "vulgar",
                         "descarado", "sanguinario", "falso", "descarado", "atemorizar", "victima", "cancer",
                         "preocupacion", "maldito", "peligro", "ofensivo", "loco", "anormal", "abolir", "abominable",
                         "abortar", "abortado", "aborta", "desgastar", "abrupto", "abruptamente", "fugarse", "ausencia",
                         "despistado", "ausente", "absurdo", "absurdo", "absurdamente", "absurdo", "abuso", "abusado",
                         "abusos", "abusivo", "abismal", "abismalmente", "abismo", "accidental", "abordar", "maldito",
                         "acusación", "acusaciones", "acusar", "acusa", "acusando", "acusatoriamente", "exacerbar",
                         "acerbo", "mordazmente", "dolor", "dolido", "dolores", "adolorido", "dolor", "acre",
                         "acremente", "acidez", "mordaz", "acritud", "firme", "firmemente", "adicto", "adicto",
                         "adictivo", "adictos", "amonestar", "amonestar", "amonestación", "amonestación",
                         "amonestación", "adulterar", "espurio", "adulteración", "adúltero", "contradictorio",
                         "adversario", "adverso", "adversidad", "afligir", "aflicción", "doloroso", "afrenta",
                         "temeroso", "agravar", "agravante", "agravación", "agresión", "agresividad", "agresor",
                         "ofender", "agraviado", "agravación", "espantado", "agonías", "agonizar", "agonizante",
                         "agonizantemente", "agonía", "encallado", "afligir", "enfermo", "enfermedad", "sin", "alarma",
                         "alarmado", "alarmante", "alarmantemente", "acusaciones", "a distancia", "altercado",
                         "emboscada", "expropiar", "expropiacion"]

    contadorPositivas = 0
    contadorNegativas = 0
    tweetsNeutro = 0
    tweetsPositivos = 0
    tweetsNegativos = 0
    columnas = ['User', 'Tweet']
    data = []

    for tweet in tweets:
        # if "RT" not in tweet.text:
        data.append([tweet.user.screen_name, tweet.text])
        textoNuevos = (tweet.text).lower()
        textoNuevo = textoNuevos.replace(",", "")
        texticoNuevo = textoNuevo.replace(".", "")
        textoVerdadero = texticoNuevo.split(" ")

        for palabra in textoVerdadero:
            if palabra in palabrasPositivas:
                contadorPositivas += 1
            elif palabra in palabrasNegativas:
                contadorNegativas += 1

        if contadorPositivas == contadorNegativas:
            tweetsNeutro += 1
            print("El tweet es Neutro")
        elif contadorPositivas > contadorNegativas:
            tweetsPositivos += 1
            print("El tweet es positivo")
        else:
            tweetsNegativos += 1
            print("El tweet es negativo")

    print("Hay " + str(tweetsNeutro) + " tweets Neutros")
    print("Hay " + str(tweetsPositivos) + " tweets positivos")
    print("Hay " + str(tweetsNegativos) + " tweets negativos")

    ## Declaramos valores para el eje x
    eje_x = ['Positivo', 'Negativo', 'Neutro']

    ## Declaramos valores para el eje y
    eje_y = []
    eje_y.append(tweetsPositivos)
    eje_y.append(tweetsNegativos)
    eje_y.append(tweetsNeutro)

    ## Creamos Gráfica
    plt.bar(eje_x, eje_y)

    ## Legenda en el eje y
    plt.ylabel('Cantidad de tweets')

    ## Legenda en el eje x
    plt.xlabel('TIPOS')

    ## Título de Gráfica
    plt.title('Grafica de tipos')

    ## Mostramos Gráfica
    plt.show()
    # saca graficas a partir de lo que me salgan en contador

    df = pd.DataFrame(data, columns=columnas)
    df.to_csv('tweets.csv')

def propuestaCandidatos():
    ventanas = Tk()
    ventanas.title("¡Encuesta Propuestas!")
    # AnchoXAlto
    ventanas.geometry('700x555')
    ventanas.config(background='light blue')

    etiqueta = Label(ventanas, text="A continuación te haremos 10 preguntas,"
                " marca 1 si estas de acuerdo, marca 2 si no estas de acuerdo.\n")
    etiqueta.pack()

    etiquetaUno= Label(ventanas, text="1)¿Está usted de acuerdo con modificar la reforma tributaria?: ")
    etiquetaUno.pack()
    etiquetaUno.place(x="0", y="30")
    textoUno = Entry(ventanas)
    textoUno.pack()
    textoUno.place(x="0", y="55")

    etiqueta2 = Label(ventanas, text="2)¿Está usted de acuerdo con el pago por horas en el trabajo?: ")
    etiqueta2.pack()
    etiqueta2.place(x="0", y="80")
    texto2 = Entry(ventanas)
    texto2.pack()
    texto2.place(x="0", y="105")

    etiqueta3 = Label(ventanas, text="3)¿Está usted de acuerdo con el tratado de paz?: "
                      )
    etiqueta3.pack()
    etiqueta3.place(x="0", y="130")
    texto3 = Entry(ventanas)
    texto3.pack()
    texto3.place(x="0", y="155")

    etiqueta4 = Label(ventanas, text="4)¿Está usted de acuerdo con reformar o eliminar la legalidad del aborto?: ")
    etiqueta4.pack()
    etiqueta4.place(x="0", y="180")
    texto4 = Entry(ventanas)
    texto4.pack()
    texto4.place(x="0", y="205")

    etiqueta5 = Label(ventanas, text="5)¿Está usted de acuerdo que debería exigirse a todos los ciudadanos de 18 años que presten al menos un año de servicio militar?: ")
    etiqueta5.pack()
    etiqueta5.place(x="0", y="230")
    texto5 = Entry(ventanas)
    texto5.pack()
    texto5.place(x="0", y="255")

    etiqueta6 = Label(ventanas, text="6)¿Está usted de acuerdo con subir la edad para recibir la pensión?: ")
    etiqueta6.pack()
    etiqueta6.place(x="0", y="280")
    texto6 = Entry(ventanas)
    texto6.pack()
    texto6.place(x="0", y="305")

    etiqueta7 = Label(ventanas, text="7)¿Está usted de acuerdo que el gobierno debe hacer recortes en el gasto público para reducir la deuda nacional?: ")
    etiqueta7.pack()
    etiqueta7.place(x="0", y="330")
    texto7 = Entry(ventanas)
    texto7.pack()
    texto7.place(x="0", y="355")

    etiqueta8 = Label(ventanas, text="8)¿Está usted de acuerdo con despenalizar y legalizar el consumo de la marihuana?: ")
    etiqueta8.pack()
    etiqueta8.place(x="0", y="380")
    texto8 = Entry(ventanas)
    texto8.pack()
    texto8.place(x="0", y="405")

    etiqueta9 = Label(ventanas, text="9)¿Está usted de acuerdo con el fracking?: ")
    etiqueta9.pack()
    etiqueta9.place(x="0", y="430")
    texto9 = Entry(ventanas)
    texto9.pack()
    texto9.place(x="0", y="455")

    etiqueta10 = Label(ventanas, text="10)¿Está usted de acuerdo que en Colombia debería aumentar los impuestos a los ricos?: ")
    etiqueta10.pack()
    etiqueta10.place(x="0", y="480")
    texto10 = Entry(ventanas)
    texto10.pack()
    texto10.place(x="0", y="505")

    botonUno = Button(ventanas, text="¡AVERIGUALO!", command=click)
    botonUno.place(x="0", y="530")

    ventana.mainloop()


#VENTANA UNO =)
ventana = Tk()
ventana.title("¡Descubre tu candidato!")
#AnchoXAlto
ventana.geometry('380x300')
ventana.config(background='misty rose')
etiqueta= Label(ventana, text="Bienvenido al programa en el cual te puedes guiar para escoger \n tu candidato en segunda vuelta =D")
etiqueta.pack()

botonUno=Button(ventana, text="Encuesta sobre los candidatos", command=propuestaCandidatos)
botonUno.place(x="80", y="85")

etiqueta1 = Label(ventana, text="Introduce el nombre del candidato que deseas buscar")
etiqueta1.pack()
etiqueta1.place(x="50", y="130")
texto1 = Entry(ventana)
texto1.pack()
texto1.place(x="100", y="155")

botonDos=Button(ventana, text="Busca los tweets sobre este candidato!", command=analisis)
botonDos.place(x="70", y="180")


ventana.mainloop()



