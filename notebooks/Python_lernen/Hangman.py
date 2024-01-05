import random
Words = []
with open("Hangman_words.txt","r",encoding="UTF8") as datei:
    int_Rows_datei = 0
    for x in datei:
        int_Rows_datei = int_Rows_datei + 1
        line_Words = x
        Words.append(line_Words)

Random_int = (random.randint(0,int_Rows_datei))
Random_int = Random_int  - 1
print(Words[Random_int])
print(Words)

