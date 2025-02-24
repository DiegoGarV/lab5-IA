from queue import Queue, LifoQueue, PriorityQueue


def bfs(problem):
    frontier = Queue()
    frontier.put((problem.initial_state, []))
    explored = set()

    while not frontier.empty():
        state, path = frontier.get()
        if problem.goal_test(state):
            return path + [state]

        if state not in explored:
            explored.add(state)
            for action in problem.actions(state):
                frontier.put((action, path + [state]))

    return None


def dfs(problem):
    frontier = LifoQueue()
    frontier.put((problem.initial_state, []))
    explored = set()

    while not frontier.empty():
        state, path = frontier.get()
        if problem.goal_test(state):
            return path + [state]

        if state not in explored:
            explored.add(state)
            for action in problem.actions(state):
                frontier.put((action, path + [state]))

    return None


def a_star(problem, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, problem.initial_state, []))
    explored = set()

    while not frontier.empty():
        cost, state, path = frontier.get()
        if problem.goal_test(state):
            return path + [state]

        if state not in explored:
            explored.add(state)
            for action in problem.actions(state):
                new_cost = cost + problem.step_cost(state, None, action)
                priority = new_cost + heuristic(action, problem.goal_states)
                frontier.put((priority, action, path + [state]))

    return None


def manhattan_heuristic(state, goal_states):
    return min(abs(state[0] - g[0]) + abs(state[1] - g[1]) for g in goal_states)
