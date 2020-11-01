import serial
import time
import threading

class arduino_con():
    def __init__(self, port, baud):
        self._arduinoData = serial.Serial(port, baud)
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

        time.sleep(1)
    
    def update(self):
        print ("start receive arduino data")
        while (True):
            while (self._arduinoData.inWaiting() == 0):
                pass

            # dataPacket = self._arduinoData.readline()
            dataPacket = self.getLatestStatus()
            dataPacket = str(dataPacket, 'utf-8')
            splitPacket = dataPacket.split(',')
            try:
                
                if (splitPacket[0] == 's' and splitPacket[-1] == 'e\r\n'):
                    self.roll = float(splitPacket[3])
                    self.pitch = float(splitPacket[2])
                    self.yaw = float(splitPacket[1])
                # print ("roll: ", self.roll, "pitch: ", self.pitch, "yaw: ", self.yaw)
            except:
                pass

            time.sleep(0.1)

    def run(self):
        arduino_thread = threading.Thread(target=self.update)
        arduino_thread.daemon = True
        arduino_thread.start()

    def getLatestStatus(self):
        while self._arduinoData.inWaiting() > 0:
            status = self._arduinoData.readline()
        return status

    def get_data(self):
        return  [self.roll, self.pitch, self.yaw]
           

if __name__=="__main__": 
    arduinoObj = arduino_con('/dev/ttyACM0', 9600)
    arduinoObj.run()
    # arduinoObj.update()
    
    while True:
        print ("roll: ", arduinoObj.roll, "pitch: ", arduinoObj.pitch, "yaw: ", arduinoObj.yaw)
        # print ("-----------------")
    