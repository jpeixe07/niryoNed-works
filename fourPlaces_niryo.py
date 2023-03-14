from pyniryo2 import *

robot = NiryoRobot("10.10.10.10")

robot.arm.calibrate_auto()

#A principio, e interessante verificar se e possivel obter resultados satisfatorios
#com x, y, z, pitch e roll com valores arbitrarios, nesse caso teriamos apeans uma solucao finita de m = n
x = 0.28
y = 0.28
z = 0.109
roll = -1.497
pitch = 1.486
yaw = 2.871


def touch_x_positive_y_positive():
    ##Procedimento para tocar o x,y = <0.28, 0.28> com o yaw = -
    global x, y, z,pitch, yaw, roll
    robot.arm.move_to_home_pose()
    robot_joints = robot.arm.inverse_kinematics(x, y, z, roll, pitch, -yaw)
    robot.arm.move_joints(robot_joints)
    print(robot.arm.get_pose())

    return robot_joints #retorna lista de joints

def touch_x_positive_y_negative():
    #Procedimento para tocar o x,y = <0.28, -0.28> com o yaw = -
    global x, y, z, pitch, yaw, roll
    #robot.arm.move_to_home_pose()
    robot_joints = robot.arm.inverse_kinematics(x, -y, z, roll, pitch, -yaw)
    robot.arm.move_joints(robot_joints)

    return robot_joints #retorna lista de joints

def touch_x_negative_y_positive():
    #Procedimento para tocar o x,y = <0.28, 0.28> com o yaw = +
    global x, y, z, pitch, yaw, roll
    #robot.arm.move_to_home_pose()
    robot_joints = robot.arm.inverse_kinematics(-x, y, z, roll, pitch, yaw)
    robot.arm.move_joints(robot_joints)

    return robot_joints #retorna lista de joints

def  touch_x_negative_y_negative():
    #Procedimento para tocar o x,y = <-0.28, -0.28> com o yaw = -
    global x, y, z, pitch, yaw, roll
    #robot.arm.move_to_home_pose()
    robot_joints = robot.arm.inverse_kinematics([-x, -y, z, roll, pitch, -yaw])
    robot.arm.move_joints(robot_joints)
    print(robot.arm.get_pose())

    return robot_joints #retorna lista de joints



robot_joints1 = touch_x_positive_y_positive()
print(robot_joints1)

robot_joints2 = touch_x_positive_y_negative()
print(robot_joints2)

robot_joints3 = touch_x_negative_y_positive()
print(robot_joints3)

robot_joints4 = touch_x_negative_y_negative()
print(robot_joints4)

robot.end()


# robot.arm.move_joints([0.07077611035673557, -0.7512304768730045, -0.44646373646137877, -0.21926659907785373, 0.15177144441088553, 0.16673176465891437])

# robot.tool.grasp_with_tool()

#robot.arm.set_learning_mode(True)

# print(robot.arm.learning_mode.value)


# while(robot.arm.learning_mode.value):
#     print(robot.arm.pose) #joints for joint printing

