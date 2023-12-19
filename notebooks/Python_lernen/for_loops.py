#Unterricht 18.12.2023 For-Loops
"""
print("X")
print("X","X","X",sep=" ")
print("X",end="")
print("");print("")

for i in range(4):
    print(i)
print("X")
print("");print("")

    X       X
     X     X
      X   X
       X X
        X
       X X
      X   X
     X     X
    X       X

"""
def draw_tree(height):
    for i in range(1,(height+1)): #Range 1,2,3,4,5
        spaces = " " * (height - i) #Erster Durchlauf: b* 5-1 = bbbb
        stars = "*" * (2 * i - 1) #Erster Durchlauf: * *2*1-1 = *
        print(spaces,stars)
    
    for x in range(2):
        spaces = " " * (int(height-1))
        draw_Stamm = "="
        print(spaces, draw_Stamm)

    

# Beispielaufruf mit einer Höhe von 5
draw_tree(7)


print("TEST123")
