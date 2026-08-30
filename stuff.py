class Robot:

    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery_level = battery_level

        @classmethod
        def robot_move(value):
            if battery_level == 0:
                return f"{self.name} has \
            no battery left and cannot move."

            if (battery_level - value*0.5) <= 0:
                mov = battery_level//(value*0.5)

            mov = battery_level - value*0.5 
            return f"{self.name} moved {mov} units.\
            Battery level is now {value.battery_level}%"

        @classmethod
        def robot_charge(value):
            battery_level += value
            if battery_level > 100:
                battery_level = 100
            return f"{self.name} charged. Battery level is\
         now {value.battery_level}%"


robot_name = Robot(input())
while True:
    user, val =  input().split(" ")
    if user == "move":
        robot_move(int(val))
    elif user == "charge":
        robot_charge(int(val))
    elif user == "quit":
        break

