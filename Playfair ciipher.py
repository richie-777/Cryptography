def di_graph(msg):
    msg_l = list(msg)
    while ' ' in msg_l:
        msg_l.remove(' ')
    f = 1
    di_graph = []
    prev = ''
    for i in range(len(msg_l)):
        if f == 1:
            prev = msg_l[i]
            f = 0
        else:
            di_graph.append(prev + msg_l[i])
            f = 1
    if prev != '':
        di_graph.append(prev + 'X')
        print(di_graph)
def playfair_key_gen(key):
    k = [[''] * 5 for i in range(5)]
    p = 0
    exclude = [ord(i) for i in list(key)]
    exclude.append(ord('J'))
    r = 0
    fill_key = list(set([i for i in range(ord('A'), ord('Z') + 1)]) - set(exclude))
    for i in range(5):
        for j in range(5):
            if p < len(key):
                k[i][j] = key[p]
                p += 1
            elif r < len(fill_key):
                k[i][j] = chr(fill_key[r])
                r += 1
    return k
def playfair_encrypt(msg, playfair_key='ETHICS'):
    di_gr = di_graph(msg)
    key_g = playfair_key_gen(playfair_key)
    out = ''
    sing_l = []
    for i in range(5):
        for j in range(5):
            sing_l.append(key_g[i][j])
    print(sing_l)
    for i in di_gr:
        i.replace('J', 'I')
        first_letter = i[0]
        second_letter = i[1]
        if first_letter == second_letter:
            out += first_letter + first_letter
        else:
            pass
    print(out)
def playfair_decrypt(msg, playfair_key='ETHICS'):
    msg_l = list(msg)
    out = ''
    for i in msg_l:
        out += chr((ord(i) - 65 - playfair_key) % 26 + 65)
    print(out)
playfair_encrypt("HELLO THERE")
#playfair_decrypt('text'))