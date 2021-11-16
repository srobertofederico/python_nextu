btc = 64000.00
dash = 226.51
ltc = 256.55
moneda = input("Escriba la criptomoneda que desea utilizar (BTC, DASH o LTC): ")
if moneda == "BTC" or moneda == "DASH" or moneda == "LTC":
    cantidad = float(input("Ingrese la cantidad que desea utilizar: "))
    if moneda == "BTC":
        monto = cantidad * btc
    elif moneda == "DASH":
        monto = cantidad * dash
    else:
        monto = cantidad * ltc
    print("La cantidad de USD recargado fue de: "+str(monto))
else:
    print("ERROR: solo se permite utilizar USD, DASH o LTC")
