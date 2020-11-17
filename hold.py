import serial
import time
import requests
import json
 
firebase_url = 'https://farmnitorapp.firebaseio.com'
 
#Connect to Serial Port for communication
ser = serial.Serial('COM3', 9600, timeout=0)
 
fixed_interval = 10
 
while 1:
 try:
 #temperature value obtained from Arduino + LM35 Temp Sensor
    moisture = ser.readline()
 #current time and date
    time_hhmmss = time.strftime('%H:%M:%S')
    date_mmddyyyy = time.strftime('%d/%m/%Y')
 
 #current location name
    temperature_location = 'Mumbai-Kandivali';
    
 #insert record
    def main():
        while True:
            time.sleep(2)
            data = ser.readline().decode("utf-8").split()
        if len(data) > 0:
            data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':moisture}
            print(data)
            on_send(data)
            result = firebase.post('/moisture/',data)
   
 
 #insert record
    print(result)
    time.sleep(fixed_interval)
 except IOError:
    print('Error! Something went wrong.')
    time.sleep(fixed_interval)