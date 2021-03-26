# Palabrotas

***

![Python version](https://img.shields.io/badge/Python-%3E%3D%203.6-brightgreen)

## A program to help you solve rebus puzzles and anagrams

<img src="images/307px-Top_Secret_Rebus_Puzzle.png" width="150">

[Image from](https://en.wikipedia.org/wiki/File:Top_Secret_Rebus_Puzzle.png)  

You must provide the letters that and the length of the word.
The script will either combine them and produce every possible word or use a
dictionary
to output only "valid" words (faster and very little memory usage).

## Contents
* [Running palabrotas.py](#running-palabrotaspy)
* [Usage](#usage)
  * [Choose mode](#choose-mode)
  * [Letters](#letters)
  * [Word length](#word-length)
  * [Complete mode](#complete-mode)
  * [Dictionary mode](#dictionary-mode)
  * [Filter](#filter)
* [Use cases](#use-cases)
  * [Rebus puzzles](#rebus-puzzles)
  * [Anagrams](#anagrams)
  * [Unexpected uses](#unexpected-uses)
    * [Your kids' homework](#your-kids-homework)
    * [Golden gate vectors design](#golden-gate-vectors-design)
* [Language](#language)
  * [Building your dictionary](#building-your-dictionary)
    * [Spanish](#spanish)
    * [English](#english)
* [TODO](#todo)

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

And run it:

```bash
cd palabrotas && python3 palabrotas.py
```

Or just copy the [script](https://raw.githubusercontent.com/aeu79/palabrotas/main/palabrotas.py)
and the ["files"](files) folder (which contains the dictionaries).
Then run it: `python3 /your/path/to/palabrotas.py`

## Usage

### Choose mode

First, you will be prompted to choose between the complete (press "c") or  
dictionary (leave empty) modes.

### Letters

After pressing enter, you have to input the letters. Every letter is used
only once, so you need to repeat them as many times as you need.

### Word length

Enter the word length and press enter.

### Complete mode

In the complete mode, every possible combination is generated. Please, be
aware  that (at least in my laptop) words of length >14 letters can hang the
system. Twelve letters long words generate almost 17 million possible
outcomes. For very long words, you should use only the dictionary mode.
Example run  in "complete" mode (-en, English version):

```
The dictionary (English) has 170588 words.

Enter "c" for "complete" mode (all possible combinations).
Leave empty for "dictionary" mode.
Mode: c
Complete mode.
Enter the letters to be combined. Sub-words can be used to be combined with the other letters and can must be indicated after a "/" (leave empty to finish).
Letters: aetor
Length of the word: 3
There are 60 possibilities. It took 0.0 seconds to combine them.
The main candidates (23) with 3 letters are: 
{'ore', 'era', 'rte', 'roe', 'toe', 'tor', 'rat', 'eat', 'tea', 'ret', 'aet', 'art', 'tar', 'eta', 'are', 'ear', 'oar', 'ort', 'oat', 'rot', 'ate', 'ora', 'ter'}
Filter out words using these letters (leave empty to finish):

Do you want to see all of them? (y/n)y
{'eot', 'aoe', 'rta', 'teo', 'ore', 'tro', 'era', 'roa', 'rte', 'rae', 'roe', 'toe', 'tor', 'oet', 'eat', 'rat', 'oea', 'tea', 'ret', 'tao', 'tre', 'aet', 'ote', 'aeo', 'tra', 'atr', 'rao', 'art', 'tar', 'eta', 'are', 'ear', 'tae', 'eao', 'oar', 'eor', 'ota', 'eto', 'aor', 'toa', 'etr', 'aer', 'ort', 'ert', 'oer', 'rto', 'aot', 'rea', 'ero', 'oae', 'oat', 'otr', 'rot', 'reo', 'ate', 'aro', 'ora', 'eoa', 'ter', 'ato'}
```

### Dictionary mode

In the dictionary mode, only words containing the letters introduced are
used, which saves a lot of memory and CPU.
Example run  in "dictionary" mode (-es, Spanish version):

```
El diccionario (Spanish) tiene 917580 palabras.

Ingrese "c" para modo completo (generar todos los posibles valores) o nada para modo "diccionario" 
Modo: 
Eligió modo diccionario.
Ingrese las letras que deben formar las palabras.
Letras (q para terminar): aspltabaro
Longitud de la palabra: 10
Las principales candidatas (1) con 10 letras son: 
['palabrotas']
```

### Filter

Independently of the mode, the program will try to identify the main
candidates by filtering with the dictionary. Those words will be on top.
Still you will be prompted to choose a filter or leave it empty (and press
enter) to finish. Filtering allows to use some letters that are
for example pretty clear from the image of a rebus or a known syllable  from
the anagram.

## Use cases

### Rebus puzzles

<img src="images/rebus.jpg" width="184">

Screenshot of [Apalabrados (Word Crack)](https://play.google.com/store/apps/details?id=com.etermax.apalabrados.lite&hl=es&gl=US)

Answer:
<img src="images/rta.png" height="160">

### Anagrams

<img src="images/anagram1.png" width="184">

Screenshot of [Word of wonders)](https://play.google.com/store/apps/details?id=com.fugo.wow&hl=en&gl=US)

Letters: M F U O R

```
Main candidates with 5 letters:
['forum']
...
Main candidates with 4 letters:
['form', 'four', 'from']
...
Main candidates with 3 letters:
['for', 'fou', 'fro', 'fum', 'fur', 'mfr', 'our', 'rom', 'rum']
```

<img src="images/anagram2.png" width="184">

And "for"... 🎉

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

Get all possible combinations of ACTG taken 3 at a time:

```
Letras: ACTG
Longitud de la palabra: 3
...
{'cgt', 'atc', 'tga', 'cga', 'gac', 'cta', 'gca', 'ctg', 'agc', 'atg', 'gtc', 'cat', 'tcg', 'tgc', 'agt', 'tac', 'act', 'cag', 'gat', 'tca', 'gct', 'tag', 'gta', 'acg'}
```

## Language  

The can run in English or Spainsh and using the corresponding dictionary

English (default):

```bash
python3 palabrotas.py -en
```

Spanish:

```bash
python3 palabrotas.py -es
```  

*Svenska kommer snart*  🤞

### Building your dictionary

Install hunspell-tools: ```sudo apt install hunspell-tools```

#### Spanish

Instruction to create the Spanish dictionary:

* Clone the repository

```bash
git clone https://github.com/sbosio/rla-es.git &&
cd ./rla-es/ && git pull
```  

* Generate the words, including plurals, conjugated verbs, etc. (unmunch 
  diccionario.dic afijos.aff):

```bash
unmunch './ortograf/herramientas/es_ANY.dic' './ortograf/herramientas/es_ANY.aff' > 'palabras_todas.txt'
```

* Remove the accent marks (á, é, í, ó, ú and uppercase variants):

```bash
sed -r 's/á/a/g;s/Á/a/g;s/É/e/g;s/é/e/g;s/Í/i/g;s/í/i/g;s/Ó/o/g;s/ó/o/g;s/Ú/u/g;s/ú/u/g' palabras_todas.txt > palabras.txt
```

* Remove uppercase:

```bash
sed -i 's/\(.*\)/\L\1/' palabras.txt
```

* And compress it (with python 😅):

```bash
python3 -m zipfile -c palabras_es.zip palabras.txt
```

#### English

```bash
wget https://archlinux.org/packages/extra/any/hunspell-en_gb/download/
unmunch en_GB-large.dic en_GB-large.aff > palabras.txt
zip palabras_en.zip palabras.txt
```

## TODO

* [x] Document the usage in the readme  
* [ ] Translate code comments to English  
* [x] Add the option to run it in Spanish/English  
* [ ] Automate dictionary creation/update
* [ ] Add Swedish dictionary.

TOC created using [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)
