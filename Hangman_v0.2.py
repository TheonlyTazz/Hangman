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
playerDB = {} # Datenbank / Dictionary
activePlayer = 0

# Alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
anzeigeReihe = []

# Anzeigewort
anzeigeWort = []

# Woerterbuch einlesen
wordfile = open('Wortlist.txt', 'r')
word_data = wordfile.read()
wordlist = word_data.split("\n")
word = ""

# Hangman Figur
hangFile = open('hangman.json', 'r')
hangman = json.load(hangFile)


def head():
    # Kopf/Logo
    os.system('cls')
    print(header)
    print(f'Name: {name} | Punkte: {punkte}')
    #print(f'Loesung: {word}')
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
    playerCreator()


def randomword(dif):
    global word, fehlerZahl
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

    fehlerZahl = 0
    anzeigeReihe.clear()
    for x in alphabet:
        anzeigeReihe.append(x)

    anzeigeWort.clear()

    for char in range(len(word)):
        anzeigeWort.append('_')


def playerCreator():
    global playerCount
    # Spieler Anzahl + Name
    head()
    print('Wieviele Spieler sollen mitspielen?')
    playerCount = input('> ')
    if playerCount.isdigit() == False:
        input('Bitte geben Sie eine Zahl ein.')
        playerCreator()
    if int(playerCount) <= 0 or int(playerCount) > 4:
        input('Bitte geben Sie eine Zahl höher als 0 oder weniger als 4 ein.')
        playerCreator()

    buildplayerdb(int(playerCount))

    guess()


def buildplayerdb(playercount):
    playerDB.clear()
    for playerIndex in range(playercount):

        name = ''
        while name == '':
            head()
            print(f'Bitte geben sie Spielername {playerIndex + 1} ein')
            name = input('> ')
        playerDB[name] = 0


def playerSelector():
    global activePlayer
    if activePlayer > len(playerDB) - 1:
        activePlayer = 0
    name = list(playerDB.keys())[activePlayer]
    activePlayer += 1
    return name


def drawhangman(fehlerZahl):
    # Galgenmännchen anzeigen
    spielfeld = hangman[str(fehlerZahl)]
    print(spielfeld)
    print()


def drawword():
    print(f'WORT:')
    print(' '.join(anzeigeWort))
    print()


def drawalphabet():
    # Alphabet Liste anzeigen bzw löschen
    print(' '.join(anzeigeReihe))


def guess():
    global fehlerZahl, name, punkte
    name = playerSelector()
    punkte = playerDB[name]
    # Raten
    head()
    # print(word)
    drawhangman(fehlerZahl)
    drawword()
    drawalphabet()

    attempt = input('Bitte geben Sie einen Buchstaben zum raten ein, oder ein Lösungswort.\n> ')

    # Buchstabe raten
    if len(attempt) == 1:
        if attempt.upper() in anzeigeReihe:
            index = anzeigeReihe.index(attempt.upper())
            anzeigeReihe[index] = ' '

            # Wenn Versuch im Wort
            if attempt.upper() in word:
                print('Buchstabe ist im Wort!')
                time.sleep(0.5)


                # Wortreihe einfüllen
                for i in range(len(word)):
                    if word[i] == attempt.upper():
                        anzeigeWort[i] = word[i]
                        playerDB[name] = playerDB[name] + 1

                if '_' not in anzeigeWort:
                    win()

            # Wenn Versuch nicht im Wort
            else:
                print(f'Das war verkehrt!')
                time.sleep(0.5)
                fehlerZahl = fehlerZahl + 1

        else:
            print('Buchstabe wurde bereits gewählt')
            time.sleep(0.5)
            fehlerZahl = fehlerZahl + 1



    # Loesungswort raten
    else:
        if attempt.upper() == word:
            for i in range(len(word)):
                if anzeigeWort[i] == '_':
                    playerDB[name] = playerDB[name] + 2

            win()
        else:
            print(f'Das war verkehrt!')
            time.sleep(0.5)
            fehlerZahl = fehlerZahl + 1


    if fehlerZahl >= 6:
        lose()

    guess()


def win():
    # Gewonnen
    print('Sie Haben gewonnen!')
    retry()


def lose():
    # Verloren

    print('Sie haben verloren\n')
    print(f'Das Lösungswort war: {word.upper()}')

    retry()


def retry():
    global name, punkte

    for player, value in playerDB.items():
        print(f'{player}: {value}  Punkte')

    # Neuspiel?
    ask = input('Noch ein Spiel?   Y/N \n>')
    if ask.upper() == 'Y':
        Retry = True
    elif ask.upper() == 'N':
        Retry = False
    else:
        head()
        retry()

    if Retry == True:
        name = ''
        punkte = 0
        mainmenu()
    else:
        exit()


if __name__ == "__main__":
    mainmenu()
