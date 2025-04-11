import socket

class SlidSender:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_frames(self, frames):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print("Waiting for receiver to connect...")
        conn, _ = self.socket.accept()

        window_size = 8
        ptr = 0

        while ptr < len(frames):
            nf = min(window_size, len(frames) - ptr)
            conn.send(f"{nf}\n".encode())

            for i in range(nf):
                conn.send(f"{frames[ptr]}\n".encode())
                print(f"Sent Frame {ptr % 8}: {frames[ptr]}")
                ptr += 1

            ack = conn.recv(1024).decode().strip()
            if not ack.isdigit():
                        print("Invalid or no acknowledgment received.")
                        break

            print(f"Acknowledgment received for Frame {int(ack) - 1}")            
            conn.send(b"yes\n")

        conn.close()

if __name__ == "__main__":
    sender = SlidSender()
    frames_to_send = [f"Frame{i}" for i in range(12)]
    sender.send_frames(frames_to_send)
