#importing serial module(need pyserial)
import serial

try:
  arduino = serial.Serial(timeout = 1, baudrate = 9600)
except:
  print('Check port')
  
rawData = []

def clean(L):
  newl = []
  
  for i in range(len(L)):
      temp = L[i][2:]
      newl.append(temp[:-5])
  return newl

cleanData = clean(rawData)

#write to file function
def write(L):
  file = open("data.txt", mode = 'w')
  
  for i in range(len(L)):
    file.write(L[i] + '\n')
    
  file.close()
  
#currently receives data indefinitely
while True:
  rawData.append(str(arduino.readline()))

write(cleanData)  

