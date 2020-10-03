import NeuralNetwork

adder = NeuralNetwork.Network([784,16,16,10],0.0001)

for _ in range(10):
    data_file = open("train.txt","r")

    data_num = int(data_file.readline())

    temp = 0
    counted = 0

    for t in range(data_num):

        example = []
        g = data_file.readline().split()

        example.append([int(g[i]) for i in range(1,len(g))])

        k = [0 for i in range(10)]
        k[int(g[0])] += 1
        example.append(k)

        if(int(g[0]) < 2):
            adder.train(example)
            temp += adder.cost(example)
            counted += 1

        if ((t+1)%100) == 0:
            print(str(temp/counted))
            temp = 0
            counted = 0

    data_file.close()

success = 0
counted = 0

test_file = open("train.txt","r")

test_num = int(test_file.readline())

for t in range(1000):
    case = []
    g = test_file.readline().split()

    case.append([int(g[i]) for i in range(1,len(g))])

    k = [0 for i in range(10)]
    k[int(g[0])] += 1
    case.append(k)

    if(int(g[0]) < 2):
        counted += 1
        adder.evaluate(case[0])

        output = []

        for x in range(len(adder.layers[-1])):
            output.append(int(adder.layers[-1][x] == max(adder.layers[-1])))

        if output == case[1]:
            success += 1


print("success ratio: " + str(success/(counted)))
    
    
    
