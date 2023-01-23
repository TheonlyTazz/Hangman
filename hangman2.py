import os
import random
import json
import time
hangFile = open('hangman.json')
hangman = json.load(hangFile)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
wordfile = open('Wortlist.txt', 'r')
word_data = wordfile.read()
wordlist = word_data.split("\n")
played = 0
header = f""" _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\_,|| ||\_, || || ||\_,|| ||
                    __/ |
                   |___/
v0.0.1 | Größe der Wörterliste: {len(wordlist)} Wörter"""
def head():
    os.system('cls')
    print(header)
    
def endgame():
    endloop = 1
    for x in spielerdic:
        spielerdic[x] = 0
    while endloop == 1:
        retry = input('Wollen sie noch eine Runde spielen? (Y/N)\n').upper()
        if retry == 'N':
            exit
        elif retry == 'Y':
            endloop = 0
            q = input('gleiche spieler? Y/N \n')
            if q.upper() == 'N':
                played = 0
                spielerdic.clear()
                spielerListe.clear()
                spielermodus()
            os.system('cls')
            reset()
            spielfeldMethod()
def spielerSelector():
    activeSpieler += 1
    if activespieler > len(spielerdic):
        activeSpieler = 0
    name = spielerListe[activeSpieler]
def reset():
    global loesung, loesungsWort, name, fehlerZahl, richtigeBuchstabe, anzeigeReihe, name, spielerdic, spielerListe, punkte
    os.system("cls")
    fehlerZahl = 0
    richtigeBuchstabe = []
    anzeigeReihe = []
    loesung = random.choice(wordlist).upper()
    loesungsWort = []
    for x in loesung:
        loesungsWort.append(x)
    for x in range(len(loesungsWort)):
        loesungsWort[x] = '_ '
    for x in alphabet:
        anzeigeReihe.append(x)
    print(header)
    if played == 0:
        spielerListe = []
        spielerdic = {}
        spielermodus()
    activeSpieler = 0
    spieler = spielerdic.items()
    name = spielerListe[activeSpieler]
    punkte = spielerdic[name]
def spielfeldMethod():
    spielfeld = hangman[str(fehlerZahl)]
    head()
    print(f'\nName: {name}')
    print(f'Fehler: {fehlerZahl} | Punkte: {punkte}')
    #print(f'DEBUG: {loesung}')
    print(spielfeld)
    print()
    word = ''.join(loesungsWort)
    print(f'WORT: {word} \n')
    print(' '.join(anzeigeReihe))
    print()
def alphabetRemoval(buchstabe):
    try:
        index = anzeigeReihe.index(eingabe.upper())
        anzeigeReihe[index] = ' '
    except:
        input('Buchstabe wurde schonmal genommen')
def spielermodus():
    spielerZahl = input('Wieviele Spieler sollen spielen?\n')
    if spielerZahl.isnumeric() == False:
        print('Bitte geben Sie eine Zahl ein')
    for i in range(int(spielerZahl)):
        name = input(f'Bitte Spieler {i+1} Name eingeben:\n')
        spielerdic[name] = 0
        spielerListe.append(name)
        head()
reset()
spielfeldMethod()
while(True):
    played = 1
    spielfeldMethod()
    if fehlerZahl >= 6:
        print('Sie haben verloren!')
        print(f'Das gesuchte Wort war: {loesung.upper()}')
        endgame()
    if ''.join(loesungsWort).replace(' ', '') == loesung.upper():
        input('Sie haben gewonnen')
        endgame()
    eingabe = input("Geben Sie eine Buchstabe oder die Lösung ein.\n").upper()
    if eingabe == "":
        print("Eingabe ist leer.")
        time.sleep(0.5)
        continue
    if len(eingabe) > 1:
        if eingabe == loesung:
            loesungIndex=[i for i in range(len(loesung)) if loesung[i]=='_ ']
            for x in loesungIndex:
                spielerdic[name] += 1
            print('Sie haben gewonnen')
            time.sleep(0.75)
            endgame()
        else:
            fehlerZahl +=1
            print('Das war falsch!')
            time.sleep(0.75)
    else:
        alphabetRemoval(eingabe)
        if eingabe in loesung:
            richtigeBuchstabe.append(eingabe)
            print(f'Die Buchstabe: {eingabe} war richtig!')
            time.sleep(0.75)
            loesungIndex=[i for i in range(len(loesung)) if loesung[i]==eingabe]
            for x in loesungIndex:
                loesungsWort[x] = eingabe.upper()+" "
                spielerdic[name] += 1
        else:
            fehlerZahl += 1
            print(f'Die Buchstabe: {eingabe} war nicht in im Lösungswort')
            time.sleep(0.75)
