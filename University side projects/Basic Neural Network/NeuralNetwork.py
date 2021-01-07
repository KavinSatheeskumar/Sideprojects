from lin_module import *
import random

class Network:
    def __init__(self,ls,r):
        self.rate = r
        self.layer_sizes = ls

        self.layers = [
                [0 for _ in range(self.layer_sizes[i])]
                for i in range(len(self.layer_sizes))
            ]

        self.e_layers = self.layers[:]

        self.z_layers = self.layers[:]

        self.webbs = [
                [
                    [random.uniform(-5,5) for _ in range(self.layer_sizes[i+1])]
                    for __ in range(self.layer_sizes[i])
                ]
                for i in range(len(self.layer_sizes)-1)
            ]

        self.biases = [
                [random.uniform(-5,5) for _ in range(self.layer_sizes[i+1])]
                for i in range(len(self.layer_sizes)-1)
            ]

    def evaluate(self,i):
        self.layers[0] = i

        for i in range(len(self.layers)-1):
            self.z_layers[i+1] = add_vec(matrix_mult(self.webbs[i],self.layers[i]), self.biases[i])
            self.layers[i+1] = sigmoid(self.z_layers[i+1])

        return (self.layers[-1])

    #This function has brought me so much pain...
    def train(self,example):
        self.evaluate(example[0])

        diff = sub_vec(self.layers[-1], example[1])
        self.e_layers[-1] = mult_vec(diff,d_sigmoid(self.z_layers[-1]))

        for x in range(len(self.e_layers)-1,0,-1):
            trans_prod = matrix_mult(transpose(self.webbs[x-1]),self.e_layers[x])
            self.e_layers[x-1] = mult_vec(trans_prod,d_sigmoid(self.z_layers[x-1]))

        for i in range(len(self.biases)):
            self.biases[i] = sub_vec(self.biases[i],scale(self.rate,self.e_layers[i+1]))

        for x in range(len(self.webbs)):
            for i in range(len(self.webbs[x])):
                for j in range(len(self.webbs[x][0])):
                    self.webbs[x][i][j] -= self.rate*(self.layers[x][i]*self.e_layers[x+1][j])

    def display(self):
        for x in range(len(self.layers)-1):
            for y in self.webbs[x]:
                print(y)
            print("----")
            print(self.biases[x])
            print("====")

    def cost(self, example):
        self.evaluate(example[0])

        output = 0

        for x in range(len(example[1])):
            output += (self.layers[-1][x] - example[1][x]) ** 2

        return output