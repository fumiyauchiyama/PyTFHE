import numpy as np
from secrets import randbits
from .torus import torus32
from .utils import gaussian_torus32

MU = 1 / 8

def tlwe_encrypt(p, sk):
    plaintextlength = len(p)
    c = np.empty((plaintextlength,sk.params.n+1),dtype = np.uint32)
    for i in range(plaintextlength):
        if p[i] == 0:
            c[i] = tlwe_binary_encrypt(-MU,sk.params.alpha,sk.key.tlwe)
        else:
            c[i] = tlwe_binary_encrypt(MU,sk.params.alpha,sk.key.tlwe)
    return c

def tlwe_decrypt(c, sk):
    ciphertextlength = len(c)
    return np.array([tlwe_binary_decrypt(c[i],sk.key.tlwe) for i in range(ciphertextlength)])

def tlwe_binary_encrypt(p, alpha, key):
    a = np.array([randbits(32) for i in range(len(key))], dtype=np.uint32)
    b = gaussian_torus32(p, alpha, 1)[0] + np.dot(a, key)
    return np.append(a, b)

def tlwe_binary_decrypt(c,key):
    return int((1 + np.sign(np.int32(c[len(key)] - np.dot(c[:len(key)],key))))/2)