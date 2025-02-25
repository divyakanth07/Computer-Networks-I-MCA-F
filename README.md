# Computer Networks - CRC Error Detection

## Overview

This project demonstrates **Cyclic Redundancy Check (CRC) error detection** using **Python sockets**. It consists of a **client (receiver.py)** that sends binary-encoded messages and a **server (server.py)** that receives and verifies the data integrity using CRC.

## Features

- Implements CRC error detection using **mod2div** function.
- Uses **socket programming** for communication between a client and server.
- Converts text to **binary representation** for transmission.
- Detects transmission errors using a **polynomial key (1001).**
- Provides feedback on data integrity (error/no error detection).

## How It Works

1. **Client (receiver.py) Steps:**

   - Accepts user input and converts it to **binary**.
   - Generates CRC-based encoded data.
   - Sends the encoded data to the server.
   - Receives and prints server feedback.

2. **Server (server.py) Steps:**

   - Listens for incoming connections.
   - Receives encoded data and extracts the original message.
   - Performs CRC error detection.
   - Sends feedback to the client (error detected or data received successfully).

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/computer-networks-crc.git
   cd computer-networks-crc
   ```
2. **Run the server:**
   ```bash
   python server.py
   ```
3. **Run the client in another terminal:**
   ```bash
   python receiver.py
   ```
4. **Enter a message** in the client terminal and observe transmission feedback.

## Example Run

```
Client:
Enter data you want to send -> Hello
Entered data in binary format: 10010001100101110110011011001101111
Encoded data to be sent to server in binary format: 10010001100101110110011011001101111010
Received feedback from server: No error detected. Data received successfully.

Server:
Server running...
Connected to ('127.0.0.1', 12345)
Received encoded data: 10010001100101110110011011001101111010
Decoded text: Hello
No error detected. Data received successfully.
```

## File Structure

```
📂 computer-networks-crc
├── 📄 receiver.py  # Client-side script (sends encoded data)
├── 📄 server.py    # Server-side script (receives and checks data integrity)
├── 📄 README.md    # Documentation (this file)
```

## Concepts Used

- **Cyclic Redundancy Check (CRC) Algorithm**
- **Socket Programming**
- **Binary Encoding & Decoding**
- **Error Detection in Computer Networks**

## Author

- **Divyakanth**
- **SRMIST-KTR, Chennai**
- **Course: Computer Networks**

## License

This project is licensed under the **MIT License**. Feel free to use and modify it!

---

**Happy Coding! 🚀**

