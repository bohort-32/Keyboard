# Send the key
def end_key(key):
    print(f'FIN')


import asyncio
import websockets
import warnings
warnings.filterwarnings("ignore")
 
async def send_key(key):
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send(key)