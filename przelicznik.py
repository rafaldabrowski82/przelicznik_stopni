print('''
Witam w programie do przeliczania jednostek stopni Celsjusz <=> Fahrenheita.
Wybierz jedną z opcji poniżej:
''')
print("1. Celsiusz na Fahrenheity")
print("2. Fahrenheity na Celsiusze")
ChosenNumber = int(input("Twój wybór: "))

if(ChosenNumber == 1):
    cels = int(input("Podaj wartość w Celsjuszach: "))
    result = cels + 32
    print(cels, " stopnie Celsjusza, to ",result, " stopni Fahrenheita")
elif(ChosenNumber == 2):
    fahr = int(input("Podaj wartość w Fahrenheita: "))
    result = fahr - 32
    print(fahr, " stopnie Fahrenheita, to ",result, " stopni Celsjusza")