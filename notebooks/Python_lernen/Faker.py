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
    randomint = random.randint(0,10)
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

for Einzelne_Person in Personen:
    i = 0
    for Person in Personen:
        if Einzelne_Person["Vorname"] == Person["Vorname"]:
            i = i + 1

randomint = RandomInt()
print(f"Name: {Personen[randomint]["Vorname"]} {Personen[randomint]["Nachname"]}, Beruf: {Personen[randomint]["Beruf"]}") 
print(f"Kontaktieren können Sie mich unter der E-Mail {Personen[randomint]["Email-Adresse"]}")


    
      