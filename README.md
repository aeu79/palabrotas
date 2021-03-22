![Python version](https://img.shields.io/badge/Python-%3E%3D%203.6-brightgreen)


# Palabrotas

### This program helps to solve rebus puzzles and anagrams.
You must provide the letters that and the lenght of the word. The script will either combine them and produce every possible word or use a dictionary to output only "valid" words (much faster and very little memory usage).
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
[Raw version](https://raw.githubusercontent.com/aeu79/palabrotas/main/README.md) 

Then run it with python:
```bash
python3 /your/path/to/palabrotas.py
```
## Usage
#### Choose mode
First, you will be prompted to choose between the complete (press "c") or dictionary (leave empty) modes.
#### Letters
After pressing enter, you have to input the letters. Every letter is used only once, so you need to repeat them as many times as you might need.
#### Word length
Enter the word length and press enter.
#### Filter
Independently of the mode, the program will try to identify the main candidates by filtering with the dictionary. Those words will be on top. Still you will be prompted to choose a filter or leave it empty (and press enter) to finish. Filtering allows to use some letters that are for example pretty clear from the image of a rebus or a known syllable from anagram.

### Complete mode
In the complete mode, every possible combination is generated. Please, be aware that (at least in my laptop) words of length >14 letters can hang the system. Twelve letters long words generate almost 17 million possible outcomes. For long words, use only the dictionary mode.  

### Dictionary mode
## Use cases
### Rebus puzzles
### Anagrams
### Unexpected uses

## Language
### Building your dictionary
### Note

## TODO:
[] Document the usage in the readme   
[] Translate code comments to English  
[] Add the option to run it in Spanish/English  
[] Automate dictionary creation/update  




