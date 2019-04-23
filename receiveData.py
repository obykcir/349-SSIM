#importing serial module(need pyserial)
import serial

try:
  arduino = serial.Serial(timeoout = 1, baudrate = 9600)
except:
  print('Check port')
  
rawData = []

#write to file function
def write(L):
  file = open("data.txt", mode = 'w')
  
  for i in range(len(L)):
    file.write(L[i] + '\n')
    
  file.close()
  
#currently receives data indefinitely
while True:
  rawData.append(str(arduino.readline()))

#write(rawData)  

