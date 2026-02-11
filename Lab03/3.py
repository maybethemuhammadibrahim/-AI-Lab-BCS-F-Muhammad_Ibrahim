#TASK 3
class GoalBasedAgent:
    def __init__(self):
        self.subjects = ["AI", "Math", "Physics"]
        self.goal = []

    def act(self):
        while self.subjects != self.goal:
            current_subject = self.subjects.pop(0)
            print(f"Studying {current_subject}")

        print("Goal Achieved all subjects completed")

agent = GoalBasedAgent()
agent.act()
