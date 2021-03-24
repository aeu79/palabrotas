# Palabrotas

***

![Python version](https://img.shields.io/badge/Python-%3E%3D%203.6-brightgreen)

## A program to help you solve rebus puzzles and anagrams
![Top secrect](images/307px-Top_Secret_Rebus_Puzzle.png)  
[Image from](https://en.wikipedia.org/wiki/File:Top_Secret_Rebus_Puzzle.png)  

You must provide the letters that and the length of the word.
The script will either combine them and produce every possible word or use a
dictionary
to output only "valid" words (faster and very little memory usage).

## Running palabrotas.py

You can clone this repository with either of these options:

```bash
# HTTPS
git clone https://github.com/aeu79/palabrotas.git
# SSH
git clone git@github.com:aeu79/palabrotas.git
# GitHub CLI
gh repo clone aeu79/palabrotas
```

Or just copy the script:  
[Raw version](<https://raw.githubusercontent.
com/aeu79/palabrotas/main/README>.md) 
and the [files](files) folder (contains the dictionary)

And then run it with python: `python3 /your/path/to/palabrotas.py`

## Usage

#### Choose mode

First, you will be prompted to choose between the complete (press "c") or  
dictionary (leave empty) modes.

#### Letters

After pressing enter, you have to input the letters. Every letter is used
only once, so you need to repeat them as many times as you might need.

#### Word length

Enter the word length and press enter.

### Complete mode

In the complete mode, every possible combination is generated. Please, be
aware  that (at least in my laptop) words of length >14 letters can hang the
system. Twelve letters long words generate almost 17 million possible
outcomes. For long words, use only the dictionary mode.  
```
Ingrese "c" para modo completo (generar todos los posibles valores) o nada para modo "diccionario" (ingrese "h" para ayuda)
Modo: c
Eligió modo completo
Ingrese las letras combinables y palabras para usar enteras después de una "/" (nada para terminar).
Letras: aeiban
Longitud de la palabra: 3
completo
Son 72 posibilidades.Tardó 0.0 segundos en combinarlas.
Las principales candidatas (6) son: 
{'iba', 'ine', 'nia', 'ben', 'nea', 'ana'}
Filtrar con estas letras (vacío para terminar):

Quiere ver el resto? (s/n) s
{'ani', 'eia', 'bai', 'aan', 'nbi', 'nia', 'ibn', 'bae', 'nie', 'anb', 'nea', 'eab', 'aba', 'ieb', 'abe', 'nei', 'naa', 'aib', 'bia', 'bei', 'abn', 'aeb', 'inb', 'ein', 'bni', 'nba', 'aea', 'enb', 'ain', 'bea', 'ean', 'ane', 'nab', 'aae', 'aie', 'aai', 'ibe', 'bne', 'eai', 'ine', 'baa', 'aia', 'abi', 'nai', 'iab', 'bna', 'eib', 'eba', 'aen', 'iea', 'bie', 'ebi', 'ena', 'ana', 'iba', 'ban', 'iaa', 'nae', 'neb', 'ian', 'bin', 'nib', 'ebn', 'ien', 'eaa', 'aei', 'nbe', 'ben', 'aab', 'iae', 'eni', 'ina'}
```
### Dictionary mode

In the dictionary mode, only words containing the letters introduced are 
used, which saves a lot of memory and CPU. 
``` 
El diccionario tiene 917580 palabras.

Ingrese "c" para modo completo (generar todos los posibles valores) o nada para modo "diccionario" (ingrese "h" para ayuda)
Modo: 
Eligió modo diccionario
Ingrese las letras que deben formar las palabras.
Letras: aspltabaro
Longitud de la palabra: 10
diccionario
aspltabaro
{'p', 'b', 'r', 'l', 'o', 't', 'a', 's'}
[1, 1, 1, 1, 1, 1, 3, 1]
215
1
Las principales candidatas (1) son: 
['palabrotas']
Filtrar con estas letras (vacío para terminar):
``` 

#### Filter

Independently of the mode, the program will try to identify the main
candidates by filtering with the dictionary. Those words will be on top.
Still you will be prompted to choose a filter or leave it empty (and press
enter) to finish. Filtering allows to use some letters that are
for example pretty clear from the image of a rebus or a known syllable  from 
the anagram.


## Use cases

### Rebus puzzles
![Señalada](images/rebus.jpg)  
[Screen capture from](https://play.google.com/store/apps/details?id=com.etermax.apalabrados.lite&hl=es&gl=US)


### Anagrams

### Unexpected uses
#### Your kids' homework
Good to find what words they can make using their names' letters.
```
Letras: Dogual 
['adulo', 'agudo', 'aludo', 'dogal', 'laudo']
...
Letras: Liam
['ilma', 'lami', 'lima', 'mali']
```

#### Golden gate vectors design

## Language

### Building your dictionary

### Note

## TODO

[X] Document the usage in the readme  
[] Translate code comments to English  
[] Add the option to run it in Spanish/English
[] Automate dictionary creation/update  
