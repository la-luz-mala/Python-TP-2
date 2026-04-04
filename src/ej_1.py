def ej1(text):
    # Convierto el texto a un array de líneas 
    linesList = text.split('\n')
    # Calculo la cantidad de palabras por línea y lo guardo en una lista
    wordsPerLine = []
    for line in linesList:
        words = len(line.split())
        wordsPerLine.append(words)

    # Variables auxiliares
    totalLines = len(linesList)
    totalWords = sum(wordsPerLine)
    average = totalWords / totalLines

    resultado = f'Total de líneas: {totalLines}\n'
    resultado += f'Total de palabras: {totalWords}\n'
    resultado += f'Promedio de palabras por línea: {average:.2f}\n\n'
    resultado += f'Lineas por encima del promedio ({average:.2f} palabras):\n'

    for qty, text in zip(wordsPerLine, linesList): #zip convierte 2 listas en una lista de tuplas con elementos de A y B
        if qty > average:
            resultado += f"- \"{text}\" ({qty} palabras)\n"
    return resultado