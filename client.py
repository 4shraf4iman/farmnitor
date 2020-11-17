import websocket
import serial
import json
from firebase import firebase
try:
    import thread
except ImportError:
    import _thread as thread
import time
firebase = firebase.FirebaseApplication('https://farmnitorapp.firebaseio.com/moisture/', None)
def on_message(ws, message):
    wsData = json.loads(message)
    if wsData["APP_ID"] == "SAGS":
        if wsData["body"]["from"] == "app":
            print(wsData["body"]["data"])
            arduino.write(wsData["body"]["data"].encode())

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        main()
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

def on_send(data):
    ws.send('{"APP_ID":"SAGS", "body":{"data":' + data + ', "from" : "arduino"}}')

def main():
    while True:
        time.sleep(2)
        date = time.strftime('%H:%M:%S')
        time_now = time.strftime('%d/%m/%Y')
        data = arduino.readline().decode("utf-8").split()
        if len(data) > 0:
            data = ' Moisture : ' + data[0] + ' Water Pump : ' + data[1] + ' Time : ' + time_now  + ' Date : ' + date 
            print(data)
            on_send(data)
            result = firebase.post('/Moisture/',data)
            print(result)

            data = ' Spray Status:  ' + ' Activated !  ' +' Time :  ' + time_now  + ' Date : ' + date 
            print(data)
            on_send(data)
            result = firebase.post('/Spray/',data)
            print(result)
            
if __name__=='__main__':
    try:
        arduino = serial.Serial('COM3', '9600')
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://damp-reaches-33149.herokuapp.com",
                                  on_message = on_message,
                                  on_error = on_error,
                                  on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
    except:
        print("Arduino Not Detected. Plug-in Arduino and restart program")