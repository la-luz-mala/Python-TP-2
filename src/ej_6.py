def ej6(text):
    counts = {} # Creo un diccionario vacío
    for post in text: # Recorro una sola vez cada post
        words = set(post.split()) # Elimino las palabras repetidas para no recorrer de más
        for word in words:
            if word.startswith("#"): # Si es una hashtag...
                counts[word] = counts.get(word, 0) + 1 # La sumo al key correspondiente - si no existe, (word, 0) la crea en 0
    trends = sorted(counts.items(), key=lambda x: x[1], reverse=True) # devuelvo el resultado en forma de lista, ordenado de mayor a menor
    result = "Hashtags trending (más de una aparición):\n"
    if len(trends) < 1 or trends[0][1] <= 1: # Si la lista está vacía o la primera tag (la q mas aparece) aparece menos de 2 veces...
        result += "Ninguna - X estuvo silencioso hoy."
    else:
        for item in trends:
            if item[1] > 1:
                result += f"{item[0]}: {item[1]}\n"
    return result