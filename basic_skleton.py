from vpython import *

scene.camera.pos = vector (1, 4, 0)

# common variable
JOINT_RADIUS = 0.6
# degrees = 

###########
# rotation #################
###########
body_rot = vector(0, 0, 0)
head_rot = vector(0, 1, 0)
shoulder_left_rot = vector(-1, 0, 0)
upper_arm_left_rot = vector(-1, 0, 0)
lower_arm_left_rot = vector(-1, 0, 0)

#######
# pos ####################
#######

# body
hip_pos = vector(0, 0, 0)
body_pos = vector(hip_pos.x, hip_pos.y + 4, hip_pos.z)
# head
head_pos = vector(body_pos.x, body_pos.y + 2, body_pos.z)
# shoulder left
shoulder_left_pos = vector(body_pos.x - 2, body_pos.y, body_pos.z)
elbow_left_pos = vector(shoulder_left_pos.x - 2, shoulder_left_pos.y, shoulder_left_pos.z)
wrist_left_pos = vector(elbow_left_pos.x - 2, elbow_left_pos.y, elbow_left_pos.z)
# shoulder right
shoulder_right_pos = vector(body_pos.x + 2, body_pos.y, body_pos.z)
elbow_right_pos = vector(shoulder_right_pos.x + 2, shoulder_right_pos.y, shoulder_right_pos.z)
wrist_right_pos = vector(elbow_right_pos.x + 2, elbow_right_pos.y, elbow_right_pos.z)

# coordinate
x_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(1, 0, 0), color = color.red)
y_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(0, 1, 0), color = color.green)
z_arrow = arrow(pos = vector(-1, 1, 1), axis = vector(0, 0, -1), color = color.blue)

# body
base_box = box(pos = hip_pos, axis = vector(0, 1, 0), size = vector(1, 4, 4), color = color.white)
body = cylinder(pos = hip_pos, axis = body_rot, size = vector(4, 1, 1), color = color.blue)
body_joint = sphere(pos = body_pos, radius = JOINT_RADIUS, color = color.green)

# head
neck = cylinder(pos = body_pos, axis = head_rot, size = vector(2, 1, 1), color = color.blue)
head = sphere(pos = head_pos, radius = 1, color = color.white)

# left arm
shoulder_left = cylinder(pos = body_pos, axis = shoulder_left_rot, size = vector(2, 1, 1), color = color.blue)
shoulder_left_joint = sphere(pos = shoulder_left_pos, radius = JOINT_RADIUS, color = color.green)
upper_arm_left = cylinder(pos = shoulder_left_pos, axis = upper_arm_left_rot, size = vector(2, 1, 1), color = color.blue)
elbow_left_joint = sphere(pos = elbow_left_pos, radius = JOINT_RADIUS, color = color.green)
lower_arm_left = cylinder(pos = elbow_left_pos, axis = lower_arm_left_rot, size = vector(2, 1, 1), color = color.blue)
wrist_left_joint = sphere(pos = wrist_left_pos, radius = JOINT_RADIUS, color = color.green)

# right arm
shoulder_right = cylinder(pos = body_pos, axis = vector(1, 0, 0), size = vector(2, 1, 1), color = color.blue)
shoulder_right_joint = sphere(pos = shoulder_right_pos, radius = JOINT_RADIUS, color = color.green)
upper_arm_right = cylinder(pos = shoulder_right_pos, axis = vector(1, 0, 0), size = vector(2, 1, 1), color = color.blue)
elbow_right_joint = sphere(pos = elbow_right_pos, radius = JOINT_RADIUS, color = color.green)
lower_arm_right = cylinder(pos = elbow_right_pos, axis = vector(1, 0, 0), size = vector(2, 1, 1), color = color.blue)
wrist_right_joint = sphere(pos = wrist_right_pos, radius = JOINT_RADIUS, color = color.green)

