from imageScanner import process_image
from problem import MazeProblem
from search import bfs, dfs, a_star, manhattan_heuristic
from visualize import visualize_solution


def main():
    labs = [
        "./laberintos/laberinto1.bmp",
        "./laberintos/laberinto2.bmp",
        "./laberintos/laberinto3.bmp",
    ]

    for image_path in labs:
        print(f"\nProcesando: {image_path}")

        maze, start, goals = process_image(image_path)

        problem = MazeProblem(maze, start, goals)

        solution = a_star(problem, manhattan_heuristic)

        if solution:
            visualize_solution(maze, solution, start, goals, image_path)
        else:
            print(f"No se encontró solución para: {image_path}")


if __name__ == "__main__":
    main()
