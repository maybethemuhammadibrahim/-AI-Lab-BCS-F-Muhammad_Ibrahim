class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def dls_search(self, graph, node, goal, limit, path, visited):
        #recursion: at each node we check if its the goal
        #if not and we still have depth budget we try each child
        #we backtrack by popping from path when a branch fails
        #limit decreases by 1 each level so we never go deeper than allowed
        visited.append(node)
        path.append(node)

        if node == goal:
            return path.copy()

        if limit <= 0:
            path.pop()
            return None

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                result = self.dls_search(graph, neighbour, goal, limit - 1, path, visited)
                if result is not None:
                    return result

        path.pop()
        return None

    def ids_search(self, graph, start, goal):
        max_depth = len(graph)
        for depth in range(max_depth):
            print(f"--- depth level {depth} ---")
            visited = []
            result = self.dls_search(graph, start, goal, depth, [], visited)
            print(f"visited: {visited}")
            if result:
                return f"goal {goal} found! path: {result}"
        return "goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"goal {self.goal} found! already at goal"
        return self.ids_search(graph, percept, self.goal)


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
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

start_node = 'A'
goal_node = 'G'

agent = GoalBasedAgent(goal_node)
environment = Environment(graph)
run_agent(agent, environment, start_node)