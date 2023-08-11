import numpy as np
from .trlwe import trlwe_polynomial_encrypt
from .torus import torus32
from .polynomial import  polymul

def decomposition(trlwe, params):
    trlwe += params.offset
    t = np.array([trlwe >> i for i in params.decbit])
    t &= (params.Bg - 1)
    t_hat = t.astype(np.int32)
    for i in range(params.l-1, 0, -1):
        for j in range(len(trlwe)):
            if(t_hat[i][j] >= params.Bg / 2):
                t_hat[i][j] = t_hat[i][j] - params.Bg
                t_hat[i-1][j] += 1

    return t_hat

#　一つの多項式が対象。key[0]にしているのは、鍵が多項式の数だけ作られるので。
def trgsw_encrypt(p, params, key):
    l = len(params.h)
    N = len(key[0])
    #zero_matrix = np.array([trlwe_polynomial_encrypt(np.zeros(N), params.alpha_bk, key) for i in range((params.k+1)*l)], dtype=np.uint32)
    #external productのテスト用に一旦ゼロ行列を無効化
    zero_matrix = np.zeros(((params.k+1)*l, params.k+1, N), dtype=np.uint32)
    mu_h = torus32(np.outer(params.h, p))

    print('zero_matrix', zero_matrix.shape)
    print(zero_matrix[2*l:(2+1)*l, 2].shape)

    for i in range(params.k+1):
        zero_matrix[i*l:(i+1)*l, i] += mu_h

    return zero_matrix

def trgsw_external_product(g, r, params):
    decvec = np.array([decomposition(i, params) for i in r])
    print(decvec.shape)
    decvec = decvec.reshape(-1, params.N)
    return np.array(
        [
            np.sum(
                [
                    polymul(decvec[j], g.transpose((1,0,2))[i][j]) 
                    for j in range((params.k+1) * params.l)
                ]
                , axis=0) 
            
            for i in range(params.k+1)
        ]
        )
    # return np.array(
    #     [
    #         np.sum(
    #             [
    #                 polymul(decvec[i], g[i][0], params.twist)
    #                 for i in range(2 * params.l)
    #             ],
    #             axis=0,
    #         ),
    #         np.sum(
    #             [
    #                 PolyMul(decvec[i], g[i][1], params.twist)
    #                 for i in range(2 * params.l)
    #             ],
    #             axis=0,
    #         ),
    #     ],
    #     dtype=np.uint32,
    # )