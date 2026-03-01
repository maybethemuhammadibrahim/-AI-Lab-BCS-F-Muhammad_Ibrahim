import random

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def astar_search(self, graph, start, goal, heuristic):
        frontier = [(start, 0, heuristic[start], [start])]
        visited = set()
        cost_so_far = {start: 0}

        while frontier:
            frontier.sort(key=lambda x: x[2])
            node, g_cost, f_cost, path = frontier.pop(0)

            if node in visited:
                continue
            visited.add(node)

            if node == goal:
                return path, g_cost

            for neighbor, cost in graph[node].items():
                new_g = g_cost + cost
                new_f = new_g + heuristic[neighbor]
                if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_g
                    frontier.append((neighbor, new_g, new_f, path + [neighbor]))

        return None, float('inf')

    def dynamic_astar(self, graph, start, goal, heuristic, changes):
        path, cost = self.astar_search(graph, start, goal, heuristic)
        print(f"initial path: {path}, cost: {cost}")

        for edge, new_cost in changes:
            node_a, node_b = edge
            old_cost = graph[node_a].get(node_b, None)
            if old_cost is not None:
                print(f"\nedge {node_a}-{node_b} changed from {old_cost} to {new_cost}")
                graph[node_a][node_b] = new_cost

                #recompute only if changed edge is on current path
                affected = False
                for i in range(len(path) - 1):
                    if path[i] == node_a and path[i+1] == node_b:
                        affected = True
                        break

                if affected:
                    print("path affected, recomputing from affected node...")
                    recompute_start = node_a
                    prefix = path[:path.index(node_a)]
                    prefix_cost = 0
                    for i in range(len(prefix) - 1):
                        prefix_cost += graph[prefix[i]][prefix[i+1]]

                    new_path, new_cost = self.astar_search(graph, recompute_start, goal, heuristic)
                    if new_path:
                        full_path = prefix + new_path
                        total_cost = prefix_cost + new_cost
                        path = full_path
                        cost = total_cost
                        print(f"new path: {path}, cost: {cost}")
                    else:
                        print("no path found after recomputation")
                else:
                    print("path not affected, no recomputation needed")

        return f"\nfinal path: {path}, total cost: {cost}"

    def act(self, percept, graph, heuristic, changes):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"goal {self.goal} found! already at goal"
        return self.dynamic_astar(graph, percept, self.goal, heuristic, changes)


class Environment:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node, changes):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph, environment.heuristic, changes)
    print(action)


graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

start_node = 'A'
goal_node = 'G'

#simulating dynamic edge cost changes
changes = [
    (('A', 'B'), 8),
    (('B', 'E'), 7)
]

agent = GoalBasedAgent(goal_node)
environment = Environment(graph, heuristic)
run_agent(agent, environment, start_node, changes)