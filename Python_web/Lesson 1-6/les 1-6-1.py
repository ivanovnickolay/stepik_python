# Разработать простейший TCP echo сервер.
#
# Требования
#
# Запускается на IP адресе 0.0.0.0 и TCP порту 2222
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем с адресом и портом
s.bind(('0.0.0.0 ', 2222))

# слушаем порт
# 10 - длина очереди соединений клиентов
s.listen(10)

while True:
    # получаем соединение и адрес клиента
    conn, addr = s.accept()
    while True:
        # считываем данные
        data = conn.recv(1024)
        if str(data) == 'b\'close\'':
            conn.close()
        if not data : break
        # посылаем данные по соединению
        conn.send(data)
    conn.close()
conn.shutdown(socket.SHUT_RDWR)