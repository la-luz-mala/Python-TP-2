# Cifrado César
def ej8():
    text = input("Ingrese un mensaje")
    num = input("Ingrese el desplazamiento:")
    cypherText = "" # Inicio mi nuevo texto
    for i in text:
        if i.isalpha(): # Chequeo si es una letra
            base = ord("a") if i.islower() else ord("A") # Lugar en ascii a partir de donde empiezan may / min
            char = (ord(i) - base + int(num)) % 26 # El orden del caracter viejo (menos la base más el desplazamiento, mod total de letras por si hay que dar la vuelta)
            cypherText += chr(base + char) # La base más el orden del nuevo caracter, agregado al texto nuevo
        else:
            cypherText += i # si no es una letra se agrega sin cambios
    result = f"\nMensaje cifrado: {cypherText}\nMensaje descifrado: {text}"
    return result
