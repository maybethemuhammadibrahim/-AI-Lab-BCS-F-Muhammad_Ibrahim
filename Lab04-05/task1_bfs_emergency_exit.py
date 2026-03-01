class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def grid_to_graph(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        graph = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    neighbors = []
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            neighbors.append((nr, nc))
                    graph[(r, c)] = neighbors
        return graph

    def bfs_search(self, graph, start, goal):
        visited = [start]
        queue = [(start, [start])]
        traversal = []

        while queue:
            node, path = queue.pop(0)
            traversal.append(node)

            if node == goal:
                print(f"traversal order: {traversal}")
                return f"goal {goal} found! shortest path: {path}"

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, path + [neighbour]))

        print(f"traversal order: {traversal}")
        return "goal not found"

    def act(self, percept, grid):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"goal {self.goal} found! already at goal"
        graph = self.grid_to_graph(grid)
        return self.bfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, grid):
        self.grid = grid

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.grid)
    print(action)


building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

start_node = (0, 0)
goal_node = (3, 3)

agent = GoalBasedAgent(goal_node)
environment = Environment(building)
run_agent(agent, environment, start_node)