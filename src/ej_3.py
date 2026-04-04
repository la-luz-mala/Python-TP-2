# Importo Regular Expressions para poder usar ignorecase, para no tener 
# que hacer varios reemplazos (ej. si comparo "marte" con "Marte")
import re 
def ej3(review):
    spoilers = [word.strip().lower() for word in input("Ingrese las palabras spoiler (separadas por coma):").split(", ")]

    # Defino la función de reemplazo usando IGNORECASE
    for item in spoilers:
        review = re.sub(re.escape(item), "*" * len(item), review, flags=re.IGNORECASE)

    # Output
    return review
