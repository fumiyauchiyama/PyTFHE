import numpy as np
from secrets import randbits
from .torus import torus32
from .utils import gaussian_torus32, gaussian_torusring32
from .polynomial import polymul

MU = 1 / 8

# 複数の多項式を受け付ける

def trlwe_encrypt(p, sk):
    plaintextlength = len(p)
    c = np.empty((plaintextlength, sk.params.k+1, sk.params.N),dtype = np.uint32)
    for i in range(plaintextlength):
        c[i] = trlwe_polynomial_encrypt(p[i], sk.params.alpha_bk, sk.key.trlwe)
    return c

def trlwe_decrypt(c, sk):
    ciphertextlength = len(c)
    ret = np.empty((ciphertextlength, sk.params.N), dtype=int)
    for i in range(ciphertextlength):
        ret[i] = trlwe_polynomial_decrypt(c[i],sk.key.trlwe)
    return ret

# 多項式を一つ受け付ける

def trlwe_polynomial_encrypt(p, alpha_bk, key):
    a = np.array([[randbits(32) for j in range(len(key[0]))] for i in range(len(key))], dtype=torus32)
    p_mu = np.empty_like(p, dtype=float)
    for i in range(len(p)):
            if p[i]==1:
                p_mu[i] = MU
            else:
                p_mu[i] = -MU
    
    print(p_mu, alpha_bk, len(key[0]))
    b = gaussian_torusring32(p_mu, alpha_bk, len(key[0]))

    for i in range(len(key)):
        b += polymul(a[i], key[i])


    return np.vstack((a, b))

def trlwe_polynomial_decrypt(c,key):
    N = len(c[0])
    a = c[:len(key)]
    b = c[len(key)]
    pm = np.zeros(N, dtype=np.int32)
    for j in range(len(key)):
        pm += polymul(a[j], key[j])
    
    return (1 + np.sign(np.int32(b) - pm))/2

def sample_extract_index(c, x_index:int):

    a = c[:len(c)-1]
    b = c[len(c)-1]

    k = len(a)
    N = len(a[0])

    b_sei = b[x_index]

    a_sei = np.zeros((k, N), dtype=np.uint32)
    for j in range(k):
        for i in range(x_index+1):
            a_sei[j][i] = a[j][x_index - i].copy()
        for i in range(x_index+1, N):
            a_sei[j][i] = -a[j][N + x_index - i].copy()

    a_sei = np.ravel(a_sei, order="C")

    return np.append(a_sei, b_sei)