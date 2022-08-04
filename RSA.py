import math
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
p =int(input('enter a primenumber to encrypt the msg:'))
q =int(input('enter another primenumber to use in rsa:'))
n = p*q
e = 2
phi = (p-1)*(q-1)
while (e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
k = 2
d = (1 + (k*phi))/e
msg =int(input('enter a input number'))
print("Message data = ", msg)
# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)