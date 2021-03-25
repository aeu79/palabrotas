import argparse
import itertools
import time
import zipfile
import io
import os


def carga_diccionario(language):
    # Podría poner un input. Por ahora hardcoded
    global set_dict
    directorio = os.path.dirname(__file__)
    if language == "spanish":
        zip_path = os.path.join(directorio, "files", "palabras_es.zip")
    elif language == "english":
        zip_path = os.path.join(directorio, "files", "palabras_en.zip")
    name = "palabras.txt"
    with zipfile.ZipFile(zip_path, "r") as myzip:
        # zinfo = myzip.namelist() # Esto si no conociera el nombre del archivo
        with myzip.open(name) as file:
            file = io.TextIOWrapper(file)  # para que no lea bytes y lo abra como texto
            lineas = file.readlines()
            # set_dict = set(['perro','gato','pelo','delfin'])
            set_dict = set(
                word.split("/")[0].strip() for word in lineas
            )  # Armo un set (mucho más rápido porque usa hashes).
            # Me quedo solo hasta el '/' y saco el espacio de las que no lo tienen.


def inicio(modo, letras=None):
    """
    La función que pide los inputs y espera nuevos inputs (para cargar el diccionario en memoria una sola vez).
    Solo se encarga de eso y puede ser llamada repetidas veces (distintos intentos o juegos).
    Palabrotas se encarga de los calculos.
    """
    previous = False
    if (
        letras
    ):  # I might have letters already if it is a second round (for example to check shorter words)
        if args.spanish:
            print("Las letras actuales son: ", ", ".join(letras))
            print("Deje vacío debajo para volver a usarlas.")
        else:
            print("Current letters: ", ", ".join(letras))
            print("Leave empty below to use them again.\n")
        previous = letras
    if modo == "diccionario":
        if args.spanish:
            letras = input(
                "Ingrese las letras que deben formar las palabras.\nLetras ("
                "q"
                " para terminar): "
            ).lower()
        else:
            letras = input(
                "Enter the letters that must be used to generate the words.\nLetters ("
                "q"
                " to quit): "
            ).lower()
        if previous and (letras == ""):  # If empty, use the previous ones.
            letras = previous
    # Complete mode
    else:
        if args.spanish:
            letras = input(
                'Ingrese las letras combinables. Se pueden usar sub-palabras enteras después de un "/" (deje vacío '
                "para terminar).\nLetras: "
            ).lower()
        else:
            letras = input(
                "Enter the letters to be combined. Sub-words can be used to be combined with the other letters and "
                'can must be indicated after a "/" (leave empty to finish).\nLetters: '
            ).lower()
    if letras == "" or letras == "q":
        quit()
    if args.spanish:
        long = input("Longitud de la palabra: ")
    else:
        long = input("Length of the word: ")
    modo = modo
    palabrotas(modo, letras, long)


def filtrar(candidatas, letras):
    """
    Se encarga de filtrar y recuperar solo las palabras que contienen ciertas
    letras o palabra (Solo en el orden en que se pusieron).
    """
    filtrada = [palabra for palabra in candidatas if letras in palabra]
    print(len(filtrada))
    print(filtrada)  # set para no repetir elementos
    print("\n")
    # Vuelve a preguntar y lanza la función de nuevo (si ingresa nuevas letras):
    if args.spanish:
        rta = input("Filtrar ahora con estas letras (vacío para terminar):\n")
    else:
        rta = input(
            "Filter again but with these letters instead (leave empty to finish):\n"
        )
    if rta != "":
        filtrar(candidatas, rta)
    return


def palabrotas(modo, letras, longitud):
    # Save letras for next round
    old_letras = letras
    # Primero me fijo y separo las palabras que se hayan ingresado con "/"
    letras = letras.split("/")  # If len >1, entonces sí había algo separado por /
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
                # combinadas = [''.join(it).replace('1', letras[1]).replace('2', letras[2]).replace('3', letras[3])
                # for it in itertools.permutations(letras[0].join('123'), longitud)]
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
                print(
                    "No debería llegar nunca a este punto"
                )  # It shouldn't be possible to get here.

        combinadas = set(combinadas)
        candidatas = set(
            word for word in combinadas if word in set_dict
        )  # transformo en set para evitar repetidos: 'zafar', 'zafar' (dos "a" en el input y las considera distintas)
        that_many = str(len(combinadas))
        took = str(round(time.time() - t, 3))
        if args.spanish:
            print(
                f"Son {that_many} posibilidades. Tardó {took} segundos en combinarlas."
            )
        else:
            print(
                f"There are {that_many} possibilities. It took {took} seconds to combine them."
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
        combinadas = []
        letters = tuple(letters)
        for palabra in candidatas:
            letras = set(palabra)
            resultado = "OK"
            for letra in letras:
                if (
                    palabra.count(letra) > frecuencias[letters.index(letra)]
                ):  # letters tiene el tuple de letras combinables únicas. Con index traigo su posicón para buscar en
                    # frecuencias el número de ocurrencias.
                    resultado = "tiene más"
                    break
            if resultado == "OK":
                combinadas.append(palabra)
        candidatas = sorted(combinadas)
        """
        for word in combinadas:
            if letters & set(word):  # El & hace la intersección entre los dos sets.
                print(candidatas)
                print(type(candidatas))
                candidatas = candidatas.append(word)
        combinadas = candidatas # Compatibilidad con el modo completo (por lo que sigue)
        """
    if args.spanish:
        print(
            f"Las principales candidatas ({str(len(candidatas))}) con {longitud} letras son: "
        )
    else:
        print(
            f"The main candidates ({str(len(candidatas))}) with {longitud} letters are: "
        )
    print(candidatas)
    if args.spanish:
        rta = input("Filtrar con estas letras (vacío para terminar):\n")
    else:
        rta = input("Filter out words using these letters (leave empty to finish):\n")
    if (
        rta != ""
    ):  # Uso las letras que ingresa para filtrar los resultados un poco más (y ganarle a Matías)
        filtrar(candidatas, rta)
    if modo != "diccionario":
        if args.spanish:
            answer = input("Quiere ver el todas las posibles palabras? (s/n) ")
        else:
            answer = input("Do you want to see all of them? (y/n)")
        if (answer == "s") or (answer == "y"):
            print(set(combinadas))  # set para no repetir elementos
            print("\n")
    inicio(modo, old_letras)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-e",
        "--english",
        action="store_true",
        help="Use the English dictionary (default)",
    )
    group.add_argument(
        "-s", "--spanish", action="store_true", help="Use the Spanish dictionary"
    )
    global args
    args = parser.parse_args()
    if args.spanish:
        carga_diccionario(
            "spanish"
        )  # Carga el diccionario al principio para tenerlo en memoria y poder usarlo varias veces sin recargarlo.
        lang = "Spanish"
        print(f"El diccionario ({lang}) tiene {str(len(set_dict))} palabras.\n")
    else:
        carga_diccionario("english")
        lang = "English"
        print(f"The dictionary ({lang}) has {str(len(set_dict))} words.\n")

    if args.spanish:
        rta = input(
            'Ingrese "c" para modo completo (generar todos los posibles valores) o nada para modo "diccionario" '
            "\nModo: "
        )
    else:
        rta = input(
            'Enter "c" for "complete" mode (all possible combinations).\nLeave empty for "dictionary" mode.\nMode: '
        )
    if rta == "c":
        if args.spanish:
            print("Eligió modo completo.")
        else:
            print("Complete mode.")
        inicio("completo")  # En modo completa genera todas las opciones
    else:
        if args.spanish:
            print("Eligió modo diccionario.")
        else:
            print("Dictionary mode.")

        inicio(
            "diccionario"
        )  # En modo diccionario sólo evalúa las que coinciden con el diccionario.
