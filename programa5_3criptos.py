cripto1=input("Ingrese el nombre de la primera criptomoneda: ")
cant1=float(input("Ingrese el monto de la primera criptomoneda: "))
cripto2=input("Ingrese el nombre de la segunda criptomoneda: ")
cant2=float(input("Ingrese el monto de la segunda criptomoneda: "))
cripto3=input("Ingrese el nombre de la tercera criptomoneda: ")
cant3=float(input("Ingrese el monto de la tercera criptomoneda: "))

if cant1 >= cant2 and cant1 >= cant3:
    print(cripto1,cant1)
    if cant2 >= cant3:
        print(cripto2,cant2)
        print(cripto3,cant3)
    else:
        print(cripto3,cant3)
        print(cripto2,cant2)
elif cant2 >= cant1 and cant2 >= cant3:
    print(cripto2,cant2)
    if cant1 >= cant3:
        print(cripto1,cant1)
        print(cripto3,cant3)
    else:
        print(cripto3,cant3)
        print(cripto1,cant1)
else:
    print(cripto3,cant3)
    if cant1 >= cant2:
        print(cripto1,cant1)
        print(cripto2,cant2)
    else:
        print(cripto2,cant2)
        print(cripto1,cant1)