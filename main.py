from PIL import Image
import matplotlib.pyplot as plt

def representar_discreta_con_color(imagen, factor_redimension=10):
    # Redimensionar la imagen a un tamaño más pequeño (para pixelearla)
    ancho, alto = imagen.size
    imagen_pequeña = imagen.resize((ancho // factor_redimension, alto // factor_redimension), Image.NEAREST)
    
    # Redimensionarla de nuevo a su tamaño original para obtener el efecto pixeleado
    imagen_pixeleada = imagen_pequeña.resize((ancho, alto), Image.NEAREST)

    imagen_suavizada = imagen_pequeña.resize((ancho, alto), Image.BOX)
    
    return imagen_suavizada


ruta_imagen = 'laberintos/laberinto1.bmp'
imagen = imagen = Image.open(ruta_imagen)

# Llamar a la función de discresión
imagen_pixeleada_con_color = representar_discreta_con_color(imagen)

# Mostrar las imagenes
plt.figure(figsize=(10, 5))

# Imagen original
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(imagen)
plt.axis('off')

# Imagen pixeleada
plt.subplot(1, 2, 2)
plt.title('Imagen Pixeleada con Colores')
plt.imshow(imagen_pixeleada_con_color)
plt.axis('off')

plt.show()
