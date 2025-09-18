import socket
import sys
import select

def client(host='127.0.0.1', port=9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.setblocking(False)
    print("连接成功！输入消息发送，空行退出。")

    while True:
        rlist, _, _ = select.select([sys.stdin, s], [], [])
        for r in rlist:
            if r == s:
                data = s.recv(1024)
                if not data:
                    print("服务器关闭")
                    return
                print(data.decode().strip())
            elif r == sys.stdin:
                msg = sys.stdin.readline().strip()
                if not msg:
                    return
                s.sendall(msg.encode())

if __name__ == "__main__":
    client()
