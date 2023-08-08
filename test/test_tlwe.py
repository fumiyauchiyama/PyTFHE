from PyTFHE import key,tlwe
import numpy as np

sk = key.SecretKey(
    636,
    9.2511997 * (10**-5)
    )
c = tlwe.tlwe_encrypt(np.array([0,1,0,1,0]),sk)
print (tlwe.tlwe_decrypt(c,sk))