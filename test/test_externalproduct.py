from PyTFHE.trlwe import trlwe_polynomial_encrypt, trlwe_polynomial_decrypt
from PyTFHE.trgsw import trgsw_encrypt, trgsw_external_product
from PyTFHE.key import SecretKey
import numpy as np

np.set_printoptions(threshold=4000)
for i in range(100):
    sk = SecretKey(
        n=636, #n 
        alpha=9.2511997 * (10**-5), #alpha
        alpha_bk=2**-25, #alpha_bk
        N=512, #N
        k=2, #k
        polys=1 #試す多項式の数
    )
    x = trlwe_polynomial_encrypt(
        np.full(sk.params.N, 1), sk.params.alpha, sk.key.trlwe
    )
    A = trgsw_encrypt(
        np.append([1], np.zeros(sk.params.N - 1)),
        sk.params,
        sk.key.trlwe,
    )

    print(trlwe_polynomial_decrypt(x, sk.key.trlwe))
    # A = A.reshape(len(A), -1)
    # x = x.reshape(-1)
    print('a', A.shape, 'x', x.shape)

    y = trgsw_external_product(A, x, sk.params)
    print(np.sum(trlwe_polynomial_decrypt(y, sk.key.trlwe)), len(y[0]))
    print(trlwe_polynomial_decrypt(y, sk.key.trlwe))
    if np.sum(trlwe_polynomial_decrypt(y, sk.key.trlwe)) != len(y[0]):
        print(trlwe_polynomial_decrypt(y, sk.key.trlwe).shape)
        print(np.uint32(y).shape)
        print(i)
        break