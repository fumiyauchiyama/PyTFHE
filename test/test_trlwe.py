from PyTFHE import trlwe_encrypt,trlwe_decrypt
from PyTFHE import SecretKey
from secrets import randbits
import numpy as np

np.set_printoptions(threshold=2000)
for i in range(1000):
    sk = SecretKey(
        636, #n 
        9.2511997 * (10**-5), #alpha
        #2**-25, #alpha_bk
        0,
        512, #N
        3, #k
        2 #試す多項式の数
    )
    p = np.array([[randbits(1) for j in range(sk.params.N)] for poly in range(sk.params.polys)], dtype=int)
    c = trlwe_encrypt(p,sk)
    y = trlwe_decrypt(c,sk)
    if np.any(p != y):
        print(i)
        print(p)
        print(trlwe_decrypt(c,sk))
        break