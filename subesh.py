import json
import requests
import websocket
import random 
import time
import serial
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200)
ws=websocket.WebSocket()
# Replace with your user's token
TOKEN = '30:C6:F7:1F:BB:7B'
url = 'ws://127.0.0.1:8000/dashboard?token='+TOKEN
# Connecting to the server and handle connection errors
connected = False
while not connected:
    try:
        ws.connect(url)
        connected = True
    except websocket.WebSocketConnectionClosedException:
        print("Failed to connect to the server. Retrying in 5 seconds")
        time.sleep(2)
while(True):
    serial_data = ser.readline().decode("utf-8")
    # Parse the serial data as a JSON string
    try:
        serial_data_dict = json.loads(serial_data)
        # Extract the values you need from the serial data
        value = serial_data_dict['hum']
        node = serial_data_dict['node']
        temp = serial_data_dict['temp']
        message = {'value': int(value), 'node': int(node),'temp': int(temp)}
        message_str = json.dumps(message)
        ws.send(message_str)
        print(message_str)
        time.sleep(1)
    except:
        print(serial_data)
