# CHANGELOGS:
    # supports Windows only

import asyncio
import websockets
import os
import platform
import time

PORT = 6969 # no need to change this.

system = platform.system()
if system != "Windows":
    print("sorry! but you need windows for this to work.")
    time.sleep(1)
    exit()

async def shutdown_device():
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 1")
    else:
        print("Unsupported OS.")

async def sleep_device():
    system = platform.system()
    if system == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep") # make sure you have hibernation disabled
    else:
        print("Unsupported OS.")

async def kill_roblox():
    system = platform.system()
    if system == "Windows":
        os.system("taskkill /F /IM RobloxPlayerBeta.exe")
    else:
        print("Unsupported OS.")

async def handler(websocket, path):
    async for message in websocket:
        if message.lower() == "shutdown":
            await shutdown_device()
        elif message.lower() == "sleep":
            await sleep_device()
        elif message.lower() == "kill_roblox":
            await kill_roblox()

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"hosting server on: {PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exited.")

