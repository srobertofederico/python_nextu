cripto = input("Nombre de la criptomoneda: ")
cant = float(input("Cantidad de criptomonedas: "))
dias = int(input("Cantidad de dias a negociar: "))
ganancia = float(input("Porcentaje a ganar por día: %"))

ganancia_total = cant*ganancia/100*dias
cant_total = cant+ganancia_total

print("La ganancia de",cripto,"durante los",str(dias),"días es",str(ganancia_total))
print("El monto total de",cripto,"a los",str(dias),"días es de",str(cant_total))
