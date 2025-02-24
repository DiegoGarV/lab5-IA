from imageScanner import process_image
from problem import MazeProblem
from search import bfs, dfs, a_star, manhattan_heuristic
from visualize import visualize_solution


def main():
    # Lista de laberintos a procesar
    laberintos = [
        "./laberintos/laberinto1.bmp",
        "./laberintos/laberinto2.bmp",
        "./laberintos/laberinto3.bmp",
    ]

    for image_path in laberintos:
        print(f"\nProcesando: {image_path}")

        # Procesar la imagen
        maze, start, goals = process_image(image_path)

        # Crear el problema
        problem = MazeProblem(maze, start, goals)

        # Ejecutar búsqueda
        solution = a_star(problem, manhattan_heuristic)

        # Guardar la solución en una imagen en lugar de mostrarla
        if solution:
            visualize_solution(maze, solution, start, goals, image_path)
        else:
            print(f"No se encontró solución para: {image_path}")


if __name__ == "__main__":
    main()