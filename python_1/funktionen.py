def say_hello():
    return 'Hello'

# print(say_hello())


def addition(erster_wert, zweiter_wert):
    ergebnis = erster_wert + zweiter_wert
    return int(ergebnis)

#print(addition(7, 3))


def subtraktion(zweiter_wert):
    erster_wert_neu = addition(1, 5)  # 6
    ergebnis = erster_wert_neu - zweiter_wert
    return int(ergebnis)


print(subtraktion(2))

