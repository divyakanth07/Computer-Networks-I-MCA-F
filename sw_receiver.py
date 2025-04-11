import socket

class SlidReceiver:
    def __init__(self, host='127.0.0.1', port=12345):
        self.rbuf = [None] * 8
        self.rptr = -1
        self.host = host
        self.port = port

    def receive_frames(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))

            while True:
                try:
                    nf = int(s.recv(1024).decode().strip())
                except:
                    break

                for _ in range(nf):
                    self.rptr = (self.rptr + 1) % 8
                    frame = s.recv(1024).decode().strip()
                    self.rbuf[self.rptr] = frame
                    print(f"Received Frame {self.rptr}: {frame}")

                s.send(f"{self.rptr + 1}\n".encode())
                print("\nAcknowledgment sent\n")

                if s.recv(1024).decode().strip() != "yes":
                    break

if __name__ == "__main__":
    receiver = SlidReceiver()
    receiver.receive_frames()
