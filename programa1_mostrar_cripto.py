nombreCripto = input("Nombre de la criptomoneda: ")
cantCripto = float(input("Cantidad de la criptomoneda: "))
cotizacion = float(input("Cotización en US$ del día de la criptomoneda: "))

valorTotal = cantCripto * cotizacion

print("El valor total es US$ " +str(valorTotal))
