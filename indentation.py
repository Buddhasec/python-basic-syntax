"""if 5 > 3:
    print("5 ist größer als 3.")
    print("Dieser Block gehört zum if-Befehl.")
print("Dieser Text steht außerhalb des if-Blocks.")

zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist postitv.")
    if zahl % 2 == 0:
        print("Außerdem ist die Zahl gerade.")
    else:
        print("Außerdem ist die Zahl ungerade.")
elif zahl< 0:
    print("Die Zahl ist negativ.")
    if zahl % -2 == 0:
        print("Außerdem ist die Zahl gerade.")
    else:
        print("Außerdem ist die Zahl ungerade.")
else:
    print("Die Zahl ist null.")"""

"""for i in range(1, 6):
    print(f"Iteration {i}:")
    if i % 2 == 0:
        print(f"{i} ist gerade.")
    else:
        print(f"{i} ist ungerade.")
print("Schleife abgeschlossen.")"""

for i in range(1, 4):
    print(f"Nummer {i}:")
    if i == 2:
        print(f"Nummer {i} erreicht!")
        continue
    print(f" Nummer {i} ist keine Zwei!")
print(f"Fertig!")