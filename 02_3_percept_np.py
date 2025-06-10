import numpy as np
def Percept(w1,w2,theta):
    W=np.array([[w1],[w2]])
    B=np.array([-theta])
    def H(x1,x2):
        X=np.array([x1,x2])
        return np.sum(np.dot(X,W)+B)>0
    return H
def PrintPercept(pf,str):
    for i in range(0,4):
        x1,x2=i//2,i%2 
        print(f'{str} {x1},{x2} = {pf(x1,x2)}')
        
Pand=Percept(0.5,0.5,0.9)
Por =Percept(0.5,0.5,0.4)
Pnand=Percept(-0.5,-0.5,-0.9)

PrintPercept(Pand,'AND')
PrintPercept(Por,'OR')
PrintPercept(Pnand,'NAND')
