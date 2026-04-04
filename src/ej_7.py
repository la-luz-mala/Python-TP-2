# Amigo invisible
import random

def ej7():
    friends = input("Ingrese los participantes (separados por coma):").split(", ") # Ingreso valores
    if len(friends) %2 != 0: # Si son impares, soluciono o doy la chance de salir
        newValue = (input("Ingresaste una cantidad impar de personas! Ingresá una más o 0 para terminar"))
        if newValue == "0":
            return("La lista no se generó")
        friends.append(newValue)
    
    random.shuffle(friends) # Randomizo la lista
    results = []
    
    for i in range(0, int(len(friends))):
        gifter = friends[i] # Asigno la persona que va a regalar
        giftee = friends[(i + 1) % len(friends)] # Recibe el de al lado y si quien regala es último, el % len da 0 y da la vuelta.
        results.append((gifter, giftee)) # Agrego el resultado como tupla
    result = "Sorteo de amigo invisible:\n"
    for item in results:
        result += f"{item[0]} → {item[1]} \n"
    return result