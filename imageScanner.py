import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def process_image(image_path, grid_size=20):
    # Cargar la imagen
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rango de colores
    fisrt_red, second_red = np.array([0, 100, 100]), np.array([10, 255, 255])
    first_green, second_green = np.array([50, 100, 100]), np.array([70, 255, 255])
    mask_red = cv2.inRange(hsv, fisrt_red, second_red)
    mask_green = cv2.inRange(hsv, first_green, second_green)

    # Tamaño de la imagen
    height, width = binary.shape
    rows, cols = height // grid_size, width // grid_size
    maze_grid = np.zeros((rows, cols), dtype=int)

    # Identificación de paredes, inicio y metas
    start = None
    goals = set()

    for i in range(rows):
        for j in range(cols):
            block = binary[
                i * grid_size : (i + 1) * grid_size, j * grid_size : (j + 1) * grid_size
            ]

            # Detectar paredes
            if np.mean(block) < 128:
                maze_grid[i, j] = 1

            # Detectar inicio (rojo)
            elif start is None and np.any(
                mask_red[
                    i * grid_size : (i + 1) * grid_size,
                    j * grid_size : (j + 1) * grid_size,
                ]
                > 0
            ):
                start = (i, j)

            # Detectar metas (verde)
            elif (i, j) not in goals and np.any(
                mask_green[
                    i * grid_size : (i + 1) * grid_size,
                    j * grid_size : (j + 1) * grid_size,
                ]
                > 0
            ):
                goals.add((i, j))

    goals = list(goals)

    output_dir = "laberintos_discretos"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar la imagen discretizada
    plt.figure(figsize=(6, 6))
    plt.imshow(maze_grid, cmap="gray_r")
    plt.scatter(start[1], start[0], color="red", label="Inicio")
    for g in goals:
        plt.scatter(g[1], g[0], color="green", label="Meta")
    plt.legend()
    plt.title("Laberinto Discretizado")

    # Obtener el nombre base del archivo y guardar la imagen
    filename = os.path.basename(image_path).replace(".bmp", ".png")
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path)
    plt.close()

    print(f"Imagen discretizada guardada en: {output_path}")

    return maze_grid, start, goals