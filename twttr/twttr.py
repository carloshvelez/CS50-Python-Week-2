palabra = input("Input: ")
lista_letras = ["a", "e", "i", "o", "u"]

for i in palabra:
    if i.lower() in lista_letras:
        print("", end = "")
    else:
        print(i, end = "")
print("")
