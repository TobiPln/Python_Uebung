user_name = input("Bitte dein Namen eingeben! ")
user_age = input("Bitte dein Alter eingeben! ")

#user_name = str(user_name) -> wandelt user_name in ein String um
#user_age = int(user_age) -> wandelt user_age in ein int um

print(f"Hallo, {user_name} du bist {user_age} Jahre alt!")
print("")
if int(user_age) <= 12:
    print("Du bist noch ein Kind! ")
    print("Du musst um 18 Uhr Zuhause sein! ")

elif int(user_age) <= 16:
    print("Du bist ein Jugendlicher! ")
    print("Prima du darfst bis 20 Uhr raus! ")

elif int(user_age) < 18:
    print("Super du darfst bereits bis 22 Uhr raus! ")

else:
     print("Du bist Erwachsen, mach was du willst! ")


input("Mit Enter Programm beenden! ")