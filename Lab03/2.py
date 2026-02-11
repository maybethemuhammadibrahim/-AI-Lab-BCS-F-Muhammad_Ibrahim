#TASK 2
import random

class ClassroomEnvironment:
    def __init__(self):
        self.lights_on = False

    def get_percept(self):
        return random.choice([True, False])

    def update_lights(self, status):
        self.lights_on = status

class LightControllerAgent:
    def __init__(self):
        self.model = {'students': False, 'lights': False}

    def act(self, students_present, environment):
        self.model['students'] = students_present
        self.model['lights'] = environment.lights_on

        action = "No action"

        if self.model['students'] and not self.model['lights']:
            action = "Turn lights ON"
            environment.update_lights(True)
        elif not self.model['students'] and self.model['lights']:
            action = "Turn lights OFF"
            environment.update_lights(False)

        print(f"Model: {self.model}")
        return action

env = ClassroomEnvironment()
agent = LightControllerAgent()

for i in range(8):
    students = env.get_percept()
    action = agent.act(students, env)
    print(f"Step {i+1}: Students: {students}, Light Status: {env.lights_on}, Action: {action}")
    print("------------------------------")
