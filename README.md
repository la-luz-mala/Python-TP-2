# Proyecto de Ejercicios Python 
**Nombre: María Luz Davico**
**Legajo: 12087/2**

Este proyecto contiene los ejercicios resueltos correspondientes al Trabajo Práctico 2 de la materia Seminario de Python 2026, Facultad de Informática, UNLP.

## 📂 Estructura del Proyecto

El proyecto sigue una estructura que separa la lógica de las funciones de la ejecución visual:

- **src/**: Contiene los archivos `.py` con la lógica de las funciones (ej. `procesamiento.py`, `validaciones.py`).
- **notebooks/**: Contiene los archivos Jupyter Notebook (`.ipynb`) desde donde se importan y ejecutan las funciones.
- **README.md**: Guía de uso e instalación.

## 🛠️ Requisitos e Instalación

Este proyecto utiliza únicamente la **Standard Library** de Python, por lo que no es necesario instalar librerías de terceros.

### Requisitos
- **Python 3.10+**
- **Jupyter Notebook** o **VS Code** con la extensión de Jupyter.

### Instalación
1. Clona este repositorio o descarga los archivos.
2. Asegurate de mantener la estructura de carpetas para que las importaciones funcionen correctamente.

## 🚀 Ejecución

1. Abrí la carpeta del proyecto en tu editor (yo uso Antigravity pero lo que te haga feliz).
2. Dirigite a la carpeta `notebooks/`.
3. Abrí el archivo `.ipynb` correspondiente.
4. Ejecutá las celdas - es importante ejecutar la primera celda siempre para activar el routing y que Python localice las funciones sin errores.

## 📝 Librerías Utilizadas
- `re`: Para el procesamiento de textos y censura de spoilers (uso de `IGNORECASE`).
- `random`: Para la generación de pares en el sorteo de Amigo Invisible.
- `sys`: Para la gestión de rutas y conexión entre carpetas.
