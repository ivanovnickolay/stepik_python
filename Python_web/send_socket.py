# как записывать сокет
def mysend(sock, msg):
    totalsent = 0
    # len(msg) длина документа
    while totalsent < len(msg):
        # сколько байт удалось отправить
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError('broken')
        totalsend = totalsent + sent