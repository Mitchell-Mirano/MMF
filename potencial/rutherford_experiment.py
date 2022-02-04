import numpy as np
import matplotlib.pyplot as plt
from typing import List


def xt_n(xn_1,yn_1,vn_1,dt):
    m=1.67*10**-27
    k=9*10**9
    q=1.6*10**-19
    Q=79*q
    p=k*Q*q/m
    r=np.sqrt(xn_1**2 +yn_1**2)
    an_1=p*xn_1/r**3
    vn=vn_1 + an_1*dt
    return xn_1 +vn*dt+0.5*an_1*dt**2,vn

def yt_n(xn_1,yn_1,vn_1,dt):
    m=1.67*10**-27
    k=9*10**9
    q=1.6*10**-19
    Q=79*q
    p=k*Q*q/m
    r=np.sqrt(xn_1**2 +yn_1**2)
    an_1=p*yn_1/r**3
    vn=vn_1 + an_1*dt
    return yn_1 +vn*dt + 0.5*an_1*dt**2,vn


def Rutherford_Experiment():
    m=1.67*10**-27
    K=4.7*10**6*1.6*10**-19

    while True:
        b_values: str = input("Ingrese valores entre(-10**-12,10**-12) para el parametro b: ")
        if b_values=="q":
            break
        b_values: List[str] = b_values.replace("[", "").replace("]", "").split(",")
        yns:List[float] = [eval(value) for value in b_values]

        xs=[]
        ys=[]
        for yn in yns:
            xn=-2000*10**-15
            vx0=np.sqrt(2*K/m)
            vy0=0
            dt=10**-21
            x=[]
            y=[]
            for _ in range(300):
                xn,vx0=xt_n(xn,yn,vx0,dt)
                yn,vy0=yt_n(xn,yn,vy0,dt)
                x.append(xn)
                y.append(yn)
            xs.append(x)
            ys.append(y)

        plt.figure(figsize=(30,15))
        for x,y in zip(xs,ys):
            plt.plot(x,y,lw=3,color="red")
            plt.text(x[0],y[0],f"P0",fontsize=10)
            plt.text(x[-1],y[-1],f"Pf",fontsize=10)
        plt.scatter(0, 0, s=500, color="blue")
        plt.xlabel("Eje X",fontsize=20)
        plt.ylabel("Eje Z",fontsize=20)
        plt.title("Experimento de Rutherford",fontsize=20)
        plt.axhline()
        plt.axvline()
        plt.show()