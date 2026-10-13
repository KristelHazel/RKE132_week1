#kirjutada programmi, mis küsib kasutajalt tema nime ja tervitab teda personaalselt.

#Algus
#Küsi kasutajalt eesnimi
#Salvesta väärtus muutujasse first_name
#Väljastab tervituse: "Hello, <eesnimi>!"
#Lõpp

first_name = input("Enter your first name? ")
last_name = input("Enter your last name? ")
print("Hello, " + first_name + " " + last_name + "!")

#f-string
print(f"Hello, {first_name} {last_name}!")

#tehke nii, et programm küsiks kasutajal mitte ainult eesnime, vaid ka perekonnanime ning tervitataks teda nii eesnime kui ka perekonnanimega.