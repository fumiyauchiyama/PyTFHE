from .torus import torus32
import numpy as np

def gaussian_torus32(mu:float,alpha:float,size = 1):
    return torus32(np.random.normal(0,alpha,size)) + torus32(mu)

def gaussian_torusring32(mu:float,alpha:float,size = 1):
    return torus32(np.random.normal(0,alpha,size)) + torus32(mu)

if __name__ == "__main__":

    print(gaussian_torus32(torus32(1/8),0.2,1))