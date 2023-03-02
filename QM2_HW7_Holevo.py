import numpy as np 
import matplotlib.pyplot as plt


def I(t,a,p):
    HY1 =0.5*(np.log2(0.25*(1-((1-2*p)*np.cos(2*t)*np.cos(a))**2 +(np.sin(2*t)*np.sin(a))**2)))
    HY2 = (1/2*(np.cos(2*t)*np.cos(a)*(1-2*p)-np.sin(2*t)*np.sin(a)))
    HY2 *= np.log2((1+(1-2*p)*np.cos(2*t)*np.cos(a)-np.sin(2*t)*np.sin(a))/
                  (1-(1-2*p)*np.cos(2*t)*np.cos(a)+np.sin(2*t)*np.sin(a)))
    HYcX = (1/2*(np.log2(1/2-np.cos(4*t)*np.cos(2*a))
                 +np.cos(2*t+a)*np.log2((1+np.cos(2*t+a))/(1-np.cos(2*t+a)))))
    return -HY1-HY2-HYcX 

def holevo(t,p): 
    A = 0.5*(1-np.sqrt(2*p*(p-1)*(np.cos(2*t))**2+1))
    logA = np.log2(0.5*(1-np.sqrt(2*p*(p-1)*(np.cos(2*t))**2+1)))
    B = 0.5*(1+np.sqrt(2*p*(p-1)*(np.cos(2*t))**2+1))
    logB = np.log2(0.5*(1+np.sqrt(2*p*(p-1)*(np.cos(2*t))**2+1)))
    
    
    return  -(A*logA+B*logB)


print(I(0,np.pi/4,0.5))



plt.figure()
plt.xlabel('Probability')
plt.ylabel('Information (bits)')

p = np.arange(0,1,0.01)

def plot(t,a_arr):
    plt.plot(p,holevo(t,p), '--',label = "Holevo Bound with theta = {} rad".format(round(t,1)), )
    for a in a_arr: 
        plt.plot(p,I(t,a,p), label = "Mutual Information with alpha = {} rad, theta = {} rad".format(round( a,1),round(t,1)))
        

plot(np.pi,[ np.pi/4, np.pi/3])



plt.legend()
save_str = 'holevo.png'
plt.savefig(save_str)