import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    return tmp

def decodeData(data, key):
    remainder = mod2div(data, key)
    return remainder

def binary_to_text(binary_data):
    text = ''
    for i in range(0, len(binary_data), 7):  # Assuming ASCII (7-bit or 8-bit encoding)
        char = chr(int(binary_data[i:i+7], 2))
        text += char
    return text

def main():
    s = socket.socket()
    port = 12345
    s.bind(('127.0.0.1', port))
    s.listen(1)
    print("Server running...")
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    data = conn.recv(1024).decode()
    key = "1001"
    print("Received encoded data:", data)
    decoded_text = binary_to_text(data[:-len(key) + 1])  # Extract original message
    print("Decoded text:", decoded_text)
    remainder = decodeData(data, key)
    if remainder == "0" * (len(key) - 1):
        feedback = "No error detected. Data received successfully."
    else:
        feedback = "Error detected! Please resend the data."
    conn.send(feedback.encode())
    conn.close()
    s.close()

if __name__ == "__main__":
    main()
