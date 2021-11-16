import random

cripto=input("Inserte el nombre de la criptomoneda: ")
cant=float(input("Inserte el monto de la criptomoneda: "))
count=0

while count <= 7:
    porcentaje_aleatorio = random.uniform(-0.03,0.03)
    cantidad_total = cant + (cant*porcentaje_aleatorio)
    count=count+1
    print("el saldo de",cripto,"el día",str(count),"es de %6.7f"%cantidad_total+". Ganancia de %6.2f"%(porcentaje_aleatorio*100),"%")