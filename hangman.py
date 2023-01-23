import os
import random
import json

hangFile = open('hangman.json')
hangman = json.load(hangFile)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
wordlist = ['test', 'florian', 'hamburger']
played = 0


def endgame():
    retry = input('Wollen sie noch eine Runde spielen? (Y/N)\n').upper()
    if retry == 'N':
        exit
    elif retry == 'Y':
        reset()

        
def reset():
    global loesung, loesungsWort, name, fehlerZahl, richtigeBuchstabe, anzeigeReihe, name

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
        
    name = input('Bitte geben Sie ihren Namen ein:\n')



def spielfeldMethod():
    spielfeld = hangman[str(fehlerZahl)]
    os.system('cls')
    print(f'Name: {name}')
    print(f'Fehler: {fehlerZahl}')
    #print(f'DEBUG: {loesung}')
    print(spielfeld)
    print()
    word = ''.join(loesungsWort)
    print(f'WORT: {word} \n\n\n')

    print(' '.join(anzeigeReihe))
    print()
    

def alphabetRemoval(buchstabe):
    try:
        index = anzeigeReihe.index(eingabe.upper())
        anzeigeReihe[index] = ' '
    except:
        input('Buchstabe wurde schonmal genommen')


spielfeldMethod()    
reset()


    
while(True):
    spielfeldMethod()
    if fehlerZahl >= 6:
        print('Sie haben verloren!')
        print(f'Das gesuchte Wort war: {loesung.upper()}')
        endgame()
            
    if ''.join(loesungsWort).replace(' ', '') == loesung.upper():
        input('Sie haben gewonnen')
        endgame()
    
    eingabe = input("Geben Sie eine Buchstabe oder die Lösung ein.\n").upper()
    if len(eingabe) > 1:
        if eingabe == loesung:
            input('Sie haben gewonnen')
            endgame()
        else:
            input('Das war falsch!')
            fehlerZahl +=1
            
    else:
        alphabetRemoval(eingabe)
        if eingabe in loesung:
            richtigeBuchstabe.append(eingabe)
            input(f'Die Buchstabe: {eingabe} war richtig!')
            loesungIndex=[i for i in range(len(loesung)) if loesung[i]==eingabe]
            for x in loesungIndex:
                loesungsWort[x] = eingabe.upper()+" "

                
        else:
            fehlerZahl += 1
            input(f'Die Buchstabe: {eingabe} war nicht in im Lösungswort')
            
            

    
