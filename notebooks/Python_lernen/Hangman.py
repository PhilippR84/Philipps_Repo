import random

my_datei = open("C:\\Users\\Phili\\OneDrive\\DHBW\\VSCode\\Philipps_Repo\\notebooks\\Python_lernen\\Hangman_words.txt","r",encoding="UTF8")
int_Rows_datei = 0
Underscore_String = []
eingegebene_Buchstaben = []
correct_guess = 0

data = my_datei.read().splitlines()

for x in data:
    int_Rows_datei = int_Rows_datei + 1

Random_int = (random.randint(0,int_Rows_datei))
Random_int = Random_int  - 1
Hangman_Word = data[Random_int]
print("Willkommen zu HANGMAN")
Len_word = (len(Hangman_Word))
Hangman_Word = Hangman_Word.lower()
print("Das gesuchte Wort ist " + str(Len_word) + " Buchstaben lang")

i = 1
while i <= Len_word:
    Underscore_String.append("_")
    i = i + 1

print(" ".join(Underscore_String))

while correct_guess < Len_word:
    input_Letter = input("Welcher Buchstabe? Groß und Kleinschreibung egal!:  ")
    input_Letter = input_Letter.lower()
    if len(input_Letter) > 1:
        print("SO NICHT!. Ein Buchstabe eingeben!")
    elif input_Letter ==  "":
        print("Nichts eingeben geht auch nicht!")
    else:
        if input_Letter in eingegebene_Buchstaben:
            print("Hast du schonmal eingeben!")
        else:
            eingegebene_Buchstaben.append(input_Letter)
            if input_Letter in Hangman_Word:
                index_counter = 0
                print("Buchstabe ist vorhanden")
                for One_Letter in Hangman_Word:
                    if One_Letter == input_Letter:
                        correct_guess = correct_guess + 1
                        Underscore_String[index_counter] = input_Letter
                    index_counter = index_counter + 1    
                print(" ".join(Underscore_String))
            else:
                print("Leider nicht vorhanden")
print("Wort korrekt!")
print("Das gesuchte Wort war: " + Hangman_Word)


