import tkinter as tk
import random
import tkinter.messagebox
import tkinter.font as font
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Hangman Spiel - 10IT")
fontSettings = font.Font(size=18)

# Feld für Galge bereitstellen
canvas = tk.Canvas(root, height=300, width=400)
canvas.pack(side="top", fill="both", expand=True)
canvas.pack()

# List of words for the game
# Woerterbuch einlesen
wordfile = open('Wortlist.txt', 'r')
word_data = wordfile.read()
word_list = word_data.split("\n")

word = random.choice(word_list).lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Zähler für falsche Angaben
incorrect_guesses = 0

# Zeichne Galgen
beam = canvas.create_line(669, 25, 669, 300, fill="black")
beamhead = canvas.create_line(669, 25, 800, 25, fill="black")
beamdiagonal = canvas.create_line(669, 42, 689, 25, fill="black" )
beamdown = canvas.create_line(800, 25, 800, 45, fill="black")
beambase = canvas.create_rectangle(650, 300, 850, 300, fill="black")

# Lade Hangman Bilder
image0 = Image.open("hangmanImage/0.png")
image1 = Image.open("hangmanImage/1.png")
image2 = Image.open("hangmanImage/2.png")
image3 = Image.open("hangmanImage/3.png")
image4 = Image.open("hangmanImage/4.png")
image5 = Image.open("hangmanImage/5.png")
image6 = Image.open("hangmanImage/6.png")
imageX = 670
imageY = 42


# Hangman Bilder Funktion
def changeHangImage(image):
    hangmanImage = ImageTk.PhotoImage(image)
    label1 = tkinter.Label(image=hangmanImage)
    label1.image = hangmanImage
    label1.place(x=imageX, y=imageY)


# Reset
def reset_game():
    global word, solution_label, incorrect_guesses, head, body, left_arm, right_arm, left_leg, right_leg, alphabet

    # neues Wort auswählen
    word = random.choice(word_list).lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    createcharbar(alphabet)

    # Lösungs Label resetten
    solution_label['text'] = "-" * len(word)

    # Reset den Zähler
    incorrect_guesses = 0
    incorrect_label['text'] = "Anzahl der Fehlversuche: 0\n"

    # Reset den Galgenmännchen
    changeHangImage(image0)


# Kontrolle ob Buchstabe im Wort
def check_letter(letter):
    global word, solution_label, incorrect_guesses, alphabet
    alphabet = alphabet.replace(letter, ' ')

    createcharbar(alphabet)
    if letter in word:
        print("Correct!")

        new_text = ""
        for i in range(len(word)):
            if word[i] == letter:
                new_text += letter
            else:
                new_text += solution_label['text'][i]
        solution_label['text'] = new_text
        if new_text == word:
            tkinter.messagebox.showinfo("Gewonnen!", "Sie haben das Word " + word + " geraten.")
            reset_game()

    else:
        print("Incorrect!")
        incorrect_guesses += 1
        incorrect_label['text'] = "Anzahl der Fehlversuche: " + str(incorrect_guesses) + "\n"
        incorrect_guess(incorrect_guesses)


# Falsch geraten
def incorrect_guess(incorrect_guesses):
    # Galgenmännchen erneuern

    if incorrect_guesses == 1:
        changeHangImage(image1)
    elif incorrect_guesses == 2:
        changeHangImage(image2)
    elif incorrect_guesses == 3:
        changeHangImage(image3)
    elif incorrect_guesses == 4:
        changeHangImage(image4)
    elif incorrect_guesses == 5:
        changeHangImage(image5)

    if incorrect_guesses >= 6:
        changeHangImage(image6)

        tkinter.messagebox.showinfo("Verloren!", "Du hast mehr als 6 Versuche gebraucht. Das Wort war " + word)
        reset_game()


# Funktion zur Wortkontrolle
def check_word(word_guess):
    global word, incorrect_guesses
    word_entry.delete(0, len(word_guess))
    if word_guess == word:
        print("Correct!")
        solution_label['text'] = word
    else:
        print("Incorrect!")
        incorrect_guesses += 1
        incorrect_label['text'] = "Anzahl der Fehlversuche: " + str(incorrect_guesses) + "\n"
        incorrect_guess(incorrect_guesses)


# Funktion AlphabetBar
def createcharbar(Alphabet):
    # Knöpfe AlphabetBar
    row = 0
    col = 0
    for letter in Alphabet:
        button = tk.Button(frame, text=letter, command=lambda x=letter: check_letter(x), height=5, width=8, font=fontSettings)
        button.grid(row=row, column=col)
        col += 1
        if col > 12:
            col = 0
            row += 1



# RUN PROGRAM
if __name__ == '__main__':

    changeHangImage(image0)
    # Container frame for buttons
    frame = tk.Frame(root)
    frame.pack(side="bottom")

    createcharbar(alphabet)
    # Full word guess entry field
    word_entry = tk.Entry(root, width=50, font=('Arial 24'))
    word_entry.pack(side="bottom")

    # Full word guess submit button
    word_button = tk.Button(root, text="Wort Eingabe", command=lambda: check_word(word_entry.get()), height=4, width=16, font=fontSettings)
    word_button.pack(side="bottom")

    # Display solution word as dashes
    solution_label = tk.Label(root, text="-" * len(word), font=fontSettings)

    solution_label.pack(side="top")

    # Display incorrect guess counter
    incorrect_label = tk.Label(root, text="Anzahl der Fehlversuche: 0\n", font=fontSettings)
    incorrect_label.pack(side="bottom")

    root.mainloop()
