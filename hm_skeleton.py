from vpython import *
import numpy as np
import threading
import time
import math

#################
#
#       Note
# x,z as base. y as third
# x = cos(yaw)cos(pitch)* length
# z = sin(yaw)cos(pitch) * length
# y = sin(pitch) * length
# -----------------------------
# y,z as base. x as third
# y = - cos(pitch)cos(roll)* length
# z = sin(pitch)cos(roll) * length
# x = sin(roll) * length
#
#
##################

class hm_skeleton():
    def __init__(self):
        ## constant
        self.JOINT_RADIUS = 0.6

        scene.camera.pos = vector (1, 4, 0)

        ## defalut rotation
        self.body_rot = vector(0, 1, 0)
        self.head_rot = vector(0, 1, 0)
        self.shoulder_left_rot = vector(-1, 0, 0)
        self.upper_arm_left_rot = vector(-1, 0, 0)
        self.lower_arm_left_rot = vector(-1, 0, 0)

        ## pose config
        # body
        self.hip_pos = vector(0, 0, 0)
        self.body_pos = vector(self.hip_pos.x, self.hip_pos.y + 4, self.hip_pos.z)
        # head
        self.head_pos = vector(self.body_pos.x, self.body_pos.y + 2, self.body_pos.z)
        # shoulder left
        self.shoulder_left_pos = vector(self.body_pos.x - 2, self.body_pos.y, self.body_pos.z)
        self.elbow_left_pos = vector(self.shoulder_left_pos.x - 2, self.shoulder_left_pos.y, self.shoulder_left_pos.z)
        self.wrist_left_pos = vector(self.elbow_left_pos.x - 2, self.elbow_left_pos.y, self.elbow_left_pos.z)
        # shoulder right
        self.shoulder_right_pos = vector(self.body_pos.x + 2, self.body_pos.y, self.body_pos.z)
        self.elbow_right_pos = vector(self.shoulder_right_pos.x + 2, self.shoulder_right_pos.y, self.shoulder_right_pos.z)
        self.wrist_right_pos = vector(self.elbow_right_pos.x + 2, self.elbow_right_pos.y, self.elbow_right_pos.z)

        ## reference coordinate
        self.x_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(1, 0, 0), color = color.red)
        self.y_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(0, 1, 0), color = color.green)
        self.z_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(0, 0, -1), color = color.blue)

        ## body default drawing
        # body
        self.base_box = box(pos = self.hip_pos, axis = vector(0, 1, 0), size = vector(1, 4, 4), color = color.white)
        self.body = cylinder(pos = self.hip_pos, axis = self.body_rot, size = vector(4, 1, 1), color = color.blue)
        self.body_joint = sphere(pos = self.body_pos, radius = self.JOINT_RADIUS, color = color.green)

        # head
        self.neck = cylinder(pos = self.body_pos, axis = self.head_rot, size = vector(2, 1, 1), color = color.blue)
        self.head = sphere(pos = self.head_pos, radius = 1, color = color.white)

        # left arm
        self.shoulder_left = cylinder(pos = self.body_pos, axis = self.shoulder_left_rot, size = vector(2, 1, 1), color = color.blue)
        self.shoulder_left_joint = sphere(pos = self.shoulder_left_pos, radius = self.JOINT_RADIUS, color = color.green)
        self.upper_arm_left = cylinder(pos = self.shoulder_left_pos, axis = self.upper_arm_left_rot, size = vector(2, 1, 1), color = color.blue)
        self.elbow_left_joint = sphere(pos = self.elbow_left_pos, radius = self.JOINT_RADIUS, color = color.green)
        self.lower_arm_left = cylinder(pos = self.elbow_left_pos, axis = self.lower_arm_left_rot, size = vector(2, 1, 1), color = color.blue)
        self.wrist_left_joint = sphere(pos = self.wrist_left_pos, radius = self.JOINT_RADIUS, color = color.green)

    def update(self):
        while True:            
            self.body.axis = self.body.axis
            self.neck.pos = self.body.axis
            self.shoulder_left.pos = self.body.axis
            self.upper_arm_left.pos = self.shoulder_left.axis

            time.sleep(0.1)
    
    def run(self):
        skeleton_thread = threading.Thread(target=self.update)
        skeleton_thread.daemon = True
        skeleton_thread.start()

    def set_single_rotation(self, part, length, roll, pitch, yaw):
        x = - cos(radians(pitch)) * cos(radians(roll)) * length
        z = sin(radians(pitch)) * cos(radians(roll)) * length
        y = sin(radians(roll)) * length

        setattr(getattr(self, part), 'axis', vector (x, y, z))

        if (part == "body"):
            setattr(getattr(self, 'neck'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))
            setattr(getattr(self, 'shoulder_left'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))
            setattr(getattr(self, 'body_joint'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))

        elif (part == "neck"):
            setattr(getattr(self, 'head'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))

        elif (part == "shoulder_left"):
            setattr(getattr(self, 'shoulder_left_joint'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))
            setattr(getattr(self, 'upper_arm_left'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))

        elif (part == "upper_arm_left"):
            setattr(getattr(self, 'lower_arm_left'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))
            setattr(getattr(self, 'elbow_left_joint'), 'pos', vector (x + getattr(self, part).pos.x, y + getattr(self, part).pos.y, z + getattr(self, part).pos.z))
        # print (getattr(getattr(self, part), 'axis'))

    def set_group_rotation(body, neck, shoulder_left, upper_arm_left, lower_arm_left):
        self.body.axis = vector_cal(body[0], body[1], body[2])
        self.body_joint.pos = self.body.axis

        self.neck.pos = self.body.axis
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.head.pos = self.neck.axis

        self.shoulder_left.pos = self.body.axis
        self.shoulder_left.axis = vector_cal(shoulder_left[0], shoulder_left[1], shoulder_left[2])
        self.shoulder_left_joint.pos = self.shoulder_left.axis
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])
        self.neck.axis = vector_cal(neck[0], neck[1], neck[2])

    def vector_cal(roll, pitch, yaw):
        # x = - cos(radians(pitch)) * cos(radians(roll)) * length
        # z = sin(radians(pitch)) * cos(radians(roll)) * length
        # y = sin(radians(roll)) * length
        # return (vector (x, y, z)))
        pass


        
if __name__=="__main__":
    operator = hm_skeleton()
    operator.run()

    while True:
        pass
        # print ("2222222222222222222222222222222222222222222")