import NeuralNetwork
import random
import math

def XOR():
    xor = NeuralNetwork.Network([2, 3, 1], 0.1)

    for x in range(100000):
        example = [[random.randint(0,1),random.randint(0,1)]]
        example.append([example[0][0] ^ example[0][1]])
        xor.train(example)

    success_tally = 0

    for x in range(100):
        example = [[random.randint(0,1),random.randint(0,1)]]
        example.append([example[0][0] ^ example[0][1]])

        output = xor.evaluate(example[0])

        if abs(output[0] - example[1][0]) < 0.5:
            success_tally += 1

    print("The success rate of the network at computing the XOR operation was: " + str(success_tally/100))

def tic_tac_toe():

    ttt = NeuralNetwork.Network([9,5,1],0.5)

    for x in range(100000):
        example = []

        example.append([random.randint(0,1) for _ in range(9)])

        if(example[0][0] == 1 and example[0][4] == 1 and example[0][8] == 1):
            example.append([1])

        elif(example[0][2] == 1 and example[0][4] == 1 and example[0][6] == 1):
            example.append([1])

        elif(example[0][0] == 1 and example[0][3] == 1 and example[0][6] == 1):
            example.append([1])

        elif(example[0][1] == 1 and example[0][4] == 1 and example[0][7] == 1):
            example.append([1])

        elif(example[0][2] == 1 and example[0][5] == 1 and example[0][8] == 1):
            example.append([1])

        elif(example[0][0] == 1 and example[0][1] == 1 and example[0][2] == 1):
                example.append([1])

        elif(example[0][3] == 1 and example[0][4] == 1 and example[0][5] == 1):
                example.append([1])

        elif(example[0][6] == 1 and example[0][7] == 1 and example[0][8] == 1):
                example.append([1])

        else:
            example.append([0])

        ttt.train(example)

    success_tally = 0

    for x in range(100):
        example = []

        example.append([random.randint(0,1) for _ in range(9)])

        if(example[0][0] == 1 and example[0][4] == 1 and example[0][8] == 1):
            example.append([1])

        elif(example[0][2] == 1 and example[0][4] == 1 and example[0][6] == 1):
            example.append([1])

        elif(example[0][0] == 1 and example[0][3] == 1 and example[0][6] == 1):
            example.append([1])

        elif(example[0][1] == 1 and example[0][4] == 1 and example[0][7] == 1):
            example.append([1])

        elif(example[0][2] == 1 and example[0][5] == 1 and example[0][8] == 1):
            example.append([1])

        elif(example[0][0] == 1 and example[0][1] == 1 and example[0][2] == 1):
                example.append([1])

        elif(example[0][3] == 1 and example[0][4] == 1 and example[0][5] == 1):
                example.append([1])

        elif(example[0][6] == 1 and example[0][7] == 1 and example[0][8] == 1):
                example.append([1])

        else:
            example.append([0])

        output = ttt.evaluate(example[0])
        if ((output[0] >= 0.5) and (example[1][0] == 1)):
            success_tally += 1
        elif ((output[0] <= 0.5) and (example[1][0] == 0)):
            success_tally += 1

    print("The success rate of the network was at evaluating a tic tac toe board: " + str(success_tally/100))

def sine_squared():
    sine = NeuralNetwork.Network([1,5,1],0.1)
    average_cost = 0

    for x in range(1000000):
        t = random.uniform(0,2*math.pi)
        average_cost += sine.cost([[t],[math.sin(t) * math.sin(t)]])
        sine.train([[t],[math.sin(t) * math.sin(t)]])
        if (x+1)%1000 == 0:
            average_cost = 0

    average_cost = 0

    for x in range(100):
        t = random.uniform(0,2*math.pi)
        average_cost += sine.cost([[t],[math.sin(t) * math.sin(t)]])/100

    print("The average difference between the function and the desired output squared is: " + str(average_cost))
    
