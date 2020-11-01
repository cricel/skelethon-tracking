import time
from multiprocessing import Process


class TestClass():
    def test_f(self):
        ctr = 0
        while True:
            ctr += 1
            print("     ", ctr)
            time.sleep(1.0)


if __name__ == '__main__':
    ## run function in the background
    CT = TestClass()
    p = Process(target=CT.test_f)
    p.start()

    ## will not exit if function finishes, only when
    ## "q" is entered, but this is just a simple example
    stop_char = ""
    while stop_char.lower() != "q":
        stop_char = input("Enter 'q' to quit ")
        print ("sdsd")
        if stop_char.lower() == "u":
            pass
            ## do something else
        print("terminate process")
        if p.is_alive():
            p.terminate()


# //           X Accel  Y Accel  Z Accel   X Gyro   Y Gyro   Z Gyro
# //OFFSETS     -348,    1681,    2218,     128,      86,     -63