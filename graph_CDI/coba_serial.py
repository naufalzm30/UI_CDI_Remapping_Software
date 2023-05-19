# import serial as s

# import time

# serialcomm = s.Serial('COM5', 115200)

# serialcomm.timeout = 1

# while True:

#     # i = input("Enter Input: ").strip()
#     i="on"
#     if i == "Done":

#         print('finished')

#         break

#     serialcomm.write(i.encode())

#     time.sleep(0.5)

#     # print(serialcomm.readline())

# serialcomm.close()


import serial
import time

# Open the serial port at the desired baud rate
ser = serial.Serial('COM5', 115200)

# Define the data to be sent as a byte string
data = b"on"

# Send the data over the serial port
# for i in range(5):
#     # ser.flush()
#     ser.write(b"on")
#     ser.read(6) 
#     # ser.flush()
#     ser.write(b"off")
#     ser.read(7) 
#     # ser.flush()

import struct
import numpy as np
# value = [20.5, 30.45, 300.89, 20.39, 13.37]  # arbitrary float 
value = [10,100,1000,10000] 
# value = [20]   
bin =[]

for x in value:
    # a = struct.pack('f', x)
    # bin.append(a)
    # ser.flush()
    ser.write(hex(np.uint16(x)).encode())
    # ser.read(8)
    # ser.flush()


# for b in bin:
#     for s in b:
#         ser.write(s)




# Close the serial port
ser.close()
