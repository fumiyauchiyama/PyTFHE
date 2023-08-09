from PyTFHE import key,tlwe
import numpy as np

sk = key.SecretKey(
        n=636, #n 
        alpha=9.2511997 * (10**-5), #alpha
        alpha_bk=2**-25, #alpha_bk
        N=512, #N
        k=2, #k
        polys=1 #試す多項式の数
    )
c = tlwe.tlwe_encrypt(np.array([0,1,0,1,0]),sk)
print (tlwe.tlwe_decrypt(c,sk))