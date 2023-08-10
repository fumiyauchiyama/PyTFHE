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
            l:int,
            Bgbit:int,
    ):
        self.n = n
        self.alpha = alpha
        self.alpha_bk = alpha_bk
        self.N = N
        self.k = k
        self.polys = polys
        self.l = l
        self.Bg = 1 << Bgbit
        self.Bgbit = Bgbit
        self.h = np.array([self.Bg ** (-(1 + i)) for i in range(l)], dtype=np.double)
        self.offset = np.uint32(1 << (32 - self.l * Bgbit - 1))
        self.decbit = [32 - (p + 1) * Bgbit for p in range(l)]

class SecretKey:
    def __init__(
            self,
            n:int,
            alpha:float,
            alpha_bk:float,
            N: int,
            k: int,
            polys: int,
            l: int = 2,
            Bgbit: int = 8,
    ):
        self.params = lweParams(n,alpha,alpha_bk,N,k,polys,l,Bgbit)
        self.key = lweKey(n,N,k)