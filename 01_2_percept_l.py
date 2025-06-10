import numpy as np
def Percept(w1,w2,theta):
    return lambda x1,x2:(x1*w1+x2*w2>theta)

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
