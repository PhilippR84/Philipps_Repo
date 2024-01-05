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


def draw_tree(height):
    for i in range(1,(height+1)): 
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces,stars)
    
    for x in range(2):
        spaces = " " * (int(height-1))
        draw_trunk = "="
        print(spaces, draw_trunk)

draw_tree(7)


print("TEST123")
"""

vt_Names = ["Philipp", "Alex", "Jonas", "Robin"]
print(vt_Names[2])