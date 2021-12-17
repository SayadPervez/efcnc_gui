import socketio,uvicorn

sio = socketio.AsyncServer(async_mode="asgi")
static_files={
    "/":"./public/"
}
app = socketio.ASGIApp(sio,static_files=static_files)

@sio.event
async def connect(sid,environ):
    print(sid,"connected")

@sio.event
async def disconnect(sid):
    print(sid,"disconnected")

#sio.emit('Process Confirmation', {'status': 'foobar'})

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=3000)