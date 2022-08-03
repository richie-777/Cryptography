def ceaser_encrypt(msg,k=3):
    msg_l = list(msg)
    out = ''
    for i in msg_l:
        out += chr((ord(i) - 65 + k) % 26 + 65)
    print(out)
def ceaser_decrypt(msg,k=3):
    msg_l = list(msg)
    out = ''
    for i in msg_l:
        out += chr((ord(i) - 65 - k) % 26 + 65)
    print(out)
ceaser_encrypt(ceaser_decrypt(str(input("Enter the Text: "))))
