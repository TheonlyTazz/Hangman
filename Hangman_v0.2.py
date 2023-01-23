import os
import time
import random
import json


header = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      '''

# Variablen
name = ''
punkte = 0
fehlerZahl = 0
difficulty = ''
playerDB = {}

# Alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
anzeigeReihe = []

# Woerterbuch einlesen
wordfile = open('Wortlist.txt', 'r')
word_data = wordfile.read()
wordlist = word_data.split("\n")

# Hangman Figur
hangFile = open('hangman.json', 'r')
hangman = json.load(hangFile)




def head():
    # Kopf/Logo
    os.system('cls')
    print(header)
    print(f'Name: {name} | Punkte: {punkte}')
    print('\n')


def mainmenu():
    global difficulty
    # Hauptmenu
    head()
    print('Wilkommen beim 10IT Hangman Spiel.')
    print()
    print('Bitte Schwierigkeit auswählen')
    difficulty = input('1) 4-5 Buchstaben\n2) 6-8 Buchstaben\n3) 9+ Buchstaben\n> ')
    if difficulty.isdigit() == False:
        input('Bitte geben Sie eine Zahl ein.')
        mainmenu()
    elif int(difficulty) > 3 or int(difficulty) <= 0:
        input('Bitte geben Sie eine Zahl zwischen 1 - 3 ein.')
        mainmenu()

    randomword(int(difficulty))
    playerselector()


def randomword(dif):
    global word
    word = random.choice(wordlist).upper()
    if dif == 1:
        if len(word) < 4 or len(word) > 5:
            randomword(dif)
    elif dif == 2:
        if len(word) < 6 or len(word) > 8:
            randomword(dif)
    elif dif == 3:
        if len(word) < 9:
            randomword(dif)

    anzeigeReihe.clear()
    for x in alphabet:
        anzeigeReihe.append(x)


def playerselector():
    global playerCount
    # Spieler Anzahl + Name
    head()
    print('Wieviele Spieler sollen mitspielen?')
    playerCount = input('> ')
    if playerCount.isdigit() == False:
        input('Bitte geben Sie eine Zahl ein.')
        playerselector()
    if int(playerCount) <= 0:
        input('Bitte geben Sie eine Zahl höher als 0 ein.')
        playerselector()

    buildplayerdb(int(playerCount))

    guess()


def buildplayerdb(playercount):
    playerDB.clear()
    for playerIndex in range(playercount):
        head()
        print(f'Bitte geben sie Spielername {playerIndex+1} ein')
        name = input('> ')
        playerDB[name] = 0


def drawhangman():
    # Galgenmännchen anzeigen
    spielfeld = hangman[str(fehlerZahl)]
    print(spielfeld)


def drawalphabet():
    # Alphabet Liste anzeigen bzw löschen
    print(' '.join(anzeigeReihe))


def drawword():
    print()


def guess():
    # Raten
    head()
    print(word)
    drawhangman()
    drawword()
    drawalphabet()

    attempt = input('Bitte geben Sie einen Buchstaben zum raten ein, oder ein Lösungswort.\n> ')
    # Buchstabe raten
    if len(attempt) == 1:
        index = anzeigeReihe.index(attempt.upper())
        anzeigeReihe[index] = ' '

        if attempt.upper() in word:
            print('Buchstabe ist im Wort!')



    # Loesungswort raten
    else:
        #TEMP
        pass


def win():
    # Gewinn
    os.system('cls')


def lose():
    # Verloren
    os.system('cls')


def retry():
    # Neuspiel?
    if retry == True:
        mainmenu()



mainmenu()


