import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем с адресом и портом
s.bind(('127.0.0.1', 1234))

# слушаем порт
# 10 - длина очереди соединений клиентов
s.listen(10)

while True:
    # получаем соединение и адрес клиента
    conn, addr = s.accept()
    while True:
        # считываем данные
        data = conn.recv(1024)
        if not data: break
        # посылаем данные по соединению
        conn.send(data)

    conn.close()



