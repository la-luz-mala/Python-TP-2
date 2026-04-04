def ej5():
    weight = float(input("Ingrese peso del paquete (kg):"))
    zone = input("Ingrese la zona de destino (local/regional/nacional):").lower()
    match zone:
        case "local":
            return("Costo de envío: " + ("500" if weight < 1 else "1000" if weight < 5 else "2000"))
        case "regional":
            return("Costo de envío: " + ("1000" if weight < 1 else "2500" if weight < 5 else "5000"))
        case "nacional":
            return("Costo de envío: " + ("2000" if weight < 1 else "5000" if weight < 5 else "8000"))
        case _:
            return("Zona no válida. Las zonas disponibles son: local, regional, nacional.")