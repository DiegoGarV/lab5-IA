from PIL import Image
import matplotlib.pyplot as plt

def cargar_imagen(ruta):
    # Cargar la imagen
    imagen = Image.open(ruta)
    
    # Pasar a escala de grises
    imagen_gray = imagen.convert('L')
    
    # Mostrar imagenes
    plt.figure(figsize=(10, 5))
    
    # Imagen original
    plt.subplot(1, 2, 1)
    plt.title('Imagen Original')
    plt.imshow(imagen)
    plt.axis('off')
    
    # Imagen en escala de grises
    plt.subplot(1, 2, 2)
    plt.title('Escala de Grises')
    plt.imshow(imagen_gray, cmap='gray')
    plt.axis('off')
    
    plt.show()
    
    return imagen_gray



ruta_imagen = 'laberintos/laberinto1.bmp'
imagen_gray = cargar_imagen(ruta_imagen)

