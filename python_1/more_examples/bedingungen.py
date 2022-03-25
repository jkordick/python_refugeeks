a = 500
b = 21
if b > a:
    print("b ist größer als a")
elif a == b:
    print("a und b sind gleich")
else:
    print("a ist größer als b")


# Switch-Case: erst ab v3.10 möglich
number = 200
match number:
    case 100:
        print("Die Nummer 100")
    case 200:
        print("Gewonnen mit Nummer 200!")
    case 300:
        print("Die Nummer 200")
    case _:
        print("Diese Nummer kenne ich nicht")
