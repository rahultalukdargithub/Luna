import asyncio
import websockets
import os
# Directory to save received files
save_directory = "path-of-your-save-directory"

async def receive_files():
    # Replace 'your_sender_ip_here' with the sender machine's IP address
    sender_ip = 'SENDER-IP'
    uri = f'ws://{sender_ip}:8789'
    async with websockets.connect(uri) as websocket:
        file_count = 1
        while True:
            content = await websocket.recv()
            file_path = os.path.join(save_directory, f'{file_count}.txt')
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Received and saved: {file_path}")
            file_count += 1

asyncio.get_event_loop().run_until_complete(receive_files())
