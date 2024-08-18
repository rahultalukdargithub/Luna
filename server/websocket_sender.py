import asyncio
import os
import websockets
import glob

# Directory to watch for new files
watch_directory = 'path-of-your-send-directory'

async def send_files(websocket, path):
    sent_files = set()
    while True:
        # Get a sorted list of text files in the directory
        files = sorted(glob.glob(os.path.join(watch_directory, '*.txt')))
        for file in files:
            if file not in sent_files:
                with open(file, 'r') as f:
                    content = f.read()
                await websocket.send(content)
                print(f"Sent: {file}")
                sent_files.add(file)
        await asyncio.sleep(1)  # Check for new files every second
# Replace 'localhost' with the sender machine's IP address
sender_ip = 'SENDER-IP'
start_server = websockets.serve(send_files, sender_ip, 8787)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

