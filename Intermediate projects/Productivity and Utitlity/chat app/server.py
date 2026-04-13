import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket):  # only one argument now
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast to all connected clients
            await asyncio.gather(*[client.send(message) for client in connected_clients])
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(chat_handler, "localhost", 12345):
        print("Chat server started on ws://localhost:12345")
        await asyncio.Future()  # run forever

asyncio.run(main())