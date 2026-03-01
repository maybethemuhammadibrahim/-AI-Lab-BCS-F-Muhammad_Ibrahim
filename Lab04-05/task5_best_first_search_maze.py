class GoalBasedAgent:
    def __init__(self, goals):
        self.goals = goals

    def formulate_goal(self, percept):
        if percept in self.goals:
            return "goal reached"
        return "searching"

    def best_first_search(self, graph, start, goal):
        frontier = [(start, 0, [start])]
        visited = set()

        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, heuristic, path = frontier.pop(0)

            if node in visited:
                continue
            visited.add(node)

            if node == goal:
                return path

            for neighbour, cost in graph.get(node, []):
                if neighbour not in visited:
                    frontier.append((neighbour, cost, path + [neighbour]))

        return None

    def find_all_goals(self, graph, start, goals):
        current = start
        remaining = list(goals)
        full_path = [start]

        while remaining:
            best_path = None
            best_goal = None
            best_len = float('inf')

            for goal in remaining:
                path = self.best_first_search(graph, current, goal)
                if path and len(path) < best_len:
                    best_path = path
                    best_goal = goal
                    best_len = len(path)

            if best_path is None:
                return f"cannot reach remaining goals: {remaining}"

            full_path.extend(best_path[1:])
            current = best_goal
            remaining.remove(best_goal)
            print(f"reached goal {best_goal}, path so far: {full_path}")

        return f"all goals visited! full path: {full_path}"

    def act(self, percept, graph):
        return self.find_all_goals(graph, percept, self.goals)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)
    print(action)


graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

start_node = 'S'
goals = ['K', 'M', 'E']

agent = GoalBasedAgent(goals)
environment = Environment(graph)
run_agent(agent, environment, start_node)