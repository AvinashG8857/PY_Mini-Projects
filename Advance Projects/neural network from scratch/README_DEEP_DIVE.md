# 🧠 Deep Dive: Building a Neural Network from Scratch
## An Advanced Exploration of Machine Learning Mechanics

This repository contains a pure Python implementation of a **Multi-Layer Perceptron (MLP)**. We bypass high-level libraries like TensorFlow to expose the raw Linear Algebra and Calculus that power modern Artificial Intelligence.

---

## 🏗️ The Architecture (Under the Hood)

Our network is designed to solve the **XOR Problem**. XOR is a classic challenge because it is not "linearly separable"—you cannot separate the outputs with a single straight line. Our solution uses a three-layer architecture:

1.  **Input Layer ($4 \times 2$ Matrix):** Represents 4 training examples, each with 2 features.
2.  **Hidden Layer (3 Neurons):** This is where the "feature extraction" happens. These 3 neurons create a 3D space that allows the data to be separated.
3.  **Output Layer (1 Neuron):** The final decision-maker.

---

## 📐 In-Depth Mathematical Pillars

### 1. Matrix Multiplication (The Connection)
Instead of looping through neurons, we use the **Dot Product**.
$$Z = X \cdot W + B$$
In this equation, $X$ is our input data, and $W$ is the weight matrix. Each weight acts as a "volume knob" for the incoming signal. If a weight is $0.8$, the signal is amplified; if it is $-0.5$, the signal is dampened and inverted.

### 2. The Activation Function (The Sigmoid "Gate")
To introduce "intelligence" (non-linearity), we use the **Logistic Sigmoid Function**:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
* **Why it's essential:** Without this, the entire network is just a linear equation. Linear equations can only solve simple problems. Sigmoid allows the network to learn "curves" and complex patterns.
* **The S-Curve:** It squashes any input into a value between $0$ and $1$, representing the probability of the neuron "firing."

### 3. Backpropagation (The Chain Rule)
This is the core of AI learning. When the AI makes a mistake, it calculates the **Gradient** using the derivative of the Sigmoid function:
$$\sigma'(z) = \sigma(z) \cdot (1 - \sigma(z))$$
The math works backward from the output error to the hidden weights. We calculate how much "blame" each weight deserves for the final error and adjust it.

### 4. Gradient Descent (The Optimization)
We update our weights by taking a small step in the opposite direction of the error:
$$W_{new} = W_{old} + (\text{Input}^T \cdot \text{Delta} \cdot \text{Learning Rate})$$
The **Learning Rate ($0.5$)** ensures the AI doesn't overreact to a single mistake.

---

## 💻 The Implementation (`neural_network.py`)

```python
import numpy as np

# --- 1. FUNCTIONS ---
def sigmoid(x):
    # Squashes values to between 0 and 1
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    # Calculates the slope of the sigmoid for backpropagation
    return x * (1 - x)

# --- 2. DATA ---
# XOR Inputs: [0,0], [0,1], [1,0], [1,1]
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
# XOR Truths: 0, 1, 1, 0
expected_output = np.array([[0], [1], [1], [0]])

# --- 3. INITIALIZATION ---
# Random weights break symmetry so neurons don't learn the same thing
hidden_weights = np.random.uniform(size=(2, 3))
output_weights = np.random.uniform(size=(3, 1))
hidden_bias = np.random.uniform(size=(1, 3))
output_bias = np.random.uniform(size=(1, 1))

lr = 0.5 # Step size for learning

# --- 4. TRAINING LOOP ---
for epoch in range(10001):
    # FORWARD PROPAGATION
    # Calculate Hidden Layer
    hidden_act = np.dot(inputs, hidden_weights) + hidden_bias
    hidden_out = sigmoid(hidden_act)
    
    # Calculate Output Layer
    output_act = np.dot(hidden_out, output_weights) + output_bias
    predicted = sigmoid(output_act)

    # BACKPROPAGATION
    # 1. Calculate Output Error
    error = expected_output - predicted
    d_predicted = error * sigmoid_derivative(predicted)
    
    # 2. Calculate Hidden Layer Error (tracing error backward)
    error_hidden = d_predicted.dot(output_weights.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_out)

    # WEIGHT UPDATES
    # Adjusting the "knobs" based on calculated error
    output_weights += hidden_out.T.dot(d_predicted) * lr
    hidden_weights += inputs.T.dot(d_hidden) * lr
    
    if epoch % 2000 == 0:
        print(f"Epoch {epoch} | Mean Error: {np.mean(np.abs(error)):.4f}")

print("\nFinal AI Prediction for XOR:")
print(predicted)
```

---

## 🏁 Summary for Beginners
* **Intelligence through Repetition:** The AI "learns" by seeing the same data 10,000 times and slowly refining its weights.
* **Vectorization:** We use NumPy because it calculates all 4 XOR rows simultaneously using matrix math, which is significantly faster than using loops.
* **The Goal:** By the end of the training, the AI will output numbers very close to `0` and `1`, having successfully "learned" the logic of XOR without ever being told the rules.

---
*Deep-dive project documentation for Advanced Python Learning.*
