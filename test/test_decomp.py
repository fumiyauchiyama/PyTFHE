from PyTFHE.trgsw import decomposition
from PyTFHE.trlwe import trlwe_polynomial_encrypt, trlwe_polynomial_decrypt
from PyTFHE.key import SecretKey
from PyTFHE.torus import torus32
import numpy as np

for i in range(1000):
    #sk = SecretKey(500, 2 ** (-7), 1024, 2, 10, 3.73e-9, 8, 2, 2.43e-5)
    sk = SecretKey(
        636, #n 
        9.2511997 * (10**-5), #alpha
        2**-25, #alpha_bk
        512, #N
        2, #k
        2 #試す多項式の数
    )
    p = np.random.randint(0, 2, size=sk.params.N, dtype=np.uint32)
    c = trlwe_polynomial_encrypt(
        (2 * p - 1) * 2 ** -3, sk.params.alpha_bk, sk.key.trlwe
    )

    cdec = decomposition(c[-1], sk.params)
    h = torus32(sk.params.h)
    rec = np.array(np.uint32(cdec[0] * h[0] + cdec[1] * h[1]))

    print('delta') #最大誤差が2 ** (32 - l*Bgbit)くらい、つまり2**16の64000くらいなら問題ない
    print(np.int32(c[-1]-rec))
    if np.any(trlwe_polynomial_decrypt(np.vstack([c[:-1],rec]), sk.key.trlwe) != p):
        print(i)
        break