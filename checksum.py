def getChecksum(SentMessage, k):
    c1 = SentMessage[0:k]
    c2 = SentMessage[k:2*k]
    c3 = SentMessage[2*k:3*k]
    c4 = SentMessage[3*k:4*k]

    sum = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2))[2:]

    if len(sum) > k:
        x = len(sum) - k
        sum = bin(int(sum[0:x], 2) + int(sum[x:], 2))[2:]
    if len(sum) < k:
        sum = '0' * (k - len(sum)) + sum

    checksum = ''
    for i in sum:
        if i == '1':
            checksum += '0'
        else:
            checksum += '1'
    return checksum

def recChecksum(recvMessage, k, checksum):
    c1 = recvMessage[0:k]
    c2 = recvMessage[k:2*k]
    c3 = recvMessage[2*k:3*k]
    c4 = recvMessage[3*k:4*k]

    recvsum = bin(int(c1, 2) + int(c2, 2) + int(checksum ,2)+int(c3, 2) + int(c4, 2) + int(checksum, 2))[2:]

    while len(recvsum) > k:
        x = len(recvsum) - k
        recvsum = bin(int(recvsum[0:x], 2) + int(recvsum[x:], 2))[2:]

    if len(recvsum) < k:
        recvsum = '0' * (k - len(recvsum)) + recvsum

    recvchecksum = ''
    for i in recvsum:
        if i == '1':
            recvchecksum += '0'
        else:
            recvchecksum += '1'
    return recvchecksum


SentMessage = "10010101011000111001010011101100"
k = 8
checksum = getChecksum(SentMessage, k)

recvMessage = "10010101011000111001010011101100"
recvchecksum = recChecksum(recvMessage, k, checksum)

print("Sender's Checksum: ", checksum)
print("Receiver's Checksum: ", recvchecksum)
totalsum = bin(int(checksum, 2) + int(recvchecksum, 2))[2:]

finalcomp = ''
for i in totalsum:
    if i == '1':
        finalcomp += '0'
    else:
        finalcomp += '1'

if int(finalcomp, 2) == 0:
    print("Receiver Checksum = 0")
    print("Accepted")
else:
    print("Receiver Checksum != 0")
    print("Error Detected!!")
