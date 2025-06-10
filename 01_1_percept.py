import numpy as np
def Pand(x1,x2):
    w1,w2,theta=0.5,0.5,0.9
    return w1*x1+w2*x2>theta
    
def Por(x1,x2):
    w1,w2,theta=0.5,0.5,0.4
    return w1*x1+w2*x2>theta

def Pnand(x1,x2):
    w1,w2,theta=-0.5,-0.5,-0.9
    return w1*x1+w2*x2>theta
    
print('AND 0 0',Pand(0,0))
print('AND 0 1',Pand(0,1))
print('AND 1 0',Pand(1,0))
print('AND 1 1',Pand(1,1))

print('OR 0 0',Por(0,0))
print('OR 0 1',Por(0,1))
print('OR 1 0',Por(1,0))
print('OR 1 1',Por(1,1))

print('NAND 0 0',Pnand(0,0))
print('NAND 0 1',Pnand(0,1))
print('NAND 1 0',Pnand(1,0))
print('NAND 1 1',Pnand(1,1))