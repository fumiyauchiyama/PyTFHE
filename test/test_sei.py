from PyTFHE.trlwe import trlwe_polynomial_encrypt, trlwe_encrypt,sample_extract_index
from PyTFHE.tlwe import tlwe_binary_decrypt
from PyTFHE.key import SecretKey
import numpy as np
from secrets import randbits

for _ in range(100):

    sk = SecretKey(
        n=636, #n 
        alpha=9.2511997 * (10**-5), #alpha
        alpha_bk=2**-25, #alpha_bk
        N=512, #N
        k=1, #k
        polys=1 #試す多項式の数
    )
    p = np.array([randbits(1) for j in range(sk.params.N)], dtype=np.uint32)
    c = trlwe_polynomial_encrypt(p, sk.params.alpha_bk, sk.key.trlwe)
    sei = sample_extract_index(c,0)
    key = np.ravel(sk.key.trlwe, order="C")
    decrypted_sei = tlwe_binary_decrypt(sei, key)
    print(p[0]==decrypted_sei)