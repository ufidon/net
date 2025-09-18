import socket

# -------------------
# 客户端协程
# -------------------
def handle_client(conn, addr, broadcast):
    conn.setblocking(False)
    while True:
        yield "wait_read"
        try:
            data = conn.recv(1024)
        except BlockingIOError:
            continue
        if not data:
            break
        message = data.decode().strip()
        print(f"[{addr}] {message}")

        # 广播给其他客户端
        yield "wait_write"
        for c in broadcast:
            if c != conn:
                try:
                    c.sendall(f"[{addr}] {message}\n".encode())
                except BlockingIOError:
                    continue

    conn.close()
    broadcast.remove(conn)
    print(f"客户端 {addr} 断开")


# -------------------
# 服务器调度器
# -------------------
def run_server(host='127.0.0.1', port=9000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind((host, port))
    server.listen()

    tasks = []          # 所有客户端任务
    broadcast = set()   # 所有客户端连接

    print(f"服务器启动 {host}:{port}")

    while True:
        # 处理新连接
        yield "wait_read_server"
        try:
            conn, addr = server.accept()
            print(f"新客户端: {addr}")
            broadcast.add(conn)
            task = handle_client(conn, addr, broadcast)
            next(task)  # 启动客户端生成器
            tasks.append(task)
        except BlockingIOError:
            pass

        # 处理现有客户端
        for task in tasks[:]:
            try:
                next(task)
            except StopIteration:
                tasks.remove(task)


if __name__ == "__main__":
    server_task = run_server()
    next(server_task)  # 启动服务器生成器

    while True:
        try:
            next(server_task)
        except StopIteration:
            break
