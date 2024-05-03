import random
no_of_rounds=3
p = list(range(4))
p=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
# random.shuffle(p)

s=list(range(16))
# s=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
s=[]
for i in range(no_of_rounds):
    s_=list(range(16))
    random.shuffle(s_)
    # s_=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
    # s_=[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8]
    s.append(s_)
# # random.shuffle(s)
# s[0]=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
# s[1]=[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8]
# s[2]=[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0]
s_inv=[]
for i in range(no_of_rounds):
    s_inv.append({value: index for index, value in enumerate(s[i])})

def demux(x):
    y=[]
    for i in range(4):
        y.append((x>> (i*4)) & 15)
    y.reverse()
    return y

def mux(x):
    y = 0
    for i in range(4):
        y = y ^ (x[i] << ((3-i) * 4))

    return y

def xorr(p, k):
    v = []

    key = demux(k)
    for i in range(4):
        v.append(p[i] ^ key[i])

    return mux(v)
def pbox(x):
    y=0
    for i in range(len(p)):
        if (x & (1 << i)) != 0:
            y=y^(1<<p[i])
    return y

def round(plain_text,k,round_no):
    e=[]
    for x in demux(plain_text):
        e.append(s[round_no][x])
    if round_no < no_of_rounds-1:
        v=demux(pbox(mux(e)))
    else:
        v=e
    return xorr(v,k)

def encrypt(key,plain_text,rounds):
    x=plain_text
    for i in range(rounds):
        x=round(x,key[i],i)
    return x

def no_of_ones(t):
    ones=0
    for h in range(4):
        ones+=(t%2)
        t=t//2
    if ones%2==0:
        return 0
    return 1

def no_of_zeros(t):
    zeros = 0
    for i in t :
        if i == 0:
            zeros += 1
    return zeros
# def apbox(x):
#     y = 0
#     for i in range(len(p)):
#         if (x & (1 << i)) != 0:
#             pval = p.index(i)
#             y = y ^ (1 << pval)
#     return y

# def asbox(x):
#     return s.index(x)

# def unround(c, k, first=False):
#     x = demux(c)

#     u = demux(xorr(x, k))

#     if first is False:
#         v = demux(apbox(mux(u)))
#     else:
#         v = u

#     w = []
#     for s in v:
#         w.append(asbox(s))

#     return mux(w)

# def decrypt(key, c, rounds):
#     x = c
#     for i in range(rounds):
#         x = unround(x, key, first=(i==0))
#     return x

# key=0
# message=''.join(str(random.randint(0, 1)) for _ in range(16))
# m=0
# for i in range(16):
#     m+=(1<<i)*int(message[i])
# c=encrypt(key,m,no_of_rounds)
# print(m)
# print(c)
# print(decrypt(key,c,no_of_rounds))
# print(s[2])
# print(pbox(s[2]))
# print(pbox(1))