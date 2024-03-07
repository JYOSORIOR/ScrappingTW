import tweepy
import pandas as pd
import matplotlib.pyplot as plt

from questionPresident import questionPresident

questionPresidentt = questionPresident()


#Leer claves de twitter
api_key = "zpmslWcxmAdFeIChym9Bv4lOI"
api_key_secret = "DVRYwIfNU5av32fAMYdGAUxA3oAHQ4BbsF2IzmHO1jwVq2ICtE"

access_token = "1261647634328162310-93Ia28pQCfxqUfwJseD9ny9KOcMZg6"
access_token_secret = "j4qUvNkX9YtQ5Dlv9ml7WSCiNItami5FZpOcjldkhUrVL"

#Autenticar claves de twitter

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

questionPresidentt.EncuestaCandidatos()


#BUSQUEDA DE PALABRAS EN TWEETS
searchTerm = input("\nRespecto a su resultado anterior, nos gustaría que visualizara que piensan las personas \nde el candidato "
                   "de tu preferencia o del otro candidato inscrito,\npara esto ingresa el nombre del candidato sobre"
                   " quien te gustaría saber: ")

cuantostweets = input("Ingrese cuantos tweets desea analizar: ")

tweets = api.search_tweets(q=searchTerm,  count=cuantostweets)
print(len(tweets))
palabrasPositivas = ["progreso", "futuro", "equidad", "responsable", "justicia", "imparcial", "admirablemente", "habil", "adaptado",  "alcanzable", "ventaja", "defensor", "poder", "agil", "adecuado", "garantia", "autentico", "desempeño", "inteligente", "fortaleza", "pacto", "libertad", "gentil", "generoso", "honesto", "heroe", "ingeniero", "record", "sincero", "un+", "abundar", "abunda", "abundancia", "abundante","accesible", "accesible", "aclamación", "aclamado","aclamación","espaldarazo","elogios","cómodo","acomodativo","realizar","logrado","preciso","precisamente","realizable","logro","logros","alcanzable","perspicacia","adaptable","adaptado","adecuado","ajustable","admirable","admirablemente","admiración","admirar","admirador","admirativo","admirativamente","adorable","adorar","adorado","adorador","cariñoso","con adoración","hábil","hábilmente","adular","adulación","adulador","avanzado","ventaja","ventajoso","ventajosamente","ventajas","aventurero","aventurero","defensor","defendido","defensores","afabilidad","afable","afablemente","afectación","afecto","cariñoso","afinidad","afirmar","afirmación","afirmativo","afluencia","afluente","poder pagar","asequible","asequible","asequible","ágil","ágilmente","agilidad","agradable","simpatía","agradablemente","todo al rededor","seductor","seductoramente","altruista","altruistamente","asombrado","asombro","asombra","increíble","Asombrosamente","ambicioso","ambiciosamente","mejorar","dócil","amenidad","amabilidad","amablemente","amable","amabilidad","amistoso","amistosamente","amistad","amplio","ampliamente","entretener","entretenido","graciosamente","ángel","angelical","apoteosis","apelación","atractivo","aplaudir","apreciable","agradecer","apreciado","aprecia","agradecido","apreciativamente","adecuado","aprobación","aprobar","ardiente","ardientemente","ardor","articular", "aspiración", "aspiraciones","aspirar","garantía","garantías","asegurar","ciertamente","asegurando","asombrar","asombroso"]
palabrasNegativas = ["mamerto", "paraco","sucia", "delito", "decepción", "cizaña", "riesgo", "demanda", "corrupciòn", "paramilitar", "hampones", "guerrillero", "primera linea", "hijueputa", "dos caras", "machista", "agresivo", "grosero", "pesimo", "arrogante", "asesino", "vulgar", "descarado", "sanguinario", "falso", "descarado", "atemorizar", "victima", "cancer", "preocupacion", "maldito", "peligro", "ofensivo", "loco", "anormal","abolir","abominable","abortar","abortado","aborta","desgastar","abrupto","abruptamente","fugarse","ausencia","despistado","ausente","absurdo","absurdo","absurdamente","absurdo","abuso","abusado","abusos","abusivo","abismal","abismalmente","abismo","accidental","abordar","maldito","acusación","acusaciones","acusar","acusa","acusando","acusatoriamente","exacerbar","acerbo","mordazmente","dolor","dolido","dolores","adolorido","dolor","acre","acremente","acidez","mordaz","acritud","firme","firmemente","adicto","adicto","adictivo","adictos","amonestar","amonestar","amonestación","amonestación","amonestación","adulterar","espurio","adulteración","adúltero","contradictorio","adversario","adverso","adversidad","afligir","aflicción","doloroso","afrenta","temeroso","agravar","agravante","agravación","agresión", "agresividad","agresor","ofender","agraviado","agravación","espantado","agonías","agonizar","agonizante","agonizantemente","agonía","encallado","afligir","enfermo","enfermedad","sin","alarma","alarmado","alarmante","alarmantemente","acusaciones","a distancia","altercado", "emboscada", "expropiar", "expropiacion"]
contadorPositivas =0
contadorNegativas=0
tweetsNeutro = 0
tweetsPositivos = 0
tweetsNegativos = 0
columnas = ['User', 'Tweet']
data = []

for tweet in tweets:
    #if "RT" not in tweet.text:
        data.append([tweet.user.screen_name, tweet.text])
        textoNuevos=(tweet.text).lower()
        textoNuevo=textoNuevos.replace(",", "")
        texticoNuevo=textoNuevo.replace(".", "")
        textoVerdadero=texticoNuevo.split(" ")

        for palabra in textoVerdadero:
            if palabra in palabrasPositivas:
                contadorPositivas += 1
            elif palabra in palabrasNegativas:
                contadorNegativas += 1

        if contadorPositivas == contadorNegativas:
            tweetsNeutro +=1
            print("El tweet es Neutro")
        elif contadorPositivas > contadorNegativas:
            tweetsPositivos +=1
            print("El tweet es positivo")
        else:
            tweetsNegativos +=1
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
#saca graficas a partir de lo que me salgan en contador

df = pd.DataFrame(data, columns=columnas)
df.to_csv('tweets.csv')