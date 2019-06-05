import asyncio
import time

# py intrinsic async to load a function with asynchronization property
# coroutine is the new property in python 3.7
async def dispatch(reader) : 
    while True :
        data = reader.readline()
        if data == '' : 
            break
        await asyncio.sleep(0.01)
        print(data)

stream_in = open('./large_file.txt', mode='r')

loop = asyncio.get_event_loop()
loop.run_until_complete(dispatch(stream_in))
loop.close()