from PyTFHE.trlwe import trlwe_encrypt,sample_extract_index
from PyTFHE.tlwe import tlwe_decrypt
from PyTFHE.key import SecretKey
import numpy as np
from secrets import randbits

for _ in range(100):
    print('start session')

    sk = SecretKey(
        n=636, #n 
        alpha=9.2511997 * (10**-5), #alpha
        alpha_bk=2**-25, #alpha_bk
        N=512, #N
        k=2, #k
        polys=1 #試す多項式の数
    )
    p = np.array([[randbits(1) for j in range(sk.params.N)] for poly in range(sk.params.polys)], dtype=np.uint32)
    c = trlwe_encrypt(p,sk)[0]
    sei = sample_extract_index(c,0)
    print('SampleExtractIndex.shape: ', sei.shape)
    sk.key.tlwe = np.ravel(sk.key.trlwe, order="C")
    print('p[i]', p[0][0], 'sei', tlwe_decrypt(sei, sk))