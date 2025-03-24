import socket

host = '127.0.0.1' 
port = 12345

def sliding_window_sender():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening on port 10...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    sbuff = [None] * 8
    sptr = 0
    sws = 8
    
    try:
        while True:
            nf = int(input("Enter the number of frames: "))
            conn.sendall(str(nf).encode())
            
            if nf <= sws - 1:
                print(f"Enter {nf} messages to be sent")
                for i in range(nf):
                    sbuff[sptr] = input()
                    conn.sendall(sbuff[sptr].encode())
                    sptr = (sptr + 1) % 8
                
                sws -= nf
                print("Acknowledgment received")
                ano = int(conn.recv(1024).decode())
                print(f" for {ano} frames")
                sws += nf
            else:
                print("The number of frames exceeds window size")
                break
            
            ch = input("Do you want to send some more frames: ")
            conn.sendall(ch.encode())
            if ch.lower() != "yes":
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        server_socket.close()

sliding_window_sender()
