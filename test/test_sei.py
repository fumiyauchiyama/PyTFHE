from PyTFHE.trlwe import trlwe_encrypt,sample_extract_index
from PyTFHE.tlwe import tlwe_binary_decrypt
from PyTFHE.key import SecretKey
import numpy as np
from secrets import randbits

for _ in range(100):

    sk = SecretKey(
        636, #n 
        9.2511997 * (10**-5), #alpha
        2**-25, #alpha_bk
        512, #N
        2, #k
        1 #試す多項式の数
    )
    p = np.array([[randbits(1) for j in range(sk.params.N)] for poly in range(sk.params.polys)], dtype=np.uint32)
    c = trlwe_encrypt(p,sk)[0]
    sei = sample_extract_index(c,0)
    print('oooooo')
    print(sei.shape)
    print('p[i]', p[0][0], 'sei', tlwe_binary_decrypt(sei, np.ravel(sk.key.trlwe, order="C")))