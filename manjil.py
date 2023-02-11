import json
import requests
import websocket
import random 
import time
ws=websocket.WebSocket()
# Replace with your user's token
TOKEN = 'BC:DD:C2:82:88:2F'
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
	message = {'value': random.randint(100, 500), 'node': random.randint(1, 5),'temp': random.randint(0,99)}
	message_str = json.dumps(message)
	ws.send(message_str)
	time.sleep(2)

