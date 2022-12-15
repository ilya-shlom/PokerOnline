import socket
import sys
import subprocess
try:
    import redis
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'redis'])

r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('localhost', 8888))

    sock.listen()

    conn, addr = sock.accept()
    while True:
        try:
            print(conn)
            msg = conn.recv(1024)
            if msg:
                msg = msg.decode()
                vals = msg.split()
                print(addr, msg, sep=' : ')
                if vals[0] == "post":
                    r.set(vals[1], vals[2])
                    conn.sendto("саксес".encode(), addr)
                elif vals[0] == "get":
                    conn.sendto(r.get(vals[1]).encode(), addr)
                elif vals[0] == "delete":
                    conn.sendto(r.get(vals[1]).encode(), addr)
                    r.delete(vals[1])
                elif vals[0] == 'search':
                    result = "Found in: "
                    for key in r.scan_iter():
                        if vals[1] in r.get(key):
                            result += f'{key} '
                    conn.sendto(result.encode(), addr)
                else:
                    conn.sendto(b"Wrong command!", addr)
            else:
                conn.sendto(b"No data!", addr)

        except KeyboardInterrupt:
            break
    conn.close()
