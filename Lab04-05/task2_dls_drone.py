class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def dls_search(self, graph, node, goal, limit, path, visited):
        #recursion: we go deeper into each branch one node at a time
        #if we hit the depth limit we stop and backtrack
        #if we find the goal we return the path
        #if a node has unvisited children and we havent hit the limit we recurse deeper
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

    def act(self, percept, graph, limit):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"goal {self.goal} found! already at goal"
        visited = []
        result = self.dls_search(graph, percept, self.goal, limit, [], visited)
        print(f"visited nodes: {visited}")
        if result:
            return f"goal {self.goal} found! path: {result}"
        return f"goal not found within depth limit {limit}"


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node, limit):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph, limit)
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
goal_node = 'H'

agent = GoalBasedAgent(goal_node)
environment = Environment(graph)

print("=== depth limit 2 ===")
run_agent(agent, environment, start_node, 2)

print("\n=== depth limit 3 ===")
run_agent(agent, environment, start_node, 3)