import secrets

zeichen = "QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm1234567890"
sonderzeichen = "@!$%&?*+#-_:.()=><,"

pw = ""


while True: 
    try: # etwas, das schief gehen kann
        laenge = int(input("Bitte die Passwortlänge eingeben: "))

        if laenge < 8 or laenge > 64:
            print("Die Passwortlänge muss zwischen 8 und 64 liegen!")
            continue # springt zum nächsten durchlauf der Schleife

        break   # bei gültiger Eingabe wird die Schleife verlassen

    except ValueError: # was soll passieren, wenn es schiefgeht?
        print("Ungültige Eingabe! Bitte eine Zahl zwischen 8 und 64 eingeben!")


sonder = input("Sonderzeichen verwenden? j/n: ")
sonder = sonder.lower()



while sonder != "j" and sonder != "n":
    print("Ungültige Eingabe. Bitte j oder n eingeben!")
    sonder = input(("Sonderzeichen verwenden? j/n: "))
    sonder = sonder.lower()

if sonder == "j":
    pw += secrets.choice(sonderzeichen)
    zeichenpool = zeichen

    for _ in range(laenge - 1):
        pw += secrets.choice(zeichenpool)

else:
    zeichenpool = zeichen
    
    for _ in range(laenge):
        pw += secrets.choice(zeichenpool)



print("Dein Passwort:", pw)
