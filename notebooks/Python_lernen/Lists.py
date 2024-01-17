"""
List = ["1", "2", "3", "4", "1", "3"]
print(min(List))
print(max(List))

new_List = []
for x in List:
    if x not in new_List:
        new_List.append(x)

print(new_List)
"""
import datetime
import re
# Track all financial transactions including type amounut and date
#Use a list of diectionaries where each 

Purchase1 = {
  "Type": "Banane",
  "amount": "4",
  "price" : 20,
  "date": datetime.date(2024, 1, 15),
}

Purchase2 = {
  "Type": "Apfel",
  "amount": "2",
  "price" : 10,
  "date": datetime.date(2024, 1, 15),
}

Purchase3 = {
  "Type": "Birne",
  "amount": "1",
  "price" : 5,
  "date": datetime.date(2024, 1, 14),
}

Purchase4 = {
  "Type": "Kiwi",
  "amount": "10",
  "price" : 30,
  "date": datetime.date(2024, 1, 14),
}
List_of_purchase = [Purchase1, Purchase2, Purchase3, Purchase4]

for x in List_of_purchase:
    if x["date"] == datetime.date(2024, 1, 14):
        print(x)

values = [x["date"] for x in List_of_purchase]
print(values)

def sum_up(my_key):
    amount = [x[my_key] for x in List_of_purchase]
    return (sum(amount))
income = sum_up("price")
print(income)


student = {
    'name': 'Rainer Zufall',
    'Alter': 20,
    'Kurse': ['Programmieren', 'Theoretische Informatik', 'Lineare Alegbra']
}

#Ausgaebe mit "f" -> Ausdrücke können in den String verwendet werden
print(f"Name: {student['name']}")
print(f"Alter: {student['Alter']}")
print(f"Kurse: {', '.join(student['Kurse'])}")

#Werte hinzufügen
student['Wohnort'] = 'WÜ'

#Ändern eines Eintrages
student['Alter'] = 23

print(f"Alter: {student['Alter']}")
print(f"Wohnort: {student['Wohnort']}")
