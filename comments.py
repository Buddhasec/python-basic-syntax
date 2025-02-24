# Das folgende Programm addiert zwei  Zahlen

# Hier wird einer Variable der Wert 5 zugeteilt
zahl1 = 5 

# Hier wird der zweiten Variable der Wert 10 zugeteilt
zahl2 = 10 

# Hier werden die beiden Variablen addiert.
# Das Ergebnis der Addition wird der Variablen 'ergebnis' zugeteilt
ergebnis = zahl1 + zahl2 

# Wir verwenden hier einen sogenannten f-String (formatted string)
# Ein f-String ermöglicht es, Variablen direkt in einen String einzubetten,
# indem ein 'f' vor die Anführungszeichen gesetzt wird.
# Das ist übersichtlicher, effizienter und lesbarer als andere Methoden, z.B:
#  -"Das Ergebnis ist: " + str(ergebnis) # Umständlicher, da str() notwendig ist
#  -"Das Ergebnis ist: {}".format(ergebnis) # Länger und weniger intuitiv
# Mit einem f-String können wir einfach {ergebnis} in den Text einfügen
print(f"Das Ergebnis ist: {ergebnis}") 

# Mit f-String (empfohlen)
print(f"Das Ergebnis ist: {ergebnis}")

# Mit format()
print("Das Ergebnis ist: {}".format(ergebnis))

# Mit String-Konkatenation
print("Das Ergebnis ist: " + str(ergebnis))