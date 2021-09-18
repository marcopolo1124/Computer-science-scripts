class Robot:
    num = 0
    def __init__(self):
        Robot.num += 1


robot1 = Robot()
robot2 = Robot()
robot3 = Robot()

print(robot3.num)

