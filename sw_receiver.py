import socket

class SlidReceiver:
    def __init__(self):
        self.rws = 8
        self.rbuf = [None] * 8
        self.rptr = -1
        self.host = '127.0.0.1'
        self.port = 12345

    def receive_frames(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        
        while True:
            nf = int(s.recv(1024).decode().strip())
            if nf <= self.rws - 1:
                for i in range(nf):
                    self.rptr = (self.rptr + 1) % 8
                    self.rbuf[self.rptr] = s.recv(1024).decode().strip()
                    print(f"The received Frame {self.rptr} is : {self.rbuf[self.rptr]}")
                self.rws -= nf
                print("\nAcknowledgment sent\n")
                s.send(f"{self.rptr + 1}\n".encode())
                self.rws += nf
            else:
                break
            ch = s.recv(1024).decode().strip()
            if ch != "yes":
                break

if __name__ == "__main__":
    receiver = SlidReceiver()
    receiver.receive_frames()
