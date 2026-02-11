#TASK 4
class UtilityAgent:
    def __init__(self):
        self.restaurants = {
            "A": {"distance": 3, "rating": 7},
            "B": {"distance": 5, "rating": 9}
        }

    def calculate_utility(self):
        best_restaurant = None
        max_utility = -100

        for name, data in self.restaurants.items():
            utility = data["rating"] - data["distance"]
            print(f"Restaurant {name} Utility = {utility}")

            if utility > max_utility:
                max_utility = utility
                best_restaurant = name

        return best_restaurant

agent = UtilityAgent()
selected = agent.calculate_utility()
print(f"\nSelected Restaurant: {selected}")
