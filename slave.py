import keyboard
from functions_slave import *
import asyncio
import websockets
import warnings
warnings.filterwarnings("ignore")

KEY_PRESS = []

 
async def recep_key(websocket, Null):
    key = await websocket.recv()

    if key not in KEY_PRESS:
        KEY_PRESS.append(key)
    else:
        cmd = ''
        for input in KEY_PRESS:
            if cmd == '':
                cmd = f"{input}"
            else:
                cmd = f"{cmd}+{input}"

        print(cmd)
        KEY_PRESS.clear()
        print(KEY_PRESS)
        if len(key) == 1:
            keyboard.write(key)

        else :
            keyboard.send(key)
            # Prevoir fin de processus
 
 
 
start_server = websockets.serve(recep_key, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()