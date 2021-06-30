import numpy as np
eta=0.1
np.random.seed(0)
n_iter =120
m=100
X=2*np.random.rand(100,1)
y=4+3*X+np.random.randn(100,1)
X_b=np.c_[np.ones((100,1)),X]
theta=[[5],[4]]#np.random.rand(2,1)

print(theta)

for i in range(n_iter):
        gradient=2/m*X_b.T.dot(X_b.dot(theta)-y)
        #print(i,"G", gradient)
        theta=theta-eta*gradient
        #print("iteration no:",i,"Theta:",theta)

print(theta)
    
