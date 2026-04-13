import asyncio
import websockets

async def chat_client():
    async with websockets.connect("ws://localhost:12345") as websocket:
        print("Connected to chat server. Type messages and press Enter.")
        while True:
            msg = input("You: ")
            await websocket.send(msg)
            response = await websocket.recv()
            print("Received:", response)

asyncio.run(chat_client())