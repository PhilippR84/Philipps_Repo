from faker import Faker
import random

fake = Faker()
Email_Endungen = ["web", "gmx", "outlook", "yahoo", "mirFälltNixEin"]
Personen = []
def build_email(Person, Email_Endungen):
    Mailendung = random.choice(Email_Endungen)
    Email = (Person["Vorname"] + "." + Person["Nachname"] + "@" + Mailendung + ".de")
    return Email

def RandomInt():
    randomint = random.randomint(10)
    return randomint

for _ in range(10):
    Person = {
        "Vorname": fake.first_name(),
        "Nachname": fake.last_name(),
        "Beruf": fake.job(),        
    }
    Email = build_email(Person, Email_Endungen)
    Person["Email-Adresse"] = Email
    Personen.append(Person)

#Hier muss noch was gemacht werden!
for Vorname in Personen["Vorname"]:
    i = 0
    for Vorname2 in Personen["Vorname"]:
        if Vorname == Vorname2:
            i = i + 1

randomint = RandomInt()
print(Personen[1][Vorname])


    
      