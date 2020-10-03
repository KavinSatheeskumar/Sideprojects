import NeuralNetwork
import random

ttt = NeuralNetwork.Network([9,5,1],0.1)

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


    ttt.evaluate(example[0])
    if ((ttt.layers[-1][0] >= 0.5) and (example[1][0] == 1)):
        success_tally += 1
    elif ((ttt.layers[-1][0] <= 0.5) and (example[1][0] == 0)):
        success_tally += 1

print(success_tally/100)
