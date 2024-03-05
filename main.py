from PIL import Image

def contar_pixeles(imagen_path):
    # Abrir la imagen
    imagen = Image.open(imagen_path)

    # Obtener las dimensiones de la imagen
    ancho, alto = imagen.size

    # Inicializar un contador de píxeles
    total_pixeles = 0

    # Iterar sobre cada píxel en la imagen
    for x in range(ancho):
        for y in range(alto):
            # Obtener el valor del píxel en la posición (x, y)
            pixel = imagen.getpixel((x, y))

            # Incrementar el contador de píxeles
            total_pixeles += 1

    # Cerrar la imagen
    imagen.close()

    return total_pixeles

# Ruta de la imagen que deseas analizar
ruta_imagen = "ruta/a/tu/imagen.jpg"

# Llamar a la función para contar los píxeles
total_pixeles = contar_pixeles(ruta_imagen)

# Imprimir el resultado
print(f"La imagen tiene un total de {total_pixeles} píxeles.")
