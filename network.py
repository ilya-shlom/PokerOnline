import socket
import json
import time
import logging
import threading


class Networking:
    BUFFER_SIZE = 4096  # размер буфера для примем сообщений
    TIME_OUT = 1.0  # время таймаута при ожидании данных в сокет


    def __init__(self, port_no, broadcast=False):
        self.port_no = port_no
        self._socket = self.get_socket(broadcast=broadcast)


    def get_socket(cls, broadcast=False, timeout=TIME_OUT): # <- создание Сокета
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # <- для виндовс
        if broadcast:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(timeout)
        return sock


    def bind(self, to=""): # <- получаем сообщения из определённого порта
        self._socket.bind((to, self.port_no))


    def run_reader_thread(self, callback): # <- поток для данных из сокета
        self.read_running = True


        def reader_job():
            while self.read_running:
                data, _ = self.recv_json()
                if data:
                    callback(data)



        thread = threading.Thread(target=reader_job, daemon=True)
        thread.start()
        return thread


    def recv_json(self): # <- получение json файла
        try:
            data, addr = self._socket.recvfrom(self.BUFFER_SIZE)
            return json.loads(data.decode('utf-8', errors='ignore')), addr
        except socket.timeout:
            pass
        return None, None


    def recv_json_until(self, predicate, timeout): # <- получение json в течение timeout секунд
        t0 = time.monotonic()
        while time.monotonic() < t0 + timeout:
            data, addr = self.recv_json()
            if predicate(data):
                return data, addr
        return None, None


    def send_json(self, j, to): # <- отправить json определённым личностям
        data = bytes(json.dumps(j), 'utf-8')
        return self._socket.sendto(data, (to, self.port_no))


    def send_json_broadcast(self, j): # <- отправить json всем
        return self.send_json(j, "<broadcast>")


    def __del__(self):
        logging.info('Closing socket')
        self._socket.close()
