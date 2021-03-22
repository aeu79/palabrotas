import itertools
import time
import zipfile
import io
import os


def carga_diccionario():
    # Podría poner un input. Por ahora hardcoded
    global set_dict
    directorio = os.path.dirname(__file__)
    zip_path = os.path.join(directorio, "files", "palabras.zip")
    # zip_path = '/home/agu/Dropbox/Python scripts/palabrotas/palabras.zip'
    name = "palabras.txt"
    with zipfile.ZipFile(zip_path, "r") as myzip:
        # zinfo = myzip.namelist() # Esto si no conociera el nombre del archivo
        with myzip.open(name) as file:
            file = io.TextIOWrapper(file)  # para que no lea bytes y lo abra como texto
            lineas = file.readlines()
            # set_dict = set(['perro','gato','pelo','delfin'])
            set_dict = set(
                word.split("/")[0].strip() for word in lineas
            )  # Armo un set (mucho más rápido porque usa hashes). Me quedo solo hasta el '/' y saco el espacio de las que no lo tienen.


def inicio(modo):
    """
    La función que pide los inputs y espera nuevos inputs (para cargar el diccionario en memoria una sola vez).
    Solo se encarga de eso y puede ser llamada repetidas veces (distintos intentos o juegos).
    Palabrotas se encarga de los calculos.
    """
    if modo == "diccionario":
        letras = input("Ingrese las letras que deben formar las palabras.\nLetras: ")
    else:
        letras = input(
            'Ingrese las letras combinables y palabras para usar enteras después de una "/" (nada para terminar).\nLetras: '
        )
    if letras == "":
        quit()
    long = input("Longitud de la palabra: ")
    modo = modo
    palabrotas(modo, letras, long)


def filtrar(candidatas, letras):
    """
    Se encarga de filtrar y recuperar solo las palabras que contienen ciertas
    letras o palabra (Solo en el orden en que se pusieron).
    """
    filtrada = [
        palabra for palabra in candidatas if letras in palabra
    ]  # Toma sólo las que contienen las letras elegidas para filtrar. List comprehension with conditional if... Tomá mate!
    print(len(filtrada))
    print(filtrada)  # set para no repetir elementos
    print("\n")
    # Vuelve a preguntar y lanza la función de nuevo (si ingresa nuevas letras):
    rta = input("Filtrar ahora con estas letras (vacío para terminar):\n")
    if rta != "":
        filtrar(candidatas, rta)
    return


def palabrotas(modo, letras, longitud):
    # Primero me fijo y separo las palabras que se hayan ingresado con "/"
    letras = letras.split("/")  # If len >1, entonces sí había algo separado por /
    # letras[0] contiene las letras, 1,2, 3, etc. tienen las palabras para usar en la formación de palabras.
    print(modo)
    longitud = int(longitud)
    if modo == "completo":
        t = time.time()  # Para tomarle el tiempo
        if type(letras) is list:
            if len(letras) > 5:
                print("Solo se pueden incluir hasta 3 palabras.")
            elif len(letras) == 4:  # ['asdfasdf','perro','gato','delfin']
                new_long = str(
                    longitud - len(letras[1]) - len(letras[2]) - len(letras[3]) + 3
                )  # restando las letras de la palabra fija
                for x in letras[1]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                for x in letras[2]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                for x in letras[3]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                letras[0] += "123"
                combinadas = [
                    "".join(it)
                    .replace("1", letras[1])
                    .replace("2", letras[2])
                    .replace("3", letras[3])
                    for it in itertools.permutations(
                        letras[0].join("123"), int(new_long)
                    )
                    if len(
                        "".join(it)
                        .replace("1", letras[1])
                        .replace("2", letras[2])
                        .replace("3", letras[3])
                    )
                    == longitud
                ]
                # combinadas = [''.join(it).replace('1', letras[1]).replace('2', letras[2]).replace('3', letras[3]) for it in itertools.permutations(letras[0].join('123'), longitud)]
            elif len(letras) == 3:  # ['asdfasdf','perro','gato']
                new_long = str(
                    longitud - len(letras[1]) - len(letras[2]) + 2
                )  # restando las letras de la palabra fija
                for x in letras[1]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                for x in letras[2]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                letras[0] += "12"
                combinadas = [
                    "".join(it).replace("1", letras[1]).replace("2", letras[2])
                    for it in itertools.permutations(
                        letras[0].join("12"), int(new_long)
                    )
                    if len("".join(it).replace("1", letras[1]).replace("2", letras[2]))
                    == longitud
                ]
            elif len(letras) == 2:  # ['asdfasdf','perro']
                new_long = str(
                    longitud - len(letras[1]) + 1
                )  # restando las letras de la palabra fija
                for x in letras[1]:
                    letras[0] = letras[0].replace(
                        x, "", 1
                    )  # borro del listado las que voy a usar
                letras[0] += "1"
                combinadas = [
                    "".join(it).replace("1", letras[1])
                    for it in itertools.permutations(letras[0], int(new_long))
                    if len("".join(it).replace("1", letras[1])) == longitud
                ]
            elif len(letras) == 1:  # ['asdfasdf']
                combinadas = [
                    "".join(it) for it in itertools.permutations(letras[0], longitud)
                ]
            else:
                print("No debería llegar nunca a este punto")
        """
        Ahora voy a podría hacer un reemplazo para poder usar una palabra en el medio
        y no todas las posibles combinaciones [''.join(it).replace('P','J') for it in itertools.permutations('atdP', 3)]
     
        combinadas = [''.join(it) for it in itertools.permutations(letras, longitud)] #Las da separadas así que con join uno cada letra en palabras individuales
           """
        combinadas = set(combinadas)
        candidatas = set(
            word for word in combinadas if word in set_dict
        )  # transformo en set para evitar repetidos: 'zafar', 'zafar' (dos "a" en el input y las considera distintas)
        print(
            "Son "
            + str(len(combinadas))
            + " posibilidades."
            + "Tardó "
            + str(round(time.time() - t, 3))
            + " segundos en combinarlas."
        )
    elif modo == "diccionario":
        # Primero filtro por tamaño:
        combinadas = [
            palabra for palabra in set_dict if len(palabra) == longitud
        ]  # Traigo todas las del diccionario con el tamaño correcto.
        # Ahora las que tienen las letras correctas:
        combinables = letras[0]  # Las letras que se deben usar
        letters = set(
            combinables
        )  # Las letras que se deben usar, pero una sola vez cada letra, sin repetir.
        # Filtro solo las que tienen las letras del listado.
        candidatas = [
            palabra for palabra in combinadas if set(palabra).issubset(letters)
        ]
        # Y verifico que no excedan la cantidad de ocurrencias de cada letra en la palabra.
        frecuencias = [combinables.count(letra) for letra in letters]
        print(combinables)
        print(letters)
        print(frecuencias)
        combinadas = []
        letters = tuple(letters)
        print(len(candidatas))
        # candidatas = [palabra for palabra in candidatas if (palabra.count(letra) > frecuencias[letters.index(letra)] for letra in letras)]
        for palabra in candidatas:
            letras = set(palabra)
            resultado = "OK"
            for letra in letras:
                if (
                    palabra.count(letra) > frecuencias[letters.index(letra)]
                ):  # letters tiene el tuple de letras combinables únicas. Con index traigo su posicón para buscar en frecuencias el número de ocurrencias.
                    resultado = "tiene más"
                    break
            if resultado == "OK":
                combinadas.append(palabra)
        print(len(combinadas))
        candidatas = sorted(combinadas)
        """
        for word in combinadas:
            if letters & set(word):  # El & hace la intersección entre los dos sets.
                print(candidatas)
                print(type(candidatas))
                candidatas = candidatas.append(word)
        combinadas = candidatas # Compatibilidad con el modo completo (por lo que sigue)
        """
    print("Las principales candidatas (" + str(len(candidatas)) + ") son: ")
    print(candidatas)
    rta = input("Filtrar con estas letras (vacío para terminar):\n")
    if (
        rta != ""
    ):  # Uso las letras que ingresa para filtrar los resultados un poco más (y ganarle a Matías)
        filtrar(candidatas, rta)
    if modo != "diccionario":
        if input("Quiere ver el resto? (s/n) ") == "s":
            print(set(combinadas))  # set para no repetir elementos
            print("\n")
    modo = modo
    inicio(modo)


if (
    __name__ == "__main__"
):  # Por si después quier reusar una función de acá (sin que se ejecute todo).
    carga_diccionario()  # Carga el diccionario al principio para tenerlo en memoria y poder usarlo varias veces sin recargarlo.
    print("El diccionario tiene " + str(len(set_dict)) + " palabras.\n")
    rta = input(
        'Ingrese "c" para modo completo (generar todos los posibles valores) o nada para modo "diccionario" (ingrese "h" para ayuda)\nModo: '
    )
    if rta == "c":
        print("Eligió modo completo")
        inicio("completo")  # En modo completa genera todas las opciones
    elif rta == "h":
        print("Ayuda:")
        print("Hable con el programador...")
        inicio("completo")  # En modo completa genera todas las opciones
    else:
        print("Eligió modo diccionario")
        inicio(
            "diccionario"
        )  # En modo diccionario sólo evalúa las que coinciden con el diccionario.

    """ TODO: filtrar el restulado completo
Algo así, pero podría combinar con palbras textuales, comienzo o final, etc.
import re

words = ["AMALGAMATED", "AMMONIATED", "CIRCUMAMBULATED", "COMMENTATED", 
         "TAMTAM", "BLUB", "HOUSE", "SOMETHING"]
filter = "mmt"

regex = re.compile(".*".join(filter), re.IGNORECASE)
filtered_words = [word for word in words if regex.search(word)]

print(*filtered_words, sep="\n")

"""
"""
INSTRUCCIONES PARA ARMAR EL DICCIONARIO:
Clono el repositorio del español:
git clone https://github.com/sbosio/rla-es.git
Lo actualizo si ya lo tenía
cd ./rla-es/ && git pull
Instalo hunspell-tools:
sudo apt install hunspell-tools
Y con unmunch diccionario.dic afijos.aff hago todas las combinaciones:
unmunch '/home/agu/rla-es/ortograf/herramientas/es_ANY.dic' '/home/agu/rla-es/ortograf/herramientas/es_ANY.aff' > '/home/agu/rla-es/ortograf/herramientas/palabras_todas.txt'
Limpio el listado de acentos (con ; separa cada instrucción independiente, múltiples sed en uno solo):
El comando: sed -r 's/á/a/g;s/Á/a/g;s/É/e/g;s/é/e/g;s/Í/i/g;s/í/i/g;s/Ó/o/g;s/ó/o/g;s/Ú/u/g;s/ú/u/g'; quedaría así:
sed -r 's/á/a/g;s/Á/a/g;s/É/e/g;s/é/e/g;s/Í/i/g;s/í/i/g;s/Ó/o/g;s/ó/o/g;s/Ú/u/g;s/ú/u/g' /home/agu/rla-es/ortograf/herramientas/palabras_todas.txt > /home/agu/rla-es/ortograf/herramientas/palabras.txt
Y saco las mayúsculas (con -i edito directo en el original)
sed -i 's/\(.*\)/\L\1/' /home/agu/rla-es/ortograf/herramientas/palabras.txt
Lo comprimo con:
python3 -m zipfile -c palabras.zip '/home/agu/rla-es/ortograf/herramientas/palabras.txt'
"""
