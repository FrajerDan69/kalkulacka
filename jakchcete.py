cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))
operace = input("jakou operaci chcete provést? +, -, *, /, **,** (1/y): ")

s = "+"
o = "-"
n = "*"
d = "/"
m = "**"
od = "** (1/y)"

if operace == "+":
    print(cislo1 + cislo2)
elif operace == "-":
    print(cislo1 - cislo2)
elif operace == "*":
    print(cislo1 * cislo2)
elif cislo2 == 0 and operace == "/":
    print("nelze dělit nulou")
elif operace == "/":
    print(cislo1 / cislo2)
elif operace == "**":
    print(cislo1 ** cislo2)
elif operace == "** (1/y)":
    print(cislo1 ** (1/cislo2))
else:
    print("nesprávná volba")
while True:
    volba = input("chcete pokračovat? ano/ne: ")
    if volba == "ano":
        if operace == "+":
            cislo1 = float(input("Zadejte první číslo: "))
            cislo2 = float(input("Zadejte druhé číslo: "))
            operace = input("jakou operaci chcete provést? +, -, *, /: ")
            print(cislo1 + cislo2)
        elif operace == "-":
            print(cislo1 - cislo2)
        elif operace == "*":
            print(cislo1 * cislo2)
        elif cislo2 == 0 and operace == "/":
            print("nelze dělit nulou")
        elif operace == "/":
            print(cislo1 / cislo2)
        else:
            print("nesprávná volba")
    if volba != "ano":
        break