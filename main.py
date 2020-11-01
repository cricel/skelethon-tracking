from arduino_con import *
from hm_skeleton import *

if __name__=="__main__": 
    arduinoObj = arduino_con('/dev/ttyACM0', 115200)
    arduinoObj.run()

    operator = hm_skeleton()
    # operator.run()
    
    while True:
        # print (arduinoObj.pitch)
        operator.set_single_rotation("body", 4, arduinoObj.roll, arduinoObj.pitch, arduinoObj.yaw)
        operator.set_single_rotation("neck", 2, arduinoObj.roll, arduinoObj.pitch, arduinoObj.yaw)
        operator.set_single_rotation("upper_arm_left", 2, arduinoObj.roll, arduinoObj.pitch, arduinoObj.yaw)
        # if (arduinoObj.pitch > 30):
        #     print ("-----------------", arduinoObj.pitch)

