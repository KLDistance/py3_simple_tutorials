import asyncio

contents_buf = b''

async def dispatch(reader, writer) : 
    while True : 
        data = await reader.readline()
        message = data.decode().split(' ')
        print(data)
        if data == b'\r\n' : 
            print()
            break
    writer.writelines([
        b'HTTP/1.0 200 OK\r\n', 
        b'Content-Type:text/html; charset=utf-8\r\n', 
        b'Connection: close\r\n',
        b'\r\n', 
        contents_buf,
        b'\r\n'
    ])
    await writer.drain()
    writer.close()

if __name__  == '__main__' : 
    # read in the webpage html file
    fp_contents = open('index.html', mode='r')
    contents_buf = fp_contents.read().encode()
    fp_contents.close()
    # start asyncio server
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(dispatch, '10.21.50.12', 9999, loop=loop)
    server = loop.run_until_complete(coro)
    print('Serving on {}'. format(server.sockets[0].getsockname()))
    try : 
        loop.run_forever()
    except KeyboardInterrupt : 
        print()
    
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()