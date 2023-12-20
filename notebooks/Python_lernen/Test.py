#Hallo. Wilkommen im Test.py 
#Hier probiere ich mich aus um Python zu lernen 

#Schleifen 
#For-Schleife

"""
String = "Philipp"
for x in String:
    print (x)

for x in "Philipp":
    print(x)
"""

"""
vt_Names = ["Philipp", "Alex", "Jonas", "Robin"]
for x in vt_Names:
    if x == "Alex":
        print("Hallo Alex")
    else:
        print("Hallo")    
"""

"""
#Funktion
def myFunc():
    Name = "Robin"
    print("Hallo "+ Name)

myFunc()

#Funktion mit globaler Variable
def myFunc():
    global Name
    Name = "Robin"
    print("Hallo "+ Name)

myFunc()
print (Name)

#Variablen definieren und Typ herausfinden
x = float(5)
print(type(x))

a = "Philipp"
print (a[4])

String = "Philipp"
print(len(String))

#Prüfen ob Bestimmter Text in String vorhanden ist
Text = "Hallo mein Name ist Philipp"
print("F" in Text)

#Prüfen ob Text vorhanden ist mit hilfe eines IF-Statements
Text = "Hallo mein Name ist Philipp"
if "mein" in Text:
    print("Das Wort 'mein' ist vorhanden!")
else:
    print("Ist nicht vorhanden")

#Prüfen ob Text vorhanden ist mit hilfe eines IF-Statements mit "NOT"
Text = "Hallo mein Name ist Philipp"
if "mein" not in Text:
    print("Das Wort 'mein' ist nicht vorhanden!")
else:
    print("Ist vorhanden")

#Ausgabe von 3 Index zum 8 
b = "Hello World"
print(b[2:8])


a = "hallo philipp"
print (a.upper())
b = (a.upper())
print (b.lower())



a = "Hello World      "
print (a.strip()+ "Baum")
print (a + "Baum")

print (a.replace("l", "1"))

"""

a = "Hello World      "
print (a.strip()+ "Baum")
print (a + "Baum")