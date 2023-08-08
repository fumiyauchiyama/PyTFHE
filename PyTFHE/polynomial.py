import numpy as np

def polymul(a:np.array, b:np.array):
    res = np.zeros(len(a), dtype=np.uint32)

    for i in range(len(a)):
        for j in range(len(b)):
            if(i+j<len(a)):
                res[i+j] += a[i]*b[i]
            else:
                res[i+j-len(a)] -= a[i]*b[i]
                
    
    return res


def polymul_fft(a:np.array, b:np.array):

    raise NotImplementedError

    print('a')
    print(a)
    print('b')
    print(b)

    n = len(a)

    res = np.zeros(n,dtype=np.int64)

    #サンプル数を計算
    N = 2 ** (int(np.log2(2*n - 1)) + 1)

    # 高速フーリエ変換
    dft_a = np.fft.fft(a, N)
    dft_b = np.fft.fft(b, N)
    
    # DFTの積(畳み込み定理)
    dft_c = dft_a * dft_b
    
    # 逆高速フーリエ変換
    c = np.fft.ifft(dft_c)

    # 実部を取り、小数点以下を四捨五入
    c = np.round(c.real).astype(int)

    # mod x^n + 1
    '''
    0から(n-2)次までの係数がそれぞれnから2(n-1)までの係数と同じ分引かれることを利用
    n-1次は引かれない
    '''
    c0 = c[:n]
    c1 = c[n:]
    '''
    nが2の冪乗でないとfftのpaddingの影響で配列の長さが冗長になるので揃える
    '''
    res = c0-c1[:(len(c0))]
    print('res')
    print(res)
    print(len(res))

    # for i in range(len(res)):
    #     if(res[i]<0):
    #         print('lllllllll')
    #         print(type(res[i]))
    #         print(res[i])
    #         res[i] += 2**64
    #         print(res[i])

    return np.uint32(res)