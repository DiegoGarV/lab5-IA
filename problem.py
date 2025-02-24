from abc import ABC, abstractmethod


class Problem(ABC):

    def __init__(self, initial_state, goal_states):
        self.initial_state = initial_state
        self.goal_states = goal_states

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, action):
        pass

    @abstractmethod
    def goal_test(self, state):
        pass

    @abstractmethod
    def step_cost(self, state, action, new_state):
        pass


class MazeProblem(Problem):

    def __init__(self, maze, start, goals):
        super().__init__(start, goals)
        self.maze = maze
        self.rows, self.cols = maze.shape

    def actions(self, state):
        x, y = state
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        valid_moves = [
            (x + dx, y + dy)
            for dx, dy in possible_moves
            if 0 <= x + dx < self.rows
            and 0 <= y + dy < self.cols
            and self.maze[x + dx, y + dy] == 0
        ]
        return valid_moves

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state in self.goal_states

    def step_cost(self, state, action, new_state):
        return 1
