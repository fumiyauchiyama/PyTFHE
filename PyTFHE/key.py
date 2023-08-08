from secrets import randbits
import numpy as np

class lweKey:
    def __init__(self,n:int,N:int,k:int):
        self.tlwe = np.array([randbits(1) for i in range(n)],dtype = np.uint32)
        self.trlwe = np.array([[randbits(1) for j in range(N)] for i in range(k)], dtype=np.uint32)

class lweParams:
    def __init__(
            self,
            n:int,
            alpha:float,
            alpha_bk:float,
            N:int,
            k:int,
            polys:int,
    ):
        self.n = n
        self.alpha = alpha
        self.alpha_bk = alpha_bk
        self.N = N
        self.k = k
        self.polys = polys

class SecretKey:
    def __init__(
            self,
            n:int,
            alpha:float,
            alpha_bk:float,
            N: int,
            k: int,
            polys: int,
    ):
        self.params = lweParams(n,alpha,alpha_bk,N,k,polys)
        self.key = lweKey(n,N,k)