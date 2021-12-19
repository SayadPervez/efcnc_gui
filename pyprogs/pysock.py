import asyncio
import sys
import socketio

x = sys.argv[1]

sio = socketio.Client()
sio.connect("http://localhost:3000")

@sio.event()
def connect():
    print("Connected -pythonsocket")
    sio.emit("_mod.js",x)

@sio.event()
def die(data):
    sio.disconnect()
    exit()