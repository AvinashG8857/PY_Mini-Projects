import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmiod_derivative(x):
    return x*(1-x)

#dataset
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_outputs = np.array([[0],[1],[0],[1]])

#brain
inputLayerNeuron,hiddenLayerNeuron,OutputLayerNeuron=2,3,1

hiddenWeights= np.random.uniform(size=(inputLayerNeuron,hiddenLayerNeuron))
output_weights= np.random.uniform(size=(hiddenLayerNeuron,OutputLayerNeuron))

hidden_bias= np.random.uniform(size=(1,hiddenLayerNeuron))
output_bias= np.random.uniform(size=(1,OutputLayerNeuron))


Learning_rate= 0.5
epochs= 10000

for epoch in range(epochs):
    #forward propogation
    hidden_layer_activation=np.dot(inputs,hiddenWeights)+hidden_bias
    hidden_layer_output= sigmoid(hidden_layer_activation)

    output_layer_activation= np.dot(hidden_layer_output,output_weights)+output_bias
    prdicted_output= sigmoid(output_layer_activation)

    #backpropogation
    #calculate the eroor(real-prediction)
    error= expected_outputs-prdicted_output

    #finding gradient
    d_prediction_output= error*sigmiod_derivative(prdicted_output)

    #hidden layer contribution
    error_hidden_layer= d_prediction_output.dot(output_weights.T)
    d_hidden_layer= error_hidden_layer*sigmiod_derivative(hidden_layer_output)

    #updating weights
    output_weights+= hidden_layer_output.T.dot(d_prediction_output)*Learning_rate
    output_bias+= np.sum(d_prediction_output,axis=0,keepdims=True)*Learning_rate

    if epoch%2000==0:
        print(f"Epoch {epoch} Error:{np.mean(np.abs(error))}")

print("\nFinal Predicted Output after Training:")
print(prdicted_output)