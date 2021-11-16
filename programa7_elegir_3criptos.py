cripto1=None
cripto2=None
cripto3=None

while cripto1 != "BTC" and cripto1 != "BCC" and cripto1 != "LTC" and cripto1 != "ETH" and cripto1 != "ETC" and cripto1 != "XRP":
    cripto1 = input("Ingresar nombre de la criptomoneda nº1: ")
    cant1 = float(input("Ingresar cantidad de la criptomoneda nº1: "))
    cotizacion1 = float(input("Ingresar cotización en USD$ de la criptomoneda nº1: "))
    if cripto1 != "BTC" and cripto1 != "BCC" and cripto1 != "LTC" and cripto1 != "ETH" and cripto1 != "ETC" and cripto1 != "XRP":
        print("ERROR: ingrese una criptomoneda valida (BTC,BCC,LTC,ETH,ETC,XRP)")
while cripto2 != "BTC" and cripto2 != "BCC" and cripto2 != "LTC" and cripto2 != "ETH" and cripto2 != "ETC" and cripto2 != "XRP":   
    cripto2 = input("Ingresar nombre de la criptomoneda nº2: ")
    cant2 = float(input("Ingresar cantidad de la criptomoneda nº2: "))
    cotizacion2 = float(input("Ingresar cotización en USD$ de la criptomoneda nº2: "))
    if cripto2 != "BTC" and cripto2 != "BCC" and cripto2 != "LTC" and cripto2 != "ETH" and cripto2 != "ETC" and cripto2 != "XRP":
        print("ERROR: ingrese una criptomoneda valida (BTC,BCC,LTC,ETH,ETC,XRP)")
while cripto3 != "BTC" and cripto3 != "BCC" and cripto3 != "LTC" and cripto3 != "ETH" and cripto3 != "ETC" and cripto3 != "XRP":
    cripto3 = input("Ingresar nombre de la criptomoneda nº3: ")
    cant3 = float(input("Ingresar cantidad de la criptomoneda nº3: "))
    cotizacion3 = float(input("Ingresar cotización en USD$ de la criptomoneda nº3: "))
    if cripto3 != "BTC" and cripto3 != "BCC" and cripto3 != "LTC" and cripto3 != "ETH" and cripto3 != "ETC" and cripto3 != "XRP":
        print("ERROR: ingrese una criptomoneda valida (BTC,BCC,LTC,ETH,ETC,XRP)")

valor_total=cant1*cotizacion1+cant2*cotizacion2+cant3*cotizacion3

print("El valor Total es de USD$ %10.3f"%valor_total)