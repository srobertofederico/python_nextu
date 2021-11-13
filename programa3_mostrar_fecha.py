from datetime import datetime

cripto = input("Nombre de la criptomoneda: ")
cant = float(input("Cantidad de la criptomoneda: "))
cotizacion = float(input("Cotización en US$ del día de la criptomoneda: "))


dt_cripto = datetime.now()
print("Día y hora de la consulta: "+dt_cripto.strftime("%d/%m/%Y | %H:%M:%S"))
