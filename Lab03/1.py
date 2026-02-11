#TASK 1
class TrafficAgent:
    def act(self, percept):
        if percept == "Heavy":
            return "Extend green time"
        elif percept == "Light":
            return "Normal green"
        else:
            return "Unknown"

agent = TrafficAgent()

status = input("Enter traffic status(Heavy/Light):")
action = agent.act(status)

print(f"Percept: {status} Traffic")
print(f"Action: {action}")
