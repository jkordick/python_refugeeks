# print(len("string")) # 6

# print(round(0.12345, 2)) # 0.12

# print(float('3.14')) # 3.14 als Zahl

# # selbst funktionen definieren
# def calculateExponent(base, power):
#     result = base ** power
#     return result # ** ist das gleiche wie ^

# # aufruf 
# print(calculateExponent(2, 2)) # 4

# # frei von Seiteneffekten
# def double(x):
#     x = x * 2

# y = 3
# double(y)

# print(y) # bleibt 3


list = [2, 4]

def doubleList():
    for i in range(len(list)):
        list[i] = list[i] * 2

doubleList()

print(list) # [4, 8]