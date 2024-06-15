# Proyecto de Detección de Objetos

Este proyecto es una aplicación simple de detección de objetos utilizando OpenCV y Python.

## Requisitos

- Python
- OpenCV-Python
- Numpy

## Configuración del entorno virtual

Es recomendable utilizar un entorno virtual para instalar las dependencias del proyecto. Puedes crear un entorno virtual con el siguiente comando:

```bash
python -m venv env
```

Puedes instalar los paquetes requeridos usando pip:

Para activar el entorno virtual, usa el siguiente comando:
En Windows:
```bash
env\Scripts\activate
```

En Unix o MacOS:

```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

## Uso

El script principal es `detect_objects.py`. Este script carga imágenes de una lista especificada, las convierte a escala de grises, aplica una ecualización de histograma para un mejor contraste, aplica un desenfoque gaussiano, realiza la detección de bordes, encuentra contornos y finalmente dibuja los contornos en la imagen original. También calcula y muestra el número de objetos detectados en la imagen.

Para ejecutar el script, usa el siguiente comando:

```bash
python detect_objects.py
```

## Salida

El script muestra la imagen procesada con los objetos detectados. También guarda la imagen procesada como `contornos.jpg`.

## Nota

Esta es una aplicación simple de detección de objetos y puede que no funcione perfectamente para todos los tipos de imágenes. Es posible que necesites ajustar los parámetros en el script para obtener los mejores resultados para tus imágenes específicas.
