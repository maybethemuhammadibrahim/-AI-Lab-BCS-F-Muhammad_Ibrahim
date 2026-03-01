class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def ucs_search(self, graph, start, goal):
        frontier = [(start, 0)]
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            frontier.sort(key=lambda x: x[1])
            current_node, current_cost = frontier.pop(0)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                return f"goal found! least cost path: {path}, total cost: {current_cost}"

            for neighbor, cost in graph[current_node].items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    frontier.append((neighbor, new_cost))

        return "goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"goal {self.goal} found! already at goal"
        return self.ucs_search(graph, percept, self.goal)


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
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

start_node = 'S'
goal_node = 'G'

agent = GoalBasedAgent(goal_node)
environment = Environment(graph)
run_agent(agent, environment, start_node)