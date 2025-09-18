import asyncio

async def tcp_client(host='127.0.0.1', port=9000):
    reader, writer = await asyncio.open_connection(host, port)
    print("连接成功！输入消息发送，空行退出。")

    async def send_input():
        loop = asyncio.get_event_loop()
        while True:
            msg = await loop.run_in_executor(None, input, "> ")
            if not msg:
                writer.close()
                await writer.wait_closed()
                break
            writer.write((msg + "\n").encode())
            await writer.drain()

    async def receive():
        while True:
            data = await reader.readline()
            if not data:
                print("服务器关闭")
                break
            print(data.decode().strip())

    await asyncio.gather(send_input(), receive())


if __name__ == "__main__":
    asyncio.run(tcp_client())
