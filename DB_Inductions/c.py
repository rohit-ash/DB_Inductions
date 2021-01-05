import numpy as np
class MP_Neuron():
    def __init__(self):
        self.n = 3
        self.i = [1,1,1]
        self.w = [1,1,1]
        self.threshold = 2.5 
    def MP_Neuron_Input(self,n,inp,weight,t):
        self.n = n
        self.i = inp
        self.w = weight
        self.threshold = t
    def MP_Neuron_Evaluate(self):
        self.res = np.dot(self.i,self.w)
        if(self.res >= self.threshold):
            return 1
        else:
            return 0
i1 = input()
i2 = input()
i3 = input()
def NAND(i1,i2,i3):
    a1 = MP_Neuron()
    b1 = a1.MP_Neuron_Input(1,i1,-1,0)
    a2 = MP_Neuron()
    b2 = a2.MP_Neuron_Input(1,i2,-1,0)
    a3 = MP_Neuron()
    b3 = a3.MP_Neuron_Input(1,i3,-1,0)
    f1 = a1.MP_Neuron_Evaluate()
    f2 = a2.MP_Neuron_Evaluate()
    f3 = a3.MP_Neuron_Evaluate()
    f = [f1,f2,f3]
    w = [1,1,1]
    a4 = MP_Neuron()
    b4 = a4.MP_Neuron_Input(3,f,w,1)
    f4 = a4.MP_Neuron_Evaluate()
    return f4