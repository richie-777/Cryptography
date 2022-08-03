def affine_encrypt(msg,key_a=7,key_b=3):
    msg_l = list(msg)
    out = ''
    for i in msg_l:
        out += chr(((ord(i) - 65)*key_a + key_b) % 26 + 65 )
    print(out)
def affine_decrypt(msg,key_a=15,key_b=3):
    msg_l = list(msg)
    out = ''
    for i in msg_l:
        out += chr( (key_a * (ord(i) - 65 - key_b)) % 26 + 65 )
    print(out)
affine_decrypt( affine_encrypt(str(input("Enter text: "))))