
from my_functions import build_person, build_experiment

if __name__ == "__main__":
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    sex = input("Geschlecht: ")
    age = input("Alter: ")

supervisor = build_person("Max", "Mustermann", "male", "30")
subject = build_person(first_name, last_name, sex, age)

experiment = build_experiment("Herzfrequenz-Analyse", "19.03.2025", supervisor, subject)

print(experiment)

