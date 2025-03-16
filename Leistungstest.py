#Erste Aufgabe: Schleife erstellen um 10 Einträge zu generieren 
try:  
    first_experiment_id:int = int(input("Bitte erste Patienten_ID eingeben: "))
    experiments_dic={}
    for i in range(10):
        experiments_dic[first_experiment_id] = {
        "Versuchsleiterin": "Hannah Kleutgens",
        "Datum": "11.03.2025"
        }
        first_experiment_id+=1 
    print(experiments_dic)
except ValueError: #Falscher Wert also kein integer
    print("Achtung Fehler beim Eintippen, bitte eine natürliche Zahl eingeben!")
#Experiments_dic untereinander ausgeben
from pprint import pprint
pprint(experiments_dic)

#Zweite Aufgabe: Schleife erstellen, um die ersten 5 Einträge auszugeben 
first_id=first_experiment_id-10 #Neue Variable definieren, damit bei der ersten ID gestartet wird 
for index in range(first_id,first_id+5):
    print(index,experiments_dic[index])

#Dritte Aufgabe: Anzahl an Geraden Patienten_IDs ausgeben 
Gerade_Zahlen_Id=[]
for i in range(first_id,first_id+10):
    if i%2==0:
        Gerade_Zahlen_Id.append(i)
print(len(Gerade_Zahlen_Id))
