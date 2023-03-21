import tkinter as tk
import random
import tkinter.messagebox
import tkinter.font as font
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Hangman Spiel - 10IT")

# Creating canvas to draw hangman figure
canvas = tk.Canvas(root, height=300, width=400)
canvas.pack(side="top", fill="both", expand=True)
canvas.pack()
#label = tk.Label(canvas, image=image)
#label.image = image
#label.pack()

# List of words for the game
# Woerterbuch einlesen
wordfile = open('Wortlist.txt', 'r')
word_data = wordfile.read()
word_list = word_data.split("\n")

word = random.choice(word_list).lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Counter for incorrect guesses
incorrect_guesses = 0

# Draw hangman parts

beam = canvas.create_line(669, 25, 669, 300, fill="black")
beamhead = canvas.create_line(669, 25, 800, 25, fill="black")
beamdiagonal = canvas.create_line(669, 42, 689, 25, fill="black" )
beamdown = canvas.create_line(800, 25, 800, 45, fill="black")
beambase = canvas.create_rectangle(650, 300, 850, 300, fill="black")

head = canvas.create_oval(750, 45, 850, 145, fill="white", state="hidden")
body = canvas.create_line(800, 145, 800, 245, fill="black", state="hidden")
left_arm = canvas.create_line(800, 195, 750, 145, fill="black", state="hidden")
right_arm = canvas.create_line(800, 195, 850, 145, fill="black", state="hidden")
left_leg = canvas.create_line(800, 245, 750, 295, fill="black", state="hidden")
right_leg = canvas.create_line(800, 245, 850, 295,fill="black", state="hidden")

left_eye = canvas.create_line(775, 60, 775, 90, fill="black", state='hidden')
right_eye = canvas.create_line(825, 60, 825, 90, fill="black", state='hidden')
mouth = canvas.create_line(775, 100, 825, 100, fill="black", state='hidden')

image0 = Image.open("hangmanImage/0.png")
image1 = Image.open("hangmanImage/1.png")
image2 = Image.open("hangmanImage/2.png")
image3 = Image.open("hangmanImage/3.png")
image4 = Image.open("hangmanImage/4.png")
image5 = Image.open("hangmanImage/5.png")
image6 = Image.open("hangmanImage/6.png")


imageX = 670
imageY = 42
test = ImageTk.PhotoImage(image0)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=imageX, y=imageY)



fontSettings = font.Font(size=18)

# Function to reset the game
def reset_game():
    global word, solution_label, incorrect_guesses, head, body, left_arm, right_arm, left_leg, right_leg, alphabet

    # Choose a new word from the word list
    word = random.choice(word_list).lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    createcharbar(alphabet)

    # Reset the solution label to display dashes for each character in the word
    solution_label['text'] = "-" * len(word)

    # Reset the incorrect guess counter
    incorrect_guesses = 0
    incorrect_label['text'] = "Anzahl der Fehlversuche: 0\n"

    # Reset the hangman figure
    canvas.itemconfig(head, fill="white", state="hidden")
    canvas.itemconfig(body, fill="black", state="hidden")
    canvas.itemconfig(left_arm, fill="black", state="hidden")
    canvas.itemconfig(right_arm, fill="black", state="hidden")
    canvas.itemconfig(left_leg, fill="black", state="hidden")
    canvas.itemconfig(right_leg, fill="black", state="hidden")

    canvas.itemconfig(left_eye, fill="black", state="hidden")
    canvas.itemconfig(right_eye, fill="black", state="hidden")
    canvas.itemconfig(mouth, fill="black", state="hidden")

# Function to check if letter is in word
def check_letter(letter):
    global word, solution_label, incorrect_guesses, alphabet
    alphabet = alphabet.replace(letter, ' ')
    print(alphabet)
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

def incorrect_guess(incorrect_guesses):
    # Creating canvas to draw hangman figure

    if incorrect_guesses == 1:
        #canvas.itemconfig(head, fill="white", state="normal")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)
    elif incorrect_guesses == 2:
        #canvas.itemconfig(body, fill="black", state="normal")
        test = ImageTk.PhotoImage(image2)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)
    elif incorrect_guesses == 3:
        #canvas.itemconfig(left_arm, fill="black", state="normal")
        test = ImageTk.PhotoImage(image3)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)
    elif incorrect_guesses == 4:
        #canvas.itemconfig(right_arm, fill="black", state="normal")
        test = ImageTk.PhotoImage(image4)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)
    elif incorrect_guesses == 5:
        #canvas.itemconfig(left_leg, fill="black", state="normal")
        test = ImageTk.PhotoImage(image5)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)

    if incorrect_guesses >= 6:
        #canvas.itemconfig(right_leg, fill="black", state="normal")
        #canvas.itemconfig(left_eye, fill="black", state="normal")
        #canvas.itemconfig(right_eye, fill="black", state="normal")
        #canvas.itemconfig(mouth, fill="black", state="normal")
        test = ImageTk.PhotoImage(image6)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=imageX, y =imageY)

        tkinter.messagebox.showinfo("Verloren!", "Du hast mehr als 6 Versuche gebraucht. Das Wort war " + word)
        reset_game()

# Function to check if full word is correct
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


# Container frame for buttons
frame = tk.Frame(root)
frame.pack(side="bottom")



def createcharbar(Alphabet):
    # Creating buttons for each alphabet
    row = 0
    col = 0
    for letter in Alphabet:
        button = tk.Button(frame, text=letter, command=lambda x=letter: check_letter(x), height=5, width=8, font=fontSettings)
        button.grid(row=row, column=col)
        col += 1
        if col > 12:
            col = 0
            row += 1


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
