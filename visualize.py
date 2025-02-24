import os
import matplotlib.pyplot as plt
import numpy as np


def visualize_solution(maze, path, start, goals, image_path):

    maze_display = np.zeros((*maze.shape, 3), dtype=np.uint8)

    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i, j] == 1:
                maze_display[i, j] = [0, 0, 0]
            else:
                maze_display[i, j] = [255, 255, 255]

    for x, y in path:
        maze_display[x, y] = [255, 0, 255]

    maze_display[start] = [255, 0, 0]
    for g in goals:
        maze_display[g] = [0, 255, 0]

    output_dir = "solved_labs"
    os.makedirs(output_dir, exist_ok=True)

    filename = (
        os.path.basename(image_path).replace(".bmp", "_solved.png").replace("\\", "/")
    )
    output_path = os.path.join(output_dir, filename)

    plt.figure(figsize=(6, 6))
    plt.imshow(maze_display)
    plt.axis("off")
    plt.title("Solución del Laberinto")

    plt.savefig(output_path)
    plt.close()

    print(f"Imagen con solución guardada en: {output_path}")
