import asyncio

clients = set()  # 保存所有客户端 writer 对象

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"新客户端: {addr}")
    clients.add(writer)

    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            message = data.decode().strip()
            print(f"[{addr}] {message}")

            # 广播给其他客户端
            for w in clients:
                if w != writer:
                    w.write(f"[{addr}] {message}\n".encode())
                    await w.drain()
    except Exception as e:
        print(f"客户端 {addr} 异常: {e}")
    finally:
        print(f"客户端 {addr} 断开")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()


async def main(host='127.0.0.1', port=9000):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"服务器启动 {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
