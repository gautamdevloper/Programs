import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0) # maximum of X array longitudinally
y = y/100

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))


#Variable initialization
epoch=5000 	#Setting training iterations
lr=0.1 		#Setting learning rate
inputlayer_neurons = 2 		#number of features in data set
hiddenlayer_neurons = 3 	#number of hidden layers neurons
output_neurons = 1 		#number of neurons at output layer

#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))


#draws a random range of numbers uniformly of dim x*y
for i in range(epoch):

#Forward Propogation
    hinp=np.dot(X,wh) + bh
    hlayer_act = sigmoid(hinp)
    outinp= np.dot(hlayer_act,wout)+ bout
    output = sigmoid(outinp)

#Backpropagation
    EO = y-output
    d_output = EO*output*(1-output)
    EH = np.dot(wout.T,d_output)

#how much hidden layer wts contributed to error
    d_hiddenlayer = EH * hlayer_act*(1-hlayer_act)

# dotproduct of nextlayererror and currentlayerop
wout += np.dot(hlayer_act.T,d_output) *lr
wh +=np.dot(X.T,d_hiddenlayer ) *lr

print("Input: \n" + str(X)) 
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,output)
