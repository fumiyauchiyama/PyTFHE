import numpy as np
from secrets import randbits
from .torus import torus32
from .utils import gaussian_torus32, gaussian_torusring32
from .polynomial import polymul

MU = 1 / 8

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

def trlwe_polynomial_encrypt(p, alpha_bk, key):
    a = np.array([[randbits(32) for j in range(len(key[0]))] for i in range(len(key))], dtype=torus32)
    p_mu = np.empty_like(p, dtype=float)
    for i in range(len(p)):
            if p[i]==1:
                p_mu[i] = MU
            else:
                p_mu[i] = -MU
    
    
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