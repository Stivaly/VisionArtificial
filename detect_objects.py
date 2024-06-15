import cv2
import numpy as np

# Cargar imagen
image_files = ['decoracion-mesa-oficina-1600x980-3672599827.jpg', 'manteles-y-frutas-sobre-mesa-anne-songhurst_11-1311094030.jpg', 'objetos-mesa_274679-982-1393798751.jpg', 'tablero-de-la-mesa-creativo-con-los-objetos-110672935-1785905410.jpg']

for image_file in image_files:
    # Cargar imagen
    image = cv2.imread(image_file)

    # Imagen cargada
    cv2.imshow('Imagen Original', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ecualizar el histograma de la imagen en escala de grises
    gray = cv2.equalizeHist(gray)

    # Ajustar el contraste y el brillo
    alpha = 1.5 # Factor de contraste (1.0-3.0)
    beta = 0   # Brillo (0-100)
    adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

    # Mostrar la imagen con los contornos dibujados
    cv2.imshow('Escala de grises', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Aplicar un filtro de suavizado
    smoothed = cv2.GaussianBlur(adjusted, (15, 15), 0)

    # Aplicar la detección de bordes
    edges = cv2.Canny(smoothed, 100, 200)

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Calcular el número de objetos detectados
    num_objects = len(contours)

    # Mostrar el número de objetos detectados en la imagen
    cv2.putText(image, 'Objetos detectados: {}'.format(num_objects), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)

    # Mostrar la imagen con los contornos dibujados
    cv2.imshow('Contornos de la imagen', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Guardar la imagen con los contornos dibujados
    cv2.imwrite('contornos.jpg', image)

    print('Número de objetos detectados en {}: {}'.format(image_file, num_objects))