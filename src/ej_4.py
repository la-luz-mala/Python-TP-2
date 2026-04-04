def ej4():
    email = input("Ingrese un email:")

    arroba = email.find("@")
    if (
        email.count("@") == 1 and # Contiene exactamente un @.
        not email.startswith("@") and # Tiene al menos un carácter antes del @.
        "." in email[arroba:] and # Tiene al menos un punto (.) después del @.
        not email.endswith(".") and not email.startswith(".") and # No empieza ni termina con @ ni con ..
        len(email.split(".")[-1]) > 1 # La parte después del último punto tiene al menos 2 caracteres (el dominio).
    ):
        return "El email es válido"
    else:
        return "El email no es válido."